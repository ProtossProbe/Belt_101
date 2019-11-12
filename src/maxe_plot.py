# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import orbitplotkit as opk

folder = "11-06/"
mpl.rcParams['lines.markersize'] = 1.5

fig, ax = plt.subplots()


def plotMaxe(name):
    file = open(name, "r")
    maxe = np.loadtxt(file, usecols=(0, 1, 2))
    t, a, e = maxe[:, 0], maxe[:, 1], maxe[:, 2]

    sc = opk.scatterColorPlot(ax, a, e, t, 'a', 'e',
                              'a-maxe', (1.04, 1.3), (0, 0.28))
    opk.resonancePlot(ax, opk.resonanceLocation(2, 3, 4), (0, 1), color='red')
    opk.resonancePlot(ax, opk.resonanceLocation(2, 4, 5), (0, 1), color='red')
    opk.resonancePlot(ax, opk.resonanceLocation(
        1, 1, 2), (0, 1), color='orange')
    fig.tight_layout()
    plt.colorbar(sc)
    plt.savefig("{0:s}.png".format(name), dpi=200)


for name in ["maxe_1gyr"]:
    plotMaxe(folder+name+".out")

plt.show()
