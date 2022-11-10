#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


# This has to be an even number to work!
N_PERSON = 8
N_ITERATIONS = 50
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
    
    print(results)

    fig, (ax1, ax2) = plt.subplots(2, figsize=(12,12))

    for i, r in enumerate(np.array(results).T):
        ax1.plot(r, label="Result {}".format(i))
    ax1.legend()

    ax2.bar(range(N_PERSON), results[-1])
    plt.show()
