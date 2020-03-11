# from schrodinger import hydrogen_wave_func
from mayavi import mlab
import numpy as np

# Mayavi code:
for index in range(30):
    # load data
    x = np.load(f"result/x_{index}.dat", allow_pickle=True)
    y = np.load(f"result/y_{index}.dat", allow_pickle=True)
    z = np.load(f"result/z_{index}.dat", allow_pickle=True)
    density = np.load(f"result/den_{index}.dat", allow_pickle=True)

    # plot
    figure = mlab.figure('DensityPlot', size=(830, 830))
    pts = mlab.contour3d(density, contours=40, opacity=0.4)
    mlab.axes()

    # show figure
    # mlab.show()

    # save figure
    mlab.savefig(f"figs/3dView/3d_{index}.png")
    mlab.close()
    print(index)
