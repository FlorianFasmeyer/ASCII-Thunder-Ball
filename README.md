# ASCII Thunder Ball: Learning How To Create A Game Engine

The Thunder Ball is a command prompt game that puts you in control of a bouncing ball, letting you playfully make it zip around your terminal at high speeds. How delightful! :D

Note: The flickering you observe in the images results from the image recording software ScreenToGif (a tool I highly recommend). In actual practice, the experience will be significantly smoother.

I crafted this game in 2022, inspired by the exhaustion of a day spent skiing. While basking in the warmth of a chimney, sipping hot chocolate, and sharing the moment with my ageing father as we tuned into the news, I dedicated ~3 hours to creating this 277-line of code gem. Later, I invested additional time refining the code. Developing a game engine is not rocket science. In fact, it's much simpler than one might think.

![nice_bounces.gif](https://github.com/FlorianFasmeyer/ASCII-Thunder-Ball/blob/main/images/nice_bounces.gif)

The Thunder Ball emerged as an unintended outcome of my game engine, built entirely from scratch. I adhered to a self-imposed restriction of avoiding the internet and confined my coding activities to Microsoft's Code Block. Module downloads were the only exceptions granted. This coding venture had two objectives:

1. To test the challenges of constructing a 2D game engine with collision and 2d physics.
2. To improve my coding skills and code without bugs – developing those Pythonman fingers! >:D

This engine seamlessly handles high-speed objects, ensuring they never mysteriously phase through the game world. The only limitations on speed arise from friction variables. You can push the limits by removing all friction and witnessing how your computer copes with the unstoppable force of the THUNDER BALL!

Admittedly, it's a modest project, not one to boast about extensively. But darn it, I like it!

Now, here's where I must confess a deviation from my original rules: I peeked at Stack Overflow to acquaint myself with the pynput module. This module proved invaluable for controlling and monitoring the keyboard, and I did delve into its source code to grasp its intricacies. Exceptions, after all, can be enlightening!

# What's in the game?
1. Nice trails that become wider the faster you go.

![nice_trails.gif](https://github.com/FlorianFasmeyer/ASCII-Thunder-Ball/blob/main/images/nice_trails.gif)

2. Unlimited speed!

![accumulate_speed.gif](https://github.com/FlorianFasmeyer/ASCII-Thunder-Ball/blob/main/images/accumulate_speed.gif)

# How to run the game?
1. Download it

![download_it.gif](https://github.com/FlorianFasmeyer/ASCII-Thunder-Ball/blob/main/images/download_it.gif)

2. Install pynput and python in your favourite virtual environment: ´pip install pynput python´

3. Run it
   
![Download the fine and write "python ASCII_thunder_ball.py"](https://github.com/FlorianFasmeyer/ASCII-Thunder-Ball/blob/main/images/easy_to_run.gif)
