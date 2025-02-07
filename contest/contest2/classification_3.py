import pandas as pd
import numpy as np

def main():
    coef_ = np.array([])
    intercept_ = -0.78940101
    lines = None
    with open("./restaurants.in", "r") as file:
        lines = file.readlines()
    verdicts = []
    for line in lines[1:]:
        fields = line.split()
        di = float(fields[1])
        if fields[0] == "-1":
            ri = 10 * (1 - di)
        else:
            ri = float(fields[0])
        res = np.dot(np.array([ri, 5.0, di, 0.5]), coef_) + intercept_

        verdicts.append((ri, di, res))
        print(res)

if __name__ == "__main__":
    main()
