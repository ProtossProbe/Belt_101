# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.colors as colors


# Constants for plotting
DEFAULT_CMAP = "RdYlBu"
CMAP_START = 0.2
CMAP_END = 1.0
CMAP_BIT = 100
DEFAULT_MARKER_SIZE = 1
DEFAULT_LINE_WIDTH = 1.5
DEFAULT_ALPHA = 1


# ------------------------------
# Semi-major Axes of Nine Planets (PLUTO IS A PLANET!)
# Ratio to Earth Values (or in AU)
A_MERCURY = 0.387
A_VENUS = 0.723
A_EARTH = 1
A_MARS = 1.52
A_JUPITER = 5.20
A_SATURN = 9.58
A_URANUS = 19.20
A_NEPTUNE = 30.05
A_PLUTO = 39.48
A_PLANETS = [A_MERCURY, A_VENUS, A_EARTH, A_MARS,
             A_JUPITER, A_SATURN, A_URANUS, A_NEPTUNE, A_PLUTO]

# Mass of Nine Planets
# Ratio to Earth Values
M_MERCURY = 0.0553
M_VENUS = 0.815
M_EARTH = 1
M_MARS = 0.107
M_JUPITER = 317.8
M_SATURN = 95.2
M_URANUS = 14.5
M_NEPTUNE = 17.1
M_PLUTO = 0.0025
M_PLANETS = [M_MERCURY, M_VENUS, M_EARTH, M_MARS,
             M_JUPITER, M_SATURN, M_URANUS, M_NEPTUNE, M_PLUTO]

# Diameters of Nine Planets
# Ratio to Earth Values
D_MERCURY = 0.383
D_VENUS = 0.949
D_EARTH = 1
D_MARS = 0.532
D_JUPITER = 11.21
D_SATURN = 9.45
D_URANUS = 4.01
D_NEPTUNE = 3.88
D_PLUTO = 0.186
D_PLANETS = [D_MERCURY, D_VENUS, D_EARTH, D_MARS,
             D_JUPITER, D_SATURN, D_URANUS, D_NEPTUNE, D_PLUTO]

# Diameters of Hill Sphere of Nine Planets
# in AU
H_MERCURY = 0.0011718
H_VENUS = 0.006713
H_EARTH = 0.009837
H_MARS = 0.00657
H_JUPITER = 0.33805
H_SATURN = 0.412
H_URANUS = 0.44645
H_NEPTUNE = 0.7691
H_PLUTO = 0.03854
H_PLANETS = [H_MERCURY, H_VENUS, H_EARTH, H_MARS,
             H_JUPITER, H_SATURN, H_URANUS, H_NEPTUNE, H_PLUTO]

# ------------------------------
mpl.rcParams['lines.markersize'] = DEFAULT_MARKER_SIZE
mpl.rcParams['lines.linewidth'] = DEFAULT_LINE_WIDTH


def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap


def wrapTo360(phi):
    return phi % 360


def resonanceLocation(planet, p, q):
    try:
        a = A_PLANETS[planet]
        return (q/p) ** (2/3) * a
    except IndexError:
        print("ERROR!! Planet index number must be in the range of (0,8)")


def scatterPlot(ax, x, y, xlable, ylabel, title, xlim, ylim):
    sp = ax.scatter(x, y)
    setBasicLabels(ax, xlable, ylabel, title, xlim, ylim)
    return sp


def scatterPlotWithSize(ax, x, y, sz, xlable, ylabel, title, xlim, ylim):
    sp = ax.scatter(x, y, s=sz)
    setBasicLabels(ax, xlable, ylabel, title, xlim, ylim)
    return sp


def scatterColorPlot(ax, x, y, c, xlable, ylabel, title, xlim, ylim):
    scp = ax.scatter(x, y, c=c, cmap=DEFAULT_CMAP,
                     norm=mpl.colors.LogNorm(vmin=1e6, vmax=1e9))
    setBasicLabels(ax, xlable, ylabel, title, xlim, ylim)
    return scp


def setBasicLabels(ax, xlable, ylabel, title, xlim, ylim):
    ax.set_xlabel(xlable)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xlim(xlim[0], xlim[1])
    ax.set_ylim(ylim[0], ylim[1])


def resonancePlot(ax, a_res, ylim, color):
    rp = ax.plot((a_res, a_res), ylim, color=color)
    return rp


def stdFourScatterPlot(axes, alltp, alim, elim, Ilim):
    a, e, I, ome, Ome = alltp[:, 0], alltp[:,
                                           1], alltp[:, 2], alltp[:, 3], alltp[:, 4]

    scatterPlot(axes[0, 0], a, e, 'a', 'e', 'a-e', alim, elim)
    scatterPlot(axes[0, 1], a, I, 'a', 'I', 'a-I', alim, Ilim)
    scatterPlot(axes[1, 0], e, ome, 'e', 'omega',
                'e-omega', elim, (0, 360))
    scatterPlot(axes[1, 1], I, Ome, 'I', 'Omega',
                'I-Omega', Ilim, (0, 360))


def NEOSSatModelAEPlot(ax, grid, alim, elim):
    a_step, e_step, I_step = 0.05, 0.02, 2

    a_count = int((alim[1] - alim[0]) / a_step) + 1
    a_start = int((alim[0]-0.025)/a_step) + 1
    a_range = np.linspace(alim[0], alim[1], a_count)
    a_left = alim[0]-a_step/2
    a_right = alim[1]+a_step/2

    e_count = int((elim[1] - elim[0]) / e_step) + 1
    e_start = int((elim[0]-0.01)/e_step)
    e_range = np.linspace(elim[0], elim[1], e_count)
    e_left = elim[0]-e_step/2
    e_right = elim[1]+e_step/2

    new_cmap = truncate_colormap(plt.get_cmap(
        DEFAULT_CMAP), CMAP_START, CMAP_END,  CMAP_BIT)
    heatmap = ax.imshow(grid, extent=[
                        a_left, a_right, e_left, e_right], cmap=new_cmap)
    cbar = ax.figure.colorbar(heatmap, ax=ax)

    ax.set_xlabel("a")
    ax.set_ylabel("e")
    return heatmap


def NEOSSatModelAIPlot(ax, grid, alim, Ilim):
    a_step, e_step, I_step = 0.05, 0.02, 2

    a_count = int((alim[1] - alim[0]) / a_step) + 1
    a_start = int((alim[0]-0.025)/a_step) + 1
    a_range = np.linspace(alim[0], alim[1], a_count)
    a_left = alim[0]-a_step/2
    a_right = alim[1]+a_step/2

    I_count = int((Ilim[1] - Ilim[0]) / I_step) + 1
    I_start = int((Ilim[0]-0.01)/I_step)
    I_range = np.linspace(Ilim[0], Ilim[1], I_count)
    I_left = Ilim[0]-I_step/2
    I_right = Ilim[1]+I_step/2

    new_cmap = truncate_colormap(plt.get_cmap(
        DEFAULT_CMAP), CMAP_START, CMAP_END, CMAP_BIT)
    heatmap = ax.imshow(grid, extent=[
                        a_left, a_right, I_left, I_right], cmap=new_cmap)
    cbar = ax.figure.colorbar(heatmap, ax=ax)

    ax.set_xlabel("a")
    ax.set_ylabel("I")
    return heatmap
