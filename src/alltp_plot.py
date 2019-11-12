# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import orbitplotkit as opk

folder = "11-06/"
fig, axes = plt.subplots(2, 2)


def plotAlltp(name):
    file = open(name, "r")
    alltp = np.loadtxt(file, usecols=(1, 2, 3, 4, 5))
    alltp[:, [3, 4]] = alltp[:, [4, 3]]

    opk.stdFourScatterPlot(axes, alltp, (1, 1.3), (0, 0.2), (0, 10))
    opk.resonancePlot(axes[0, 0], opk.resonanceLocation(
        2, 3, 4), (0, 1), color='red')
    opk.resonancePlot(axes[0, 0], opk.resonanceLocation(
        2, 4, 5), (0, 1), color='red')
    opk.resonancePlot(axes[0, 0], opk.resonanceLocation(
        1, 1, 2), (0, 1), color='orange')

    fig.tight_layout()
    plt.savefig("{0:s}.png".format(name), dpi=200)


for name in ["alltp_300myr"]:
    plotAlltp(folder+name+".out")

plt.show()
