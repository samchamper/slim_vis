"""
Author: Sam Champer

Simple python matplotlib script for visualizing and saving the output of a SLiM spacial simulation.

Note:   This program by default looks for a file called slim_movie.txt, but this can be overridden
        by specifying the filename by adding it to the command line when the program is run.

Usage: To use this program, code needs to be added to SLiM to output a file that this program can read.

See the github: https://github.com/samchamper/slim_vis

"""

import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

# CONFIGURATION GLOBALS - CHANGE THESE TO CHANGE PROGRAM BEHAVIOR:
FPS = 10
INDIVIDUAL_SIZE = 3


def animate(i, subplot, xs, ys, cs):
    """
    Update the animation each frame with the data for that generation.
    """
    subplot.clear()
    subplot.set_title("Gen {}".format(i))
    subplot.set_ylim(0, 1)
    subplot.set_xlim(0, 1)
    subplot.scatter(xs[i], ys[i], color=cs[i], s=INDIVIDUAL_SIZE)


def main():
    """
    Program flow:
    1. Open file with position and color data output from slim.
    2. Parse data into lists for x coords, y coords, and colors.
    3. Make matplotlib plot with an animation function that uses the data.
    4. Export the plot as an mp4.
    5. Display the plot in a window.
    """
    # Default filenae.
    filename = "slim_movie"
    if len(sys.argv) > 1:
        # Get file name from command line.
        filename = sys.argv[1]

    # Read and parse data from the file into a list of
    # x coords, y coords, and colors for each generation:
    with open(filename, 'r') as f:
        data = f.read()
    data = data[1:].split('G\n')
    for gen in range(len(data)):
        data[gen] = data[gen][1:-1].split('\n')
    xs = [[] for _ in range(len(data))]
    ys = [[] for _ in range(len(data))]
    cs = [[] for _ in range(len(data))]
    for gen in range(len(data)):
        for ind in range(len(data[gen])):
            split = data[gen][ind].split()
            if len(split) > 0:  # Skip empty generations.
                xs[gen].append(int(split[0], 16) / 4095)
                ys[gen].append(int(split[1], 16) / 4095)
                cs[gen].append([int(split[2], 16) / 255, int(split[3], 16) / 255, int(split[4], 16) / 255])

    # Create and configure a matplotlib figure,
    # then call the animation function using the data:
    style.use('dark_background')
    fig = plt.figure(figsize=(6, 6))
    subplot = fig.add_subplot(1, 1, 1)
    anim = animation.FuncAnimation(fig, animate, frames=len(data), interval=1000/FPS, fargs=(subplot, xs, ys, cs))

    # Save the animation, and then display it in a window.
    anim.save('{}.mp4'.format(filename), writer=animation.writers['ffmpeg'](fps=FPS))
    plt.show()


if __name__ == "__main__":
    main()
