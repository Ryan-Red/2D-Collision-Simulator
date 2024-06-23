# 2D Collision Simulator

[Collisions' Gif](example/2D_Collision_Gif.gif)
## Introduction
This project is a simple 2D collision simulator to test elastic and inelastic collision physics. 

This project is meant as a minimal working example that can be extended to include more complex forces. 

## What's Implemented
Parameters like the coefficient of restitution, collision detection and video generation are implemented.

## How to use

### Dependencies

This project depends on matplotlib and numpy, and also requires having ffmpeg installed on your computer.

To install matplotlib and numpy: `pip install matplotlib numpy`

To install ffmpeg go to: https://ffmpeg.org/download.html and follow the relevant steps.

### Running the program

First, make sure to modify the parameter:
```python
mpl.rcParams['animation.ffmpeg_path']
``` 
in the `simulator.py` code with the path to your ffmpeg installation. 

Then, simply run `python3 simulator.py` to run the program. The output video will be saved as an mp4 video.
