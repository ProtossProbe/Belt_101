# -*- coding: UTF-8 -*-
import numpy as np
from random import *
from elements import *

n = 10
m = 10
num = n*m

# a_arr = np.linspace(1.08, 1.28, n)
# e_arr = np.linspace(0, 0.1, m)
# I = 1

file = open("yh_tp.in", "w+")
file.write(str(num)+"\n")
for i in range(n):
    for j in range(m):
        a = np.random.uniform(1.04, 1.3)
        e = np.random.uniform(0, 0.04)
        I = np.random.uniform(0, 1)
        ome = np.random.uniform(0, 360)
        Ome = np.random.uniform(0, 360)
        f = np.random.uniform(0, 360)
        ele = [a, e, I, ome, Ome, f]
        print(ele)
        state = e2c(ele)

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
