import math
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.multiclass import OneVsRestClassifier

def main():
    n, m = map(int, input().split())
    X = np.zeros(shape=(n, m))
    y = np.zeros(shape=(n,))
    for i in range(n):
        read_input = input().split()
        X[i] = np.array(list(map(float, read_input[:-1])))
        y[i] = int(read_input[-1])

    model = RidgeClassifier(alpha=0.0, fit_intercept=False)
    model.fit(X, y)

    calibr_obj = X[0, :]
    calibr_class = y[0]
    sign = lambda x: -1 if x < 0 else 1
    coefs = model.coef_[0]
    if sign((calibr_obj * coefs).sum()) != calibr_class:
        coefs = - coefs
    print(" ".join([str(coef) for coef in coefs]))


if __name__ == "__main__":
    main()
