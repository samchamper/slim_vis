# slim_vis

A simple python matplotlib script for visualizing and saving the output of a SLiM spatial simulation.
For information on the SLiM modelling framework, see https://messerlab.org/slim/.

SLiM already has a visualization/GUI for use on Mac computers. However, for visualizing SLiM runs in a
linux environment, when doing remote computation, or even just when it is desirable to export a
visualization to a video, this tool may be useful.

This repository has a demo showing the kind of videos that this program creates.
See: https://raw.githubusercontent.com/samchamper/slim_vis/master/pop_supression_example.mp4

## Author:

Sam Champer

## Requirements:
* python3 (https://www.python.org/downloads/; make sure to "add python path" when you install it)
* ffmpeg (ffmpeg.org; you will need to add ffmpeg to your path if you are on windows.
    See: https://www.wikihow.com/Install-FFmpeg-on-Windows)
* pipenv (after installing python, run ``pip install pipenv``)

## Installation and Usage:
1. First, generate a file that this program can read.
    See: https://github.com/samchamper/slim_vis/blob/master/generating_slim_output.md.

1. Place the generated movie file in the directory with this program.

1. Run the following command to install python dependencies:
```
pipenv install
```
Then you can run the program via:
```
pipenv run vis
```
* Optional command line arguments (don't actually include the "<>" brackets):
1. ``-src <filename>`` to specify the source. Default ``slim_movie``
1. ``-fps <number>`` to specify the fps of the animation. Each frame is a generation, 
    so this is also generations per second. Default 8.
1. ``-s`` individual size. Increases for very small populations, decrease for large ones. Default 3.
1. ``-dim`` The dimensions of the output. Default is 1000, resulting in a 1000*1000 animation.

* For example:
```
pipenv run vis -src data_file.txt -fps 8 -s 4 -dim 1080
```

* Alternate install flow: dependencies can also be installed using venv, though it's less cool.
    To do so, run ``make install`` and then to run the program, run ``make run``.

## Notes:
Adding the code to slim to export data to a file that can be read by this program greatly increases SLiM's
runtime - by as much as a factor of 2. File I/O is slow.

Warning: It can take quite a long time to generate a movie for slim runs with many hundreds/thousands of generations!

The data files that the SLiM code outputs can be somewhat large: a SLiM run with 10k population and 100
generations can be close to 20 megabytes.
