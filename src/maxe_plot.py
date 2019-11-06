# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def wrapTo360(phi):
    return phi % 360


mpl.rcParams['lines.markersize'] = 1.5
a_res = (4/3) ** (2/3) * 1


def plotMaxe(name):
    file = open(name, "r")
    maxe = np.loadtxt(file, usecols=(0, 1, 2))
    t, a, e = maxe[:, 0], maxe[:, 1], maxe[:, 2]
    fig, ax = plt.subplots()
    sc = scatterColorPlot(ax, a, e, t, 'a', 'e',
                          'a-maxe', (1.04, 1.3), (0, 0.28))
    ax.plot((a_res, a_res), (0, 1), color='red')
    fig.tight_layout()
    plt.colorbar(sc)
    plt.savefig("{0:s}.png".format(name))
    plt.show()


def scatterColorPlot(ax, x, y, c, xlable, ylabel, title, xlim, ylim):
    sc = ax.scatter(x, y, c=c, cmap="RdYlBu",
                    norm=mpl.colors.LogNorm(vmin=1e6, vmax=1e9))
    ax.set_xlabel(xlable)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xlim(xlim[0], xlim[1])
    ax.set_ylim(ylim[0], ylim[1])
    return sc


for name in ["maxe_1gyr.out"]:
    plotMaxe(name)
