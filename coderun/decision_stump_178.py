import sys
import typing

def main():
    """
    Для чтения входных данных необходимо получить их
    из стандартного потока ввода (sys.stdin).
    Данные во входном потоке соответствуют описанному
    в условии формату. Обычно входные данные состоят
    из нескольких строк.
    Можно использовать несколько методов:
    * input() -- читает одну строку из потока без символа
    перевода строки;
    * sys.stdin.readline() -- читает одну строку из потока,
    сохраняя символ перевода строки в конце;
    * sys.stdin.readlines() -- вернет список (list) строк,
    сохраняя символ перевода строки в конце каждой из них.
    Чтобы прочитать из строки стандартного потока:
    * число -- int(input()) # в строке должно быть одно число
    * строку -- input()
    * массив чисел -- map(int, input().split())
    * последовательность слов -- input().split()
    Чтобы вывести результат в стандартный поток вывода (sys.stdout),
    можно использовать функцию print() или sys.stdout.write().
    Возможное решение задачи "Вычислите сумму чисел в строке":
    print(sum(map(int, input().split())))
    """
    def get_impurity(arr: typing.List[int]) -> float:
        mean_ = sum(arr) / len(arr)
        return sum([(x - mean_)**2 for x in arr]) / len(arr)

    N = int(input())
    if N == 1:
        x, y = map(int, input().split())
        print(f"{y} {y} {x}")
        return

    x = [0] * N
    y = [0] * N

    for i in range(N):
        x[i], y[i] = map(int, input().split())

    x, y = zip(*sorted(zip(x, y), key=lambda pair: pair[0]))
    impurities = [0] * (N - 1)

    for i in range(N -  1):
        ly = y[:i + 1] #
        ry = y[i + 1:] #
        impurities[i] = get_impurity(ly) + get_impurity(ry)

    print(impurities)

    min_impurity_i = min(range(N - 1), key=lambda i: impurities[i])
    min_impurity_pivot = (x[min_impurity_i] + x[min_impurity_i + 1]) / 2
    ly = y[:min_impurity_i + 1]
    ry = y[min_impurity_i + 1:]

    a = sum(ly) / len(ly)
    b = sum(ry) / len(ry)
    c = min_impurity_pivot

    print("%.10f %.10f %.10f" % (a, b, c))


if __name__ == '__main__':
    main()