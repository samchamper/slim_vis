# slim_vis

A simple python matplotlib script for visualizing and saving the output of a SLiM spatial simulation.

SLiM already has a visualization/GUI for use on Mac computers. However, for visualizing SLiM runs in a linux environment, when doing
remote computation, or even just when it is desirable to export a visualization to a video, this tool may be useful.

This repository has a demo showing the kind of videos that this program creates.
See: https://raw.githubusercontent.com/samchamper/slim_vis/master/pop_supression_example.mp4

## Author:

Sam Champer

## Requirements:
* python3 (https://www.python.org/downloads/; make sure to "add python path" when you install it)
* ffmpeg (ffmpeg.org; you will need to add ffmpeg to your path if you are on windows. See: https://www.wikihow.com/Install-FFmpeg-on-Windows)
* pipenv (after installing python, run ``pip install pipenv``)

## Installation and Usage:
1. First, generate a file that this program can read. See: https://github.com/samchamper/slim_vis/blob/master/generating_slim_output.md.

1. Place the generated movie file in the directory with this program.

1. Run the following command to install python dependencies:
```pipenv install```
Then you can run the program via:
```pipenv run vis``
You can add an optional command line argument if the movie data file doesn't have the default filename "slim_movie":
```pipenv run vis name_of_movie_data_file.txt```

## Notes:
Adding the code to slim to export data to a file that can be read by this program greatly increases SLiM's
runtime - by as much as a factor of 2. File I/O is slow.

Warning: It can take quite a long time to generate a movie for slim runs with many hundreds/thousands of generations!
For very long runs, the fps parameter can be tweaked in the slim_vis.py file.

The data files that the SLiM code outputs can be somewhat large: a SLiM run with 10k population and 100
generations can be close to 20 megabytes.
