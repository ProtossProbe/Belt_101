# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from scipy.signal import medfilt


mu_y = 1.66013679527193009e-7
mu_v = 2.44783833966454430e-6
mu_e = 3.04043264264672381e-6
mu_m = 3.22715144505386530e-7
mu_j = 9.54791938424326609e-4
mu_s = 2.85885980666130812e-4
mu_u = 4.36624404335156298e-5
mu_n = 5.15138902046611451e-5

mu_group = np.array([mu_y, mu_v, mu_e, mu_m, mu_j, mu_s, mu_u, mu_n])

d_y = 0.387
d_v = 0.723
d_e = 1
d_m = 1.52
d_j = 5.20
d_s = 9.58
d_u = 19.20
d_n = 30.05

d_group = np.array([d_y, d_v, d_e, d_m, d_j, d_s, d_u, d_n])

hill = d_group * (mu_group/3)**(1./3.)


def wrapTo180(phi):
    phi = phi % 360
    for i in np.arange(phi.size):
        if phi[i] > 180:
            phi[i] -= 360
    return phi


def wrapTo360(phi):
    return phi % 360


def readElements(data, left, right):
    return [data[left:right, 0], data[left:right, 4], data[left:right, 5], data[left:right, 6], data[left:right, 7],
            data[left:right, 8], data[left:right, 9]]


def readElements_NoPos(data, left, right):
    return [data[left:right, 0], data[left:right, 1], data[left:right, 2], data[left:right, 3], data[left:right, 4],
            data[left:right, 5], data[left:right, 6]]


def calN(a, e, I):
    I = I / 180.0 * np.pi
    return np.sqrt(a) * (np.sqrt(1 - e**2) * np.cos(I) - 1)


def calS(a, e):
    return np.sqrt(a) * (1 - np.sqrt(1 - e * e))


def calG(a, e, I):
    return np.sqrt(a) * np.sqrt(1 - e * e)


def calSz(a, e, I):
    return calG(a, e, I) * (1+np.cos(I / 180.0 * np.pi))


def calH(a, e, I):
    return np.sqrt(1 - e * e) * np.cos(I / 180.0 * np.pi)


def poinSect_M(data_a, data_p):
    row, col = data_a.shape
    result_a = np.empty(shape=[0, col])
    result_p = result_a
    focus = data_a[:, 9]
    for i in np.arange(row - 1):
        if focus[i + 1] - focus[i] < 0:
            if focus[i + 1] < np.abs(360 - focus[i]):
                result_a = np.vstack((result_a, data_a[i + 1]))
                result_p = np.vstack((result_p, data_p[i + 1]))
            else:
                result_a = np.vstack((result_a, data_a[i]))
                result_p = np.vstack((result_p, data_p[i]))
    return result_a, result_p


mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.markersize'] = 0.5

mu = 1e-3
# target1 = ["RJ2.txt", "RJ2_2.txt"]
# target2 = ["SATURN.txt", "SATURN_2.txt"]
LOCATION = 'vatira/'

target1 = ["2019LF6.out", "ZTF09k5.out"]
target2 = "VENUS.out"
fig1 = plt.figure()
ax1 = fig1.add_subplot(111, projection='polar')
ax1.set_xlim(0, 2*np.pi)
# ax1.set_ylim(0, 0.2)

fig2, (ax2, ax3, ax4, ax5, ax6) = plt.subplots(5, sharex=True)

for target in target1:
    data_ast = np.loadtxt(LOCATION+target, skiprows=4)
    data_pla = np.loadtxt(LOCATION+target2, skiprows=4)

    num = data_ast.shape[0]
    print(num)

    [t1, a1, e1, I1, ome1, Ome1, M1] = readElements_NoPos(
        data_ast, 0, num)

    [t2, a2, e2, I2, ome2, Ome2, M2] = readElements_NoPos(
        data_pla, 0, num)

    omeb = ome1 + Ome1
    lambda_ast = omeb + M1
    lambda_pla = ome2 + Ome2 + M2

    phi1 = wrapTo180(2*lambda_ast - 3*lambda_pla + 1*omeb)
    omega = np.unwrap(ome1 * np.pi / 180) * 180 / np.pi

    size = 0.1
    alp = 0.5

    ax1.scatter(ome1/180*np.pi, e1, s=1, alpha=0.1)

    ax2.scatter(t1, a1, s=size, alpha=alp)
    ax2.set_ylabel('a')
    ax2.plot([0, t1[-1]], [0.552004, 0.552004], color='red')

    ax3.scatter(t1, e1, s=size, alpha=alp)
    ax3.set_ylabel('e')
    # ax3.set_yscale('log')
    ax4.scatter(t1, I1, s=size, alpha=alp)
    ax4.set_ylabel('I')
    ax5.scatter(t1, phi1, s=size, alpha=alp)
    ax5.set_ylabel('phi')
    # ax5.set_yscale('log')
    # ax5.plot([0, t1[-1]], [0.005, 0.005])
    ax6.scatter(t1, ome1, s=size, alpha=alp)
    ax6.set_ylabel('ome')

plt.show()
