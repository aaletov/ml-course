import typing
import numpy as np

def find_nearest_user(luser: int, users_to_films: np.ndarray) -> np.ndarray:
    min_dist = 1e+10
    min_dist_idx = -1
    for i in range(users_to_films.shape[0]):
        dist = np.linalg.norm(users_to_films[luser] - users_to_films[i])
        if dist < min_dist:
            min_dist = dist
            min_dist_idx = i
    print(min_dist_idx)
    return users_to_films[min_dist_idx]

def find_nearest_film(lfilm: int, users_to_films: np.ndarray) -> int:
    min_dist = 1e+10
    min_dist_idx = -1
    for i in range(users_to_films.shape[1]):
        dist = np.linalg.norm(users_to_films[:, lfilm] - users_to_films[:, i])
        if dist < min_dist:
            min_dist = dist
            min_dist_idx = i
    return min_dist_idx

def read_() -> typing.Tuple[np.ndarray, typing.List[typing.Any]]:
    with open("kinopoisk_input.txt", "r") as file:
        n, m, q = map(int, file.readline().rstrip().split())
        queries = [0] * q
        users_to_films = np.zeros(shape=(n, m))

        for i in range(n):
            line = file.readline().rstrip()
            users_to_films[i] = np.array(list(map(int, line.split())))
        for i in range(q):
            line = file.readline().rstrip().split()
            queries[i] = line
        return (users_to_films, queries)

def main():
    users_to_films, queries = read_()

    with open("kinopoisk_output.txt", "w") as file:
        print(str(len(queries)), file=file)
        for query in queries:
            if query[0] == "u":
                sim_user = find_nearest_user(int(query[1]) - 1, users_to_films)
                print(sim_user.argmax() + 1, file=file)

            if query[0] == "v":
                print(find_nearest_film(int(query[1]) - 1, users_to_films) + 1, file=file)



if __name__ == "__main__":
    main()