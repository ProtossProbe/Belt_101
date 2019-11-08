# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

total = 3000
folder = "11-06/"
fig, ax = plt.subplots()


def plotDiscard(name):
    file = open(name, "r")
    line = file.readline()
    discard_time = []
    while line:
        if line[1] == "P":
            line = file.readline()
            discard_time.append(float(line))
        else:
            line = file.readline()

    discard_time = np.sort(np.array(discard_time))

    ax.plot(discard_time, np.arange(len(discard_time)))
    ax.semilogx(discard_time, total-np.arange(len(discard_time)))
    ax.plot([4.6E9, 4.6E9], [0, 3000], color='red')
    ax.plot([0, 4.6E9], [3000, 3000], color='red')

    major_ticks = [1E1, 1E2, 1E3, 1E4, 1E5, 1E6, 1E7, 1E8, 1E9, 1E10]
    minor_ticks = [5, 5E1, 5E2, 5E3, 5E4, 5E5, 5E6, 5E7, 5E8, 5E9, 5E10]
    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)

    ax.set_xlim(1, 5E9)
    ax.grid(linestyle='dashed', which='major')
    ax.grid(linestyle='dotted', which='minor')


plotDiscard(folder+"discard_300myr.out")
plotDiscard(folder+"discard_1gyr.out")
plt.savefig("{0:s}.png".format("discard_comparison2"))
plt.show()
