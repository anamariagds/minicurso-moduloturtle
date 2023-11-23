import turtle as t
from random import random

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        t.color(c)
        t.forward(steps)
        t.right(30)