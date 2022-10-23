"""
Author: Sam Champer

Simple python matplotlib script for visualizing and saving the output of a SLiM spatial simulation.

Note:   This program by default looks for a file called 'slim_movie', but this can be overridden
        by specifying the filename by adding it to the command line when the program is run.
        For a list of command line arguments, run the program followed by -h

Usage: To use this program, code needs to be added to SLiM to output a file that this program can read.

See the github: https://github.com/samchamper/slim_vis
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from argparse import ArgumentParser


def animate(i, subplot, xs, ys, cs):
    """
    Update the animation each frame with the data for that generation.
    """
    print(f"   Drawing generation {i}/{len(xs)} \r", end="", flush=True)
    subplot.clear()
    subplot.set_title(f"Gen {i}")
    subplot.set_ylim(0, 1)
    subplot.set_xlim(0, 1)
    subplot.scatter(xs[i], ys[i], color=cs[i], s=individual_size)


def main():
    """
    Program flow:
    1. Open file with position and color data output from slim.
    2. Parse data into lists for x coords, y coords, and colors.
    3. Make matplotlib plot with an animation function that uses the data.
    4. Export the plot as an mp4.
    """
    # Read and parse data from the file into a list of
    # x coords, y coords, and colors for each generation:
    print(f"Reading {source}...")
    with open(source, 'r') as f:
        data = f.read()
    data = data[1:].split('G\n')
    for gen in range(len(data)):
        data[gen] = data[gen][1:-1].split('\n')
    xs = [[] for _ in range(len(data))]
    ys = [[] for _ in range(len(data))]
    cs = [[] for _ in range(len(data))]
    final_gen_with_activity = 0
    for gen in range(len(data)):
        for ind in range(len(data[gen])):
            split = data[gen][ind].split()
            if len(split) > 0:  # Skip empty generations.
                xs[gen].append(int(split[0], 16) / 4095)
                ys[gen].append(int(split[1], 16) / 4095)
                cs[gen].append([int(split[2], 16) / 255, int(split[3], 16) / 255, int(split[4], 16) / 255])
                final_gen_with_activity = gen

    # End animation on the last frame with living individuals.
    xs = xs[:final_gen_with_activity + 1]
    ys = ys[:final_gen_with_activity + 1]
    cs = cs[:final_gen_with_activity + 1]

    print("Generating animation...")
    # Create and configure a matplotlib figure, then call the animation function using the data:
    if dark:
        style.use('dark_background')
    else:
        style.use('default')
    fig = plt.figure(figsize=(dimensions/100, dimensions/100))
    subplot = fig.add_subplot(1, 1, 1)
    subplot.xaxis.set_visible(False)
    subplot.yaxis.set_visible(False)
    anim = animation.FuncAnimation(fig, animate, frames=len(xs), interval=1000/fps, fargs=(subplot, xs, ys, cs))
    fig.tight_layout(pad=2.5)
    # Save the animation, and then display it in a window.
    anim.save(f'{source}.mp4', writer=animation.writers['ffmpeg'](fps=fps))
    # plt.show()  # Not particularly useful to show the plot after outputting the movie, but might have a purpose?
    print(f"Animation written to {source}.mp4.")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-src', '--source', default="slim_movie", type=str,
                        help='File containing positional data. Default slim_movie')
    parser.add_argument('-fps', '--fps', default=10, type=int,
                        help='Frames (generations) per sec for the animation. Default 10.')
    parser.add_argument('-s', '--individual_size', default=5, type=int,
                        help='Dot size of individuals. Lower this for high pops, or things will be messy. Default 5.')
    parser.add_argument('-dim', '--dimensions', default=1080, type=int,
                        help='Dimensions of the animation. Default 1080 (1080*1080 animation).')
    parser.add_argument('-light', '--light_background', dest='dark', action='store_false', default=True,
                        help='Toggle to a simulation with a light background.')
    args = parser.parse_args()
    fps = args.fps
    dimensions = args.dimensions
    individual_size = args.individual_size
    source = args.source
    dark = args.dark
    main()
