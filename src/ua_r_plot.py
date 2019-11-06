# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def wrapTo360(phi):
    return phi % 360


mpl.rcParams['lines.markersize'] = 0.5
mpl.rcParams['lines.linewidth'] = 1
alpha = 1
start = 0
end = 5e8


def plotUaR(particle, planet, kp, k):
    file = open(particle, "r")
    ua_tp = np.loadtxt(file, usecols=(0, 1, 2, 3, 4, 5, 6))

    t1, a1, e1, I1, Ome1, ome1, M1 = ua_tp[:, 0], ua_tp[:,
                                                        1], ua_tp[:, 2], ua_tp[:, 3], ua_tp[:, 4], ua_tp[:, 5], ua_tp[:, 6]
    file.close()
    count = t1.shape[0]
    end = t1[-1]

    file = open(planet, "r")
    ua_pl = np.loadtxt(file, usecols=(0, 1, 2, 3, 4, 5, 6),)

    t2, a2, e2, I2, Ome2, ome2, M2 = ua_pl[:count, 0], ua_pl[:count,
                                                             1], ua_pl[:count, 2], ua_pl[:count, 3], ua_pl[:count, 4], ua_pl[:count, 5], ua_pl[:count, 6]

    lambda_tp = ome1 + Ome1 + M1
    lambda_pl = ome2 + Ome2 + M2
    curly_pi = ome1 + Ome1
    phi = wrapTo360(kp * lambda_pl - k * lambda_tp - (kp-k)*curly_pi)

    a_res = (k/kp) ** (2/3) * a2[0]
    print(a_res)

    axes[0, 0].plot(t1, a1, alpha=alpha)
    axes[0, 0].plot((0, t1[-1]), (a_res, a_res), alpha=alpha, color='red')
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

    axes[1, 1].scatter(t1, ome1, alpha=alpha)
    axes[1, 1].set_xlabel('t')
    axes[1, 1].set_ylabel('omega')
    axes[1, 1].set_title('t-omega')
    axes[1, 1].set_xlim(start, end)
    axes[1, 1].set_ylim(0, 360)

    axes[2, 0].scatter(t1, Ome1, alpha=alpha)
    axes[2, 0].set_xlabel('t')
    axes[2, 0].set_ylabel('Omega')
    axes[2, 0].set_title('t-Omega')
    axes[2, 0].set_xlim(start, end)
    axes[2, 0].set_ylim(0, 360)

    axes[2, 1].scatter(t1, phi, alpha=alpha)
    axes[2, 1].set_xlabel('t')
    axes[2, 1].set_ylabel('phi '+str(kp)+'/'+str(k))
    axes[2, 1].set_title('t-phi '+str(kp)+'/'+str(k))
    axes[2, 1].set_xlim(start, end)
    axes[2, 0].set_ylim(0, 360)

    fig.tight_layout()
    # plt.savefig(name+".png", dpi=200)
    # plt.show()


fig, axes = plt.subplots(3, 2)
plotUaR("ua_19.nom200", "ua_e.nom200", kp=3, k=4)
# plt.savefig("10-11/" + "ua.all_nomun"+".png", dpi=200)
plt.show()
