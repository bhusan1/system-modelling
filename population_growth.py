# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from math import *
import matplotlib.pyplot as plt

init_pop = 8000
max_pop = 15000
rate_increase = 10 / 100
new_pop = [1] * 18
new_pop[0] = 8000
new_pop[1] = 8000 + 8000 * 10 / 100
count = 1

result = ["W", "W", "W", "W", "W", "W", "L", "W", "D", "D", "W", "L", "L", "W", "W", "L", "W", "W"]
for i in range(2, len(result)):
    if result[i - 1] == "W" and result[i - 2] == "W":
        new_pop[i] = new_pop[i - 1] + (rate_increase * (1 - (new_pop[i - 1] / max_pop)) * new_pop[i - 1])

    elif result[i - 1] == "L" and result[i - 2] == "L":
        new_pop[i] = new_pop[i - 1] * rate_increase ** count
        count += 1

    elif (result[i - 1] == "D" and result[i - 2] == "W") or (result[i - 1] == "W" and result[i - 2] == "D"):
        new_pop[i] = (new_pop[i - 1]) + (new_pop[i - 1] * rate_increase)

    else:
        new_pop[i] = (new_pop[i - 1]) - (new_pop[i - 1] * rate_increase)

print(new_pop)

plt.plot(new_pop)
plt.ylabel("Number of audience")
plt.xlabel("Game")
plt.show()

