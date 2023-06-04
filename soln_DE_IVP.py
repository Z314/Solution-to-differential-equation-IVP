import numpy as np
import math as mth
from matplotlib import pyplot as plt

# solution to differential equation IVP: 2*y'+y=3 ; I.C. y(0)=2


plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True


def y(x):
    """Calculates the value of y.

    Arguments:
    x -- sequence of x values. 
    """
    return 3 - np.exp(-0.5 * x)


x = np.linspace(0, 10, 100)

plt.title("Solution to DE IVP")
plt.xlabel("x")
plt.ylabel("y")

plt.plot(x, y(x), color='red')

plt.show()
