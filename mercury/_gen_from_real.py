# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

folder = "mercury/"

name = folder+"em_region_orbit(<=5).csv"
data = np.genfromtxt(name, delimiter=',',
                     skip_header=1, usecols=(1, 2, 3, 4, 5, 6, 9))
a, e, I, ome, Ome, M, epoch = data[:, 0], data[:, 1], data[:, 2], \
    data[:, 4], data[:, 3], data[:, 5], data[:, 6]

num = a.shape[0]
print(num)

file = open(folder+"temp.txt", "w")
for i in np.arange(num):
    file.write(" {0:d}    ep={1:.1f}d0\n".format(i+101, epoch[i]))
    file.write(" {0:.16g}d0 {1:.16g}d0 {2:.16g}d0 \n {3:.16g}d0 {4:.16g}d0 {5:.16g}d0 \n 0.d0 0.d0 0.d0\n".format(
        a[i], e[i], I[i], ome[i], Ome[i], M[i]))
file.close()
