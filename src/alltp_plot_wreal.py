# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import orbitplotkit as opk

folder = "11-06/"
jpl_folder = "jpl_smdb/"


def wrapTo360(phi):
    return phi % 360


mpl.rcParams['lines.markersize'] = 1
a_res = (4/3) ** (2/3) * 1

fig, axes = plt.subplots(2)


def plotAlltp(name):
    file = open(name, "r")
    alltp = np.loadtxt(file, usecols=(1, 2, 3, 4, 5, 6))

    a, e, I, Ome, ome, M = alltp[:, 0], alltp[:,
                                              1], alltp[:, 2], alltp[:, 3], alltp[:, 4], alltp[:, 5]
    q = a*(1-e)
    opk.scatterPlot(axes[0], a, e, 'a', 'e', 'a-e', (1.04, 1.3), (0, 0.2))
    opk.scatterPlot(axes[1], a, I, 'a', 'I', 'a-I', (1.04, 1.3), (0, 10))
    opk.scatterPlot(axes[2], a, q, 'a', 'q', 'a-q', (1.04, 1.3), (0.7, 1.2))
    axes[0].plot((a_res, a_res), (0, 1), color='red')


def plotEMBelt(name):
    data = np.genfromtxt(name, delimiter=',',
                         skip_header=1, usecols=(1, 2, 3, 14))
    # data = data[data[:, -1] <= 23]
    a, e, I, H = data[:, 0], data[:, 1], data[:, 2], data[:, -1]

    d = np.power(10, 3.1236 - 0.5 * np.log10(0.15) - 0.2 * H) * 1000
    print(d.round())
    opk.scatterPlotWithSize(axes[0], a, e, d, 'a', 'e',
                            'a-e (with H)', (1.0, 1.2), (0, 0.1))
    opk.scatterPlotWithSize(axes[1], a, I, d, 'a',
                            'I', 'a-I (with H)', (1.0, 1.2), (0, 6))
    axes[0].scatter(1.095859465657055, .01678920060988707,
                    marker='+', color='white', s=40)
    axes[1].scatter(1.095859465657055, 3.817247697524332,
                    marker='+', color='white', s=40)
    axes[0].scatter(1.108845749770639, .04478812935240784,
                    marker='+', color='white', s=40)
    axes[1].scatter(1.108845749770639, 4.253254278006285,
                    marker='+', color='white', s=40)


for name in [folder+"alltp_1gyr.out"]:
    plotEMBelt(jpl_folder+"em_region(<=5).csv")
    # plotAlltp(name)
# fig.tight_layout()
# plt.savefig("{0:s}.png".format(name))
compressedAE = np.loadtxt(folder+"regional_ae.txt")
compressedAI = np.loadtxt(folder+"regional_aI.txt")
gridAE = np.flipud(np.reshape(compressedAE[:, 2], (4, 5)).T)
gridAI = np.flipud(np.reshape(compressedAI[:, 2], (4, 3)).T)
print(gridAI)

opk.NEOSSatModelAEPlot(axes[0], gridAE, alim=(
    1.025, 1.175), elim=(0.01, 0.09))
opk.NEOSSatModelAIPlot(axes[1], gridAI, alim=(
    1.025, 1.175), Ilim=(1, 5))
axes[0].set_aspect('auto')
axes[1].set_aspect('auto')
fig.tight_layout()
plt.show()
