# ASCII Thunder Ball: Learning How To Create A Game Engine

The Thunder Ball is a command prompt game that puts you in control of a bouncing ball, letting you playfully make it zip around your terminal at high speeds. How delightful! :D

I crafted this game in 2022, inspired by the exhaustion of a day spent skiing. While basking in the warmth of a chimney, sipping hot chocolate, and sharing the moment with my ageing father as we tuned into the news, I dedicated a few hours to creating this little gem. Later, I invested additional time refining the code. Developing a game engine is not rocket science. In fact, it's much simpler than one might think.

![nice_bounces.gif](https://github.com/FlorianFasmeyer/ASCII-Thunder-Ball/blob/main/images/nice_bounces.gif)

The Thunder Ball emerged as an unintended outcome of my game engine, built entirely from scratch. I adhered to a self-imposed restriction of avoiding the internet and confined my coding activities to Microsoft's Code Block. Module downloads were the only exceptions granted. This coding venture had two objectives:

1. To test the challenges of constructing a 2D game engine with collision, 2d physics and basic graphics from *absolutely nothing*
2. To improve my coding skills and develop those Pythonman fingers! >:D

This engine seamlessly handles high-speed objects, ensuring they never mysteriously phase through the game world. The only limitations on speed arise from the air friction variables. You can remove all friction in code to witness the unstoppable force of the THUNDER BALL!

Admittedly, it's a modest project, not one to boast about extensively. But darn, I like it!

Now, here's where I must confess a deviation from my original rules: I peeked at Stack Overflow to acquaint myself with the pynput module. This module proved invaluable for controlling and monitoring the keyboard, and I did delve into its source code to grasp its intricacies. Exceptions, after all, can be enlightening!

# What's in the game?
1. Nice trails that become wider the faster you go.

![nice_trails.gif](https://github.com/FlorianFasmeyer/ASCII-Thunder-Ball/blob/main/images/nice_trails.gif)

2. Unlimited speed!

![accumulate_speed.gif](https://github.com/FlorianFasmeyer/ASCII-Thunder-Ball/blob/main/images/accumulate_speed.gif)

3. Procedural terrain generation
4. Snow! You can enable it by uncommenting the 66th line: ´# snow(grid)´ -> ´snow(grid)´

# How to run the game?
1. Download it

![download_it.gif](https://github.com/FlorianFasmeyer/ASCII-Thunder-Ball/blob/main/images/download_it.gif)

2. Install pynput and python in your favourite virtual environment

![executing the command - pip install pynput](https://raw.githubusercontent.com/FlorianFasmeyer/ASCII-Thunder-Ball/main/images/pip_pynput.gif)

3. Run it
   
![Download the fine and write "python ASCII_thunder_ball.py"](https://github.com/FlorianFasmeyer/ASCII-Thunder-Ball/blob/main/images/easy_to_run.gif)

# Acknowledgements

I express my sincere gratitude to [Paul Ami Jeanbourquin](https://www.linkedin.com/in/paul-jeanbourquin-44a65bba/?originalSubdomain=ch) for his insightful suggestion to replace the "clear screen" command with the more efficient approach of resetting the console index to its initial position (0,0). This solution completely eliminates the flickering issue. Thank you, Paul, for your valuable contribution!
