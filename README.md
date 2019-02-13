# slim_vis

Simple python matplotlib script for visualizing and saving the output of a SLiM spatial simulation.

## Author: 

Sam Champer

## Requirements:
python3

ffmpeg (ffmpeg.org)

## Usage:
1. First, generate a file that this program can read. See: https://github.com/samchamper/slim_vis/blob/master/generating_slim_output.txt

2. Run ``make install`` and then ``make run`` to visualize the SLiM run.

## Notes:
Adding the code to slim to export data to a file that can be read by this program greatly increases SLiM's runtime - by as much as a factor of 2. File I/O is slow.

Warning: Can take quite a long time to generate a movie for slim runs with many hundreds/thousands of generations! For very long runs, the fps parameter can be tweaked in the slim_vis.py file.

The data files that the SLiM code outputs can be somewhat large: a SLiM run with 10k population over 100 generations can be close to 20 megabytes.

SLiM already has a visualization/GUI for use on Mac computers. However, for visualizing SLiM runs in a linux environment, when doing remote computation, or even just when it is desirable to export a visualization to a video, this tool may be useful.

This repository has a demo showing the kind of videos that this program creates. See: https://raw.githubusercontent.com/samchamper/slim_vis/master/pop_supression_example.mp4

