import matplotlib.pyplot as plt
import numpy as np
import sklearn.model_selection
import sklearn.linear_model
import sklearn.metrics

FILE = "data.csv"
random_state = 42

def main() -> None:
    data: np.ndarray = np.loadtxt(FILE, delimiter=",", dtype="float64")
    X, y = np.split(ary=data, indices_or_sections=2, axis=1)

    X = np.apply_along_axis(
        arr=X[:, 0],
        func1d=lambda x: np.array([np.sin(x)**2, np.sin(x) * np.log(x), np.log(x)**2, x**2]).T,
        axis=0,
    )

    model = sklearn.linear_model.LinearRegression()
    model.fit(X, y)

    coefs = model.coef_[0, :]
    print("a: {a} \nb: {b} \nc: {c}".format(a=np.sqrt(coefs[0]), b=np.sqrt(coefs[2]), c=coefs[3]))

if __name__ == "__main__":
    main()