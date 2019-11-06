# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
# import alltp_plot


def wrapTo360(phi):
    return phi % 360


mpl.rcParams['lines.markersize'] = 0.5
mpl.rcParams['lines.linewidth'] = 1
alpha = 0.5
start = 20e6
end = 40e6


def plotUa(name):
    file = open(name, "r")
    ua = np.loadtxt(file, usecols=(0, 1, 2, 3, 4, 5, 6))

    t, a, e, I, Ome, ome, M = ua[:, 0], ua[:,
                                           1], ua[:, 2], ua[:, 3], ua[:, 4], ua[:, 5], ua[:, 6]

    axes[0, 0].plot(t, a, alpha=alpha)
    axes[0, 0].set_xlabel('t')
    axes[0, 0].set_ylabel('a')
    axes[0, 0].set_title('t-a')
    axes[0, 0].set_xlim(start, end)

    axes[0, 1].plot(t, e, alpha=alpha)
    axes[0, 1].set_xlabel('t')
    axes[0, 1].set_ylabel('e')
    axes[0, 1].set_title('t-e')
    axes[0, 1].set_xlim(start, end)

    axes[1, 0].plot(t, I, alpha=alpha)
    axes[1, 0].set_xlabel('t')
    axes[1, 0].set_ylabel('I')
    axes[1, 0].set_title('t-I')
    axes[1, 0].set_xlim(start, end)

    axes[1, 1].plot(t, ome, alpha=alpha)
    axes[1, 1].set_xlabel('t')
    axes[1, 1].set_ylabel('omega')
    axes[1, 1].set_title('t-omega')
    axes[1, 1].set_xlim(start, end)

    axes[2, 0].plot(t, Ome, alpha=alpha)
    axes[2, 0].set_xlabel('t')
    axes[2, 0].set_ylabel('Omega')
    axes[2, 0].set_title('t-Omega')
    axes[2, 0].set_xlim(start, end)

    axes[2, 1].plot(t, wrapTo360(ome+Ome), alpha=alpha)
    axes[2, 1].set_xlabel('t')
    axes[2, 1].set_ylabel('curly_pi')
    axes[2, 1].set_title('t-curly_pi')
    axes[2, 1].set_xlim(start, end)

    fig.tight_layout()
    # plt.savefig(name+".png", dpi=200)
    # plt.show()


fig, axes = plt.subplots(3, 2)
for name in ["ua.127", "ua.200"]:
    plotUa("10-11/"+name)
# plt.savefig("10-11/" + "ua.all_nomun"+".png", dpi=200)
plt.show()
