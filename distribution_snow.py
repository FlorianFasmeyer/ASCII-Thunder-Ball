import msvcrt
import random
import math
import time
import os

os.system('color A')

# Screen.
width = 77
height = 24
empty = ' '
replace_empty = '.'

# Game.
FPS = 0.05 # Seconds.
spawn_range = (1, 2) # Time to spawn. Multiply with FPS. 

grid = [[empty]*width]*height # Empty space.
def generate_grid():
    grid = []
    for line in range(height):
        grid.append([empty]*width)

    return grid


grid = generate_grid()
stop = False
random_type = None
def main():
    global stop

    choose_random_type()

    while stop is False:
        time.sleep(FPS)
        animated_histogram()
        display(grid)

rand_func = None
def choose_random_type():
    global stop, rand_func, rand_args, width
    choice = None
    while choice == None: 
        print('''
               Choose a type of random distribution

               U - uniform
               T - triangular
               B - betavariate
               G - Gauss
               L - lognormvariate
               ____________________

               Q - Quite
              ''')
        choice = input().lower()
     
    range = (0, width-1)
    in_range = lambda x: x if 0 <= x < width else None

    if choice == 'q':
        stop = True
    elif choice == 'u':
        rand_func = lambda : round(random.uniform(*range))
    elif choice == 't':
        rand_func = lambda : round(random.triangular(*range))
    elif choice == 'b':
        args = choose_alpha_beta()
        rand_func = lambda : round(random.betavariate(*args)*range[1])
    elif choice == 'g':
        args = choose_alpha_beta(msg='''
               Enter your mean and standard deviation
               following the format: mu,stdv''')
        gauss = lambda : round(random.gauss(*args))
        rand_func = lambda : in_range(round(gauss()))
    elif choice == 'l':
        args = choose_alpha_beta(msg='''
               Enter your mean and standard deviation
               following the format: mu,stdv''')
        log = lambda : round(random.lognormvariate(*args))
        rand_func = lambda : in_range(round(log())) 
    else:
        print('Invalid choice.')


def choose_alpha_beta(msg=None):
    if msg == None:
        msg = '''
               Enter your alpha and beta
               following the format: a,b
        '''
    print(msg)
    choice = input()
    choice = choice.split(',')
    choice = tuple(int(x) for x in choice)    
    return choice
    

spawn_x = 0
spawn_timer = 0
def animated_histogram():
    global spawn_x, spawn_timer, grid, height, stop
    spawn_timer = spawn_timer-1
    if spawn_timer <= 0:
        spawn_x = None
        while spawn_x == None:
            spawn_x = rand_func()

        grid[0][spawn_x] = 'O'
        spawn_timer = random.randint(*spawn_range)

    for i in range(height-1, -1, -1):
        for j in range(width-1, -1, -1):
            if i < height-1:
                if grid[i][j] == 'O' and (grid[i+1][j] != 'O'):
                    grid[i][j] = replace_empty
                    grid[i+1][j] = 'O'
                elif grid[i+1][j] == 'O' and i == 0:
                    stop = True
                  

def display(grid):
    os.system('cls')
    image=''
    for line in grid:
        image += '\n'
        for char in line:
            image += char

    print(image)


main()
