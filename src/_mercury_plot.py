# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import orbitplotkit as opk


mpl.rcParams['lines.markersize'] = 5
a_res = (4/3) ** (2/3) * 1
folder = "mercury/"


def plotMaxe(alltp_init, alltp_max):
    t_i, a_i, e_i = alltp_init[:, 0], alltp_init[:, 1], alltp_init[:, 3]
    t_m, a_m, e_m = alltp_max[:, 0], alltp_max[:, 1], alltp_max[:, 3]
    fig, ax = plt.subplots()
    ax.plot([a_i, a_m], [e_i, e_m], color='black', alpha=0.1)
    sc = opk.scatterColorPlot(ax, a_i, e_i, t_i, 'a', 'e',
                              'a-maxe', (1.04, 1.3), (0, 80))
    sc = opk.scatterColorPlot(ax, a_m, e_m, t_m, 'a', 'e',
                              'a-maxe', (1.04, 1.3), (0, 80))

    ax.plot((a_res, a_res), (0, 1), color='red')
    fig.tight_layout()
    plt.colorbar(sc)
    plt.show()


def readOut(name):
    file = open(folder+name+".out", "r")
    tp = np.loadtxt(file, usecols=(0, 1, 2, 3, 4, 5, 6), skiprows=4)
    t, a, e, I, ome, Ome, M = tp[:, 0], tp[:, 1], tp[:,
                                                     2], tp[:, 3], tp[:, 4], tp[:, 5], tp[:, 6]
    return [t, a, e, I, ome, Ome, M]


name = np.arange(101, 129)

t2, a2, e2, I2, ome2, Ome2, M2 = readOut("EARTHMOO")

alltp_init = np.empty(shape=(0, 7))
alltp_max = np.empty(shape=(0, 7))
# print(alltp)

alpha = 0.5
start = 0
end = 5e8

for i in name:
    t1, a1, e1, I1, ome1, Ome1, M1 = readOut(str(i))

    alltp_init = np.vstack(
        (alltp_init, np.array([t1[-1], a1[0], e1[0], I1[0], ome1[0], Ome1[0], M1[0]])))
    alltp_max = np.vstack(
        (alltp_max, np.array([t1[-1], np.mean(a1), np.max(e1), np.max(I1), ome1[0], Ome1[0], M1[0]])))
    if True:
        fig, axes = plt.subplots(2, 2)
        axes[0, 0].plot(t1, a1, alpha=alpha)
        axes[0, 0].set_xlabel('t')
        axes[0, 0].set_ylabel('a')
        axes[0, 0].set_title('t-a')
        axes[0, 0].set_xlim(start, end)

        axes[0, 1].plot(t1, e1, alpha=alpha)
        axes[0, 1].set_xlabel('t')
        axes[0, 1].set_ylabel('e')
        axes[0, 1].set_title('t-e')
        axes[0, 1].set_xlim(start, end)

        axes[1, 0].plot(t1, I1, alpha=alpha)
        axes[1, 0].set_xlabel('t')
        axes[1, 0].set_ylabel('I')
        axes[1, 0].set_title('t-I')
        axes[1, 0].set_xlim(start, end)

        axes[1, 1].plot(t1, ome1, alpha=alpha)
        axes[1, 1].set_xlabel('t')
        axes[1, 1].set_ylabel('omega')
        axes[1, 1].set_title('t-omega')
        axes[1, 1].set_xlim(start, end)
        fig.tight_layout()
        plt.savefig(str(i)+".png", dpi=200)
        # plt.show()
# plotMaxe(alltp_init, alltp_max)
