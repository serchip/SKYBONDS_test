"""
Долевое строительство
1. вычислительная сложность алгоритма: O(n)

по памяти норм

Filename: task1.py

Line #    Mem usage    Increment   Line Contents
================================================
    49   11.703 MiB   11.703 MiB   @profile
    50                             def main():
    51   11.707 MiB    0.004 MiB       with open('input1.csv', newline='') as f:
    52   11.707 MiB    0.000 MiB           reader = csv.reader(f)
    53   11.711 MiB    0.004 MiB           data = [float(r[0]) for r in reader]
    54
    55   11.711 MiB    0.000 MiB       sum_of_shares = sum(data[1:])
    56                             # output
    57   11.723 MiB    0.000 MiB       for i in data[1:]:
    58   11.723 MiB    0.012 MiB           print("%.3f" % round(i/sum_of_shares, 3))

2. ограничения на размер входных параметров: входящий массив должен вместиться в ОЗУ, или надо переписать решение для работы с батчами
3. оценка сложности задачи: 1, по времени 15 мин
"""

import csv


#@profile
def main():
    with open('input1.csv', newline='') as f:
        reader = csv.reader(f)
        data = [float(r[0]) for r in reader]

    sum_of_shares = sum(data[1:])
    print('sum_of_shares=', sum_of_shares)
# output
    for i in data[1:]:
        print("%.3f" % round(i/sum_of_shares, 3))


if __name__ == "__main__":
    main()


