# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def wrapTo360(phi):
    return phi % 360


mpl.rcParams['lines.markersize'] = 1
a_res = (4/3) ** (2/3) * 1

fig, axes = plt.subplots()


def plotAlltp(name):
    file = open(name, "r")
    alltp = np.loadtxt(file, usecols=(1, 2, 3, 4, 5, 6))

    a, e, I, Ome, ome, M = alltp[:, 0], alltp[:,
                                              1], alltp[:, 2], alltp[:, 3], alltp[:, 4], alltp[:, 5]
    q = a*(1-e)
    scatterPlot(axes, a, e, 'a', 'e', 'a-e', (1.04, 1.3), (0, 0.2))
    # scatterPlot(axes[1], a, I, 'a', 'I', 'a-I', (1.04, 1.3), (0, 10))
    # scatterPlot(axes[2], a, q, 'a', 'q', 'a-q', (1.04, 1.3), (0.7, 1.2))
    axes.plot((a_res, a_res), (0, 1), color='red')

    # axes[2, 0].scatter(e, wrapTo360(ome+Ome))
    # axes[2, 0].set_xlabel('e')
    # axes[2, 0].set_ylabel('curly_pi')
    # axes[2, 0].set_title('e-curly_pi')


def scatterPlot(ax, x, y, xlable, ylabel, title, xlim, ylim):
    ax.scatter(x, y, alpha=0.5)
    ax.set_xlabel(xlable)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xlim(xlim[0], xlim[1])
    ax.set_ylim(ylim[0], ylim[1])


def plotEMBelt(name):
    data = np.genfromtxt(name, delimiter=',',
                         skip_header=1, usecols=(1, 2, 3))
    a, e, I = data[:, 0], data[:, 1], data[:, 2]
    q = a*(1-e)
    scatterPlot(axes, a, e, 'a', 'e', 'a-e', (1.04, 1.3), (0, 0.3))
    # scatterPlot(axes[1], a, I, 'a', 'I', 'a-I', (1.04, 1.3), (0, 10))
    # scatterPlot(axes[2], a, q, 'a', 'q', 'a-q', (1.04, 1.3), (0.5, 1.3))


for name in ["alltp_1gyr.out"]:
    plotEMBelt("em_belt.csv")
    # plotAlltp(name)
fig.tight_layout()
# plt.savefig("{0:s}.png".format(name))
plt.show()
