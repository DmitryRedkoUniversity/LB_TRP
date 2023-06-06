import matplotlib.pyplot as plt
import numpy as np
from math import *
import random

fig, ax = plt.subplots()
line, = ax.plot([])

def f():
    N = 4002
    W = [[-1, 1][random.randrange(2)] for i in range(N)]
    Res = [sum(W[:i])/sqrt(N) for i in range(1, len(W))]

    return Res

X = [i/4000 for i in range(4001)]
W = f()

for i in range(len(W)):
    line.set_data(range(i+1), W[:i+1])
    ax.set_xlim(0, len(W))
    ax.set_ylim(min(W), max(W))
    line.set_linewidth(0.5)
    line.set_color("Red")
    plt.draw()
    plt.pause(1000**(-100))


