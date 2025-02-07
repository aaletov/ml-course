import sys
import math


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
    N = int(input()) + 1

    dists = [0] * N
    heights = [0] * N
    for i in range(1, N):
        dists[i], heights[i] = map(int, input().split())

    def get_distance(l_idx, r_idx):
        return math.sqrt((heights[l_idx] - heights[r_idx])**2 + (dists[l_idx] - dists[r_idx])**2)

    length = 0.0
    l_idx, r_idx = 0, 1
    find_nodesc = False
    while (l_idx != (N - 1)):
        if find_nodesc:
            if r_idx >= (N - 1):
                find_nodesc = False
                l_idx += 1
                r_idx = l_idx + 1
            elif heights[l_idx] <= heights[r_idx]:
                length += get_distance(l_idx, r_idx)
                find_nodesc = False
                l_idx += 1
                r_idx = l_idx + 1
            else:
                r_idx += 1

            continue

        length += get_distance(l_idx, r_idx)
        if heights[l_idx] <= heights[r_idx]:
            l_idx += 1
            r_idx += 1
        else:
            find_nodesc = True
            r_idx += 1

    print(length)

if __name__ == '__main__':
    main()