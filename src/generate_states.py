# -*- coding: UTF-8 -*-
import numpy as np
from random import *
from elements import *

n = 10
m = 10
num = n*m


def generateRandomStates(n, m):
    eles = []
    states = []
    for i in range(n):
        for j in range(m):
            a = np.random.uniform(1.04, 1.3)
            e = np.random.uniform(0, 0.04)
            I = np.random.uniform(0, 1)
            ome = np.random.uniform(0, 360)
            Ome = np.random.uniform(0, 360)
            f = np.random.uniform(0, 360)
            ele = [a, e, I, ome, Ome, f]
            eles.append(ele)
            state = e2c(ele)
            states.append(state)
    return eles, states


def writeSwiftTPIN(states):
    file = open("yh_tp.in", "w+")
    file.write(str(num)+"\n")
    for state in states:
        for dat in state[:3]:
            file.write(" {: 2.15f}".format(dat))
        file.write("\n")
        for dat in state[3:]:
            file.write(" {: 2.15f}".format(dat))
        file.write("\n")
        file.write("  0 0 0 0 0 0 0 0 0 0 0 0 0\n")
        file.write("  0.0d0 0.0d0 0.0d0 0.0d0 0.0d0\n")
        file.write("  0.0d0 0.0d0 0.0d0 0.0d0 0.0d0\n")
        file.write("  0.0d0 0.0d0 0.0d0\n")
    file.close()


def writeMercurySMALLIN(states):
    file = open("yh_small.in", "w+")
    file.write(
        ")O+_06 Small-body initial data  (WARNING: Do not delete this line!!)\n")
    file.write(
        ") Lines beginning with `)' are ignored.\n")
    file.write(
        ")-------------------------------------------------------------------\n")
    file.write(
        " style(Cartesian, Asteroidal, Cometary)=Asteroidal\n")
    file.write(
        ")------------------------d or D is not matter--0d0 is possible too--\n")
    for i, state in zip(np.arange(num), states):
        state[5] = np.rad2deg(true2mean(np.deg2rad(state[5]), state[1]))
        file.write(" {0:d}    ep={1:.1f}d0\n".format(i+101, 0))
        for dat in state[:3]:
            file.write(" {: 2.15f}".format(dat))
        file.write("\n")
        for dat in state[3:]:
            file.write(" {: 2.15f}".format(dat))
        file.write("\n")
        file.write(" 0.d0 0.d0 0.d0\n")
    file.close()


# eles, states = generateRandomStates(10, 10)
# writeSwiftTPIN(states)
# writeMercurySMALLIN(eles)


ele = [0.969885662977092, 0.754060237341030, 0.010234899608725,
       -3.510425656234479, 4.369664920091394, 0.059111270080286]
state = c2e(ele)
state[5] = np.rad2deg(true2mean(np.deg2rad(state[5]), state[1]))
file = open("test.in", "w+")
for dat in state[:3]:
    file.write(" {: 2.15f}".format(dat))
file.write("\n")
for dat in state[3:]:
    file.write(" {: 2.15f}".format(dat))
file.write("\n")
file.write("  0.d0 0.d0 0.d0\n")
