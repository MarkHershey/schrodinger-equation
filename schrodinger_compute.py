from schrodinger import hydrogen_wave_func
from mayavi import mlab
import numpy as np
import timeit

quantum_numbers = [
    [1, 0, 0],
    [2, 0, 0],
    [2, 1, 1],
    [2, 1, 0],
    [2, 1, -1],
    [3, 0, 0],
    [3, 1, 1],
    [3, 1, 0],
    [3, 1, -1],
    [3, 2, 2],
    [3, 2, 1],
    [3, 2, 0],
    [3, 2, -1],
    [3, 2, -2],
    [4, 0, 0],
    [4, 1, 1],
    [4, 1, 0],
    [4, 1, -1],
    [4, 2, 2],
    [4, 2, 1],
    [4, 2, 0],
    [4, 2, -1],
    [4, 2, -2],
    [4, 3, 3],
    [4, 3, 2],
    [4, 3, 1],
    [4, 3, 0],
    [4, 3, -1],
    [4, 3, -2],
    [4, 3, -3],
]

for index, i in enumerate(quantum_numbers):
    print()
    print(f"calculating for quantum number: n={i[0]}, l={i[1]}, m={i[2]}")
    # time runtime
    start = timeit.default_timer()

    x, y, z, mag = hydrogen_wave_func(i[0], i[1], i[2], 40, 100, 100, 100)

    # dump data
    x.dump(f"result/x_{index}.dat")
    y.dump(f"result/y_{index}.dat")
    z.dump(f"result/z_{index}.dat")
    mag.dump(f"result/den_{index}.dat")

    # show runtime
    end = timeit.default_timer()
    timetaken = end - start
    if timetaken >= 120:
        mins = int(timetaken // 60)
        secs = timetaken - 60 * mins
        print("---complete. Time taken: {0} mins {1:.2f} secs".format(mins, secs))
    else:
        print("---complete. Time taken: {:.2f} seconds".format(timetaken))

    # print("x, y, z:")
    # print(x, y, z)
    # print("mag:")
    # print(mag)
