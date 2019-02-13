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


def animate(i):
    ax.clear()
    ax.set_title("Gen {}".format(i))
    ax.set_ylim(0, 1)
    ax.set_xlim(0, 1)
    ax.scatter(xs[i], ys[i], color=cs[i], s=individual_size)


# Some parameters that one might want to tweak:
fps = 10
individual_size = 3
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
        xs[gen].append(int(split[0], 16) / 4095)
        ys[gen].append(int(split[1], 16) / 4095)
        cs[gen].append([int(split[2], 16) / 255, int(split[3], 16) / 255, int(split[4], 16) / 255])

# Create and configure a matplotlib figure,
# then call the animation function using the data:
style.use('dark_background')
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(1, 1, 1)
anim = animation.FuncAnimation(fig, animate, frames=len(data), interval=1000/fps)

# Save the animation, and then display it in a window.
anim.save('{}.mp4'.format(filename), writer=animation.writers['ffmpeg'](fps=fps))
plt.show()
