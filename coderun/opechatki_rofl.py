import numpy as np

def to_vector(string: str) -> np.ndarray:
    # vec = np.zeros(shape=(len(string)))
    vec = np.zeros(shape=(4,))
    for i in range(len(string)):
        vec[i] = ord(string[i]) - ord("a") + 1
    return vec


if __name__ == "__main__":
    supposed = input()
    origin = input()
    N = int(input())

    supposed_vec = to_vector(supposed)
    origin_vec = to_vector(origin)
    replacements = np.zeros(shape=(N, len(origin)))

    for i in range(N):
        replacement, subs = input().split()
        replacements[i] = to_vector(replacement)

    w = np.ones(N)
    w_history_list = [w.copy()]
    lr = 1e-3
    num_steps = 10
    for i in range(num_steps):
        w -= lr * ((replacements @ replacements.T @ w) - (replacements @ supposed_vec) + 1.0 * 2 * w) / N
        w_history_list.append(w.copy())
    w_history_list = np.array(w_history_list)

    print(w)
    print(w_history_list)
