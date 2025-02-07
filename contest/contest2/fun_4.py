import numpy as np
from scipy.optimize import curve_fit

def main():
    X = []
    Y = []
    with open("data.csv", "r") as file:
        for line in file:
            x, y = line.split(",")
            X.append(float(x))
            Y.append(float(y))

    #definition of the function
    def myfunc(x, a, b, c):
        return a + b * np.cos(x - c)

    fun = lambda x, a, b, c: (a * np.sin(x) + b * np.log(x))**2 + c * x**2
    X_data = np.array(X)
    Y_data = np.array(Y)
    popt, _pcov = curve_fit(fun, X_data, Y_data)
    print(popt, _pcov)

if __name__ == "__main__":
    main()
