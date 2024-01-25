# ASCII Thunder Ball: Anti-Clipping at High Speeds in a Game Engine

The Thunder Ball is a command prompt game engine that puts you in control of a bouncing ball, letting you playfully make it zip around your terminal at high speeds.

![nice_bounces.gif](https://github.com/FlorianFasmeyer/ASCII-Thunder-Ball/blob/main/images/nice_bounces.gif)

This game engine was created in 2022, inspired by the exhaustion of a day spent skiing. Lost in my thoughts, I reminisced of a typical game engine glitch, one encountered in a previous game of mine: [Attack Of The Nullptrs](https://github.com/FlorianFasmeyer/Attack-of-the-nullptrs). Said glitch is common in most game engines and is called "clipping"; it happens when a game object goes so fast that it phases through other objects and the terrain. This happens because fast-moving objects move multiple pixels at a time for every game update (game tick). See in the below example, the object moving at speed 6 fails to collide with the square:

![clipping_speed.gif](https://github.com/FlorianFasmeyer/ASCII-Thunder-Ball/blob/main/images/clipping_speed.png)

This glitch happens in games where the developer did not intend for the player character to go past a certain speed, a speed below which the player character would have a wide enough collision box to detect another object. Speedrunners often use this glitch to phase through walls and escape beyond the boundaries of the game.

The ASCII Thunderball game engine explores this issue through a naive "simulate everything" approach, where each minimal unit of movement is recorded and tested for collision. I wanted to see the impact of such method on performances.

While creating this game engine, I adhered to a self-imposed "dry-chicken" restriction: avoiding the internet and confining my coding activities to Microsoft's Code Block. Module downloads were the only exceptions granted. I wanted to see how far I could go without IDE and Stackoverflow. It went well and took only two and a half hours. :)


# What's in the game?
1. Nice trails that become wider the faster you go.

![nice_trails.gif](https://github.com/FlorianFasmeyer/ASCII-Thunder-Ball/blob/main/images/nice_trails.gif)

2. Unlimited speed!

![accumulate_speed.gif](https://github.com/FlorianFasmeyer/ASCII-Thunder-Ball/blob/main/images/accumulate_speed.gif)

3. Procedural terrain generation
4. Snow! You can enable it by uncommenting the 66th line: ´# snow(grid)´ (remove the #)

# How to run the game?
1. Download it

![download_it.gif](https://github.com/FlorianFasmeyer/ASCII-Thunder-Ball/blob/main/images/download_it.gif)

2. Install pynput and python in your favourite virtual environment

![executing the command - pip install pynput](https://raw.githubusercontent.com/FlorianFasmeyer/ASCII-Thunder-Ball/main/images/pip_pynput.gif)

3. Run it
   
![Download the fine and write "python ASCII_thunder_ball.py"](https://github.com/FlorianFasmeyer/ASCII-Thunder-Ball/blob/main/images/easy_to_run.gif)

# Acknowledgements

I thank [Paul Ami Jeanbourquin](https://www.linkedin.com/in/paul-jeanbourquin-44a65bba/?originalSubdomain=ch) for his suggestion on a better screen refresh method.
