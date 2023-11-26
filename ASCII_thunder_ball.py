from pynput import keyboard
import random
import math
import time
import os

# Constants.
WIDTH = 77
HEIGHT = 23
GRAVITY = 1
X_FRICTION = 0.02
Y_FRICTION = 0.02
DAMPING = 0.00  # When the ball bounces, it looses energy.
JUMP_STRENGTH = -2
MAX_HORIZONTAL_SPEED = 1000000
WALK_ACCELERATION = 1
SNOW = '~'
GROUND = '#'
AIR = ' '
PLAYER = 'O'
TIME_BETWEEN_FRAMES = 0.01  # Seconds.
TRAIL_DECAY = 0.1
TRAIL_SPEED_ICONS =  {
    11:  '.',
    17: '+',
    24: 'o',
    30: '0',
    float('inf'): '$'}


# Game states.
stop_game = False
snow_timer = 0
trail = []

# Player data.
pos_x, pos_y = 20, 8
vel_x, vel_y = 0.0, 0.0

# Player controls.
controls = {
    'w': False,  # Jump.
    'a': False,  # Left.
    'd': False,  # Right.
    keyboard.Key.esc: False  # Quit game.
}


def main():
    # Initialize the world grid.
    grid = generate_empty_world()  # Initialize an empty world.
    grid = generate_terrain(grid)
    grid[pos_y][pos_x] = PLAYER  # Display player character.

    # Begin listening to keyboard events.
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

    # Start game loop.
    global stop_game
    while stop_game is False:
        time.sleep(TIME_BETWEEN_FRAMES)
        trail_decay(grid)
        player_act(grid)
        move_player(grid)
        # snow(grid)
        display(grid, clear_screen=True)


# World and player generation.
def generate_empty_world():
    grid = []
    for line in range(HEIGHT):
        grid.append([AIR] * WIDTH)

    return grid


def generate_terrain(grid):
    terrain_height = 3
    for column in range(0, WIDTH):
        mod = random.randint(-2, 2)
        new_height = terrain_height + mod
        if 1 < new_height < 10:
            terrain_height = new_height

        for i in range(1, terrain_height):
            grid[HEIGHT-i][column] = GROUND

    return grid


# Player controls.
def on_press(key):
    try:
        controls[key.char] = True
    except AttributeError:
        pass  # If special char, do nothing!
    except KeyError:
        pass  # If not a move key, do nothing


def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener.
        return False

    try:
        controls[key.char] = False
    except AttributeError:
        pass  # If special char, do nothing!
    except KeyError:
        pass  # If not a move key, do nothing


def player_act(grid):
    if controls[keyboard.Key.esc] is True:  # Escape key.
        global stop_game
        stop_game = True

    if controls['w'] is True:  # Jump.
        jump(grid)

    if controls['d'] is True:  # Move right.
        if vel_x < MAX_HORIZONTAL_SPEED:
            force = min(MAX_HORIZONTAL_SPEED - vel_x, WALK_ACCELERATION)
            add_force(force, 0)

    if controls['a'] is True:  # Move left.
        if vel_x > -MAX_HORIZONTAL_SPEED:
            force = max(-MAX_HORIZONTAL_SPEED - vel_x, -WALK_ACCELERATION)
            add_force(force, 0)


def jump(grid):
    # If player touches the ground "#", then jump.
    if grid[pos_y+1][pos_x] == GROUND:
        add_force(0, JUMP_STRENGTH)


def add_force(x, y):
    global vel_x, vel_y
    vel_x += x
    vel_y += y


# World update.
def display(grid, clear_screen=True):
    if clear_screen:
        os.system('cls')

    image = ''
    for line in grid:
        image += '\n'
        for char in line:
            image += char

    global vel_x, vel_y
    print(image,
          f'\n velocity (x: {vel_x: 3.2f}, y: {vel_y: 3.2f})')


def move_player(grid):
    """ A fast moving player character can move multiple squares within the same frame. We simulate the full
        movement for every square in the grid, making sure we don't collide with anything or phase through walls.
    """
    global pos_x, pos_y, vel_x, vel_y, trail

    grid[pos_y][pos_x] = AIR  # Remove player character.

    # Normals indicate the movement direction.
    normal_x = int(math.copysign(1, vel_x))
    normal_y = int(math.copysign(1, vel_y))

    # Number of moves left before displaying the new frame.
    move_x = abs(round(vel_x))
    move_y = abs(round(vel_y))
    total_moves = move_x + move_y

    # Making the simulated path as straight as possible (pixel lines).
    # Example: If we have to move 7 squares by x and 2 by y, we want to update by batches: 7x, 2y => [xxx y xxx y x]
    # Note: "move_y and (move_x // move_y)" Avoids divide by zero error. Returns 0 when denominator is 0.
    update_batch_x = max(1, int(move_y and (move_x // move_y)))
    update_batch_y = max(1, int(move_x and (move_y // move_x)))


    # Simulate the full motion, one square at a time.
    while move_y + move_x > 0:
        update_y = update_batch_y
        update_x = update_batch_x
        while update_y > 0 and move_y > 0:
            update_y = update_y - 1
            vertical_collision = grid[pos_y + normal_y][pos_x] == GROUND
            if vertical_collision:  # Bounce.
                vel_y = int(-vel_y * (1-DAMPING))  # Apply damping.
                move_y = 0  # Stay on the ground to allow for a jump!
            else:
                pos_y = pos_y + normal_y
                move_y = move_y - 1

            # paint_trail(grid, pos_y, pos_x, get_speed(total_moves, move_x, move_y))
            paint_trail(grid, pos_y, pos_x, total_moves)

        while update_x and move_x > 0:
            update_x = update_x -1
            horizontal_collision = grid[pos_y][(pos_x + normal_x) % WIDTH] == GROUND
            if horizontal_collision:  # Bounce.
                vel_x = int(-vel_x * (1-DAMPING))  # Apply damping.
                move_x = move_x - 1
            else:
                pos_x = (pos_x + normal_x) % WIDTH
                move_x = move_x - 1

            # paint_trail(grid, pos_y, pos_x, get_speed(total_moves, move_x, move_y))
            paint_trail(grid, pos_y, pos_x, total_moves)


    ground_collision = grid[pos_y + 1][pos_x] == GROUND
    if not ground_collision:
        vel_y = vel_y + GRAVITY

    vel_x = vel_x * (1-X_FRICTION)
    vel_y = vel_y * (1-Y_FRICTION)

    grid[pos_y][pos_x] = PLAYER  # Draw player character.


def get_speed(total_moves, move_x, move_y):
    return total_moves - move_y - move_x


def paint_trail(grid, y, x, speed=1):
    grid[y][x] = get_trail_icon(speed)
    trail.append((pos_y, pos_x))


def get_trail_icon(moves_left):
    # Returns the appropriate trail according to the number of moves allowed.
    # "Speed" is used to refer to moves, where objects going fast will have a bigger, more impressive tail.
    # The base of the tail is ideally wider than the tip.
    for speed_range, icon in TRAIL_SPEED_ICONS.items():
        if moves_left < speed_range:
            return icon


def trail_decay(grid):
    global trail
    to_remove = int(len(trail) * TRAIL_DECAY) + 1
    for t in trail[:to_remove]:
        y, x = t[0], t[1]
        if grid[y][x] in TRAIL_SPEED_ICONS.values():
            grid[y][x] = AIR


    trail = trail[to_remove:]


def snow(grid):
    global snow_timer
    snow_timer = snow_timer-1

    # Spawn snow.
    if snow_timer <= 0:
        spawn_x = random.randint(0, WIDTH - 1)
        grid[0][spawn_x] = SNOW
        snow_timer = random.randint(1, 3)

    # Update snow fall.
    for i in range(HEIGHT - 1, -1, -1):
        for j in range(WIDTH - 1, -1, -1):
            if grid[i][j] == SNOW:
                if grid[i+1][j] == AIR:
                    grid[i][j] = AIR
                    grid[i+1][j] = SNOW


main()
