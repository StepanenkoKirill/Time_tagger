import time
import matplotlib.pyplot as plt


def plotter(args, func, x_lbl, y_lbl):
    plt.plot(args, func, 'black', linewidth=0.5)
    plt.xlabel(x_lbl)
    plt.ylabel(y_lbl)
    plt.grid(True)
    plt.savefig("Resonator_scanning" + str(round(time.time())) + ".png")
    plt.close()


# plotter([1, 2, 3], [3, 2, 1], "X", "Y")

a = 4
b = 5
mod = 0
if a > b:
    mod = 22
else:
    mod = 33
print(mod)
