#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import multiprocessing as mp
import itertools


# This has to be an even number to work!
N_PERSON = 30
N_ITERATIONS = 1000
MIN_CONCENTRATION_INITIAL = 1
MAX_CONCENTRATION_INITIAL = 5
PRODUCTION_RATE = 5
# Critical value for this parameter is < 1.0
DEGRADATION_RATE = 0.2


def add_inverse_neighbors(a):
    da = PRODUCTION_RATE/(np.roll(a, 1) + np.roll(a, -1))
    da += - DEGRADATION_RATE * a
    a += da
    return a


def plot_results_ind(res_i, max_value):
    i, res = res_i
    cmap = mpl.colormaps['viridis']

    colors = cmap(res/max_value)

    fig, ax = plt.subplots(figsize=(12,12))
    ax.bar(range(len(res)), res, color=colors)

    plt.savefig("out/chessboard_1d_{:010.0f}.png".format(i))
    plt.close(fig)


if __name__ == "__main__":
    
    a = np.array(
        np.random.randint(
            MIN_CONCENTRATION_INITIAL,
            MAX_CONCENTRATION_INITIAL+1,
            (N_PERSON)
        ),
        dtype=float
    )

    results = np.zeros((N_ITERATIONS+1, N_PERSON))
    results[0] = a

    for i in range(1, N_ITERATIONS+1):
        a = add_inverse_neighbors(a)
        results[i] = a

    fig, (ax1, ax2) = plt.subplots(2, figsize=(12,12))

    p = mp.Pool()

    p.starmap(
        plot_results_ind,
        zip(
            enumerate(np.array(results)),
            itertools.repeat(np.max(results)),
        )
    )
