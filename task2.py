"""
Мегатрейдер
1. вычислительная сложность алгоритма: O(n)

по памяти норм

Filename: task2.py

Line #    Mem usage    Increment   Line Contents
================================================
    19   11.707 MiB   11.707 MiB   @profile
    20                             def main():
    21   11.711 MiB    0.004 MiB       with open('input.csv', newline='') as f:
    22   11.711 MiB    0.000 MiB           reader = csv.reader(f, delimiter=' ')
    23   11.715 MiB    0.004 MiB           data = list(reader)
    24
    25   11.715 MiB    0.000 MiB       profits = {}
    26   11.715 MiB    0.000 MiB       n, m, s = data[0]
    27   11.719 MiB    0.004 MiB       balance = float(s)
    28   11.719 MiB    0.000 MiB       sum_profit = 0
    29   11.719 MiB    0.000 MiB       operations = {}
    30
    31                             # вычислили профит по всем лотам
    32   11.719 MiB    0.000 MiB       for row in data[1:]:
    33   11.719 MiB    0.000 MiB           profits[" ".join(row)] = (CALC * int(row[3])) - ((float(row[2]) * 10) * int(row[3]) - REPAYMENT * int(row[3]))
    34
    35                             # набираем самые профитные
    36   11.719 MiB    0.000 MiB       for k, v in sorted(profits.items(), key=lambda x: x[1], reverse=True):
    37   11.719 MiB    0.000 MiB           row = k.split(" ")
    38   11.719 MiB    0.000 MiB           cost = (float(row[2]) * 10) * int(row[3])
    39   11.719 MiB    0.000 MiB           if cost < balance:
    40   11.719 MiB    0.000 MiB               sum_profit += v
    41   11.719 MiB    0.000 MiB               balance -= cost
    42   11.719 MiB    0.000 MiB               operations[k] = row[0]
    43
    44                             # output
    45   11.730 MiB    0.012 MiB       print(sum_profit)
    46   11.730 MiB    0.000 MiB       for k, v in sorted(operations.items(), key=lambda x: x[1]):
    47   11.730 MiB    0.000 MiB           print(k)
    48   11.730 MiB    0.000 MiB       print('')

2. ограничения на размер входных параметров: входящий массив должен вместиться в ОЗУ, или надо переписать решение для работы с батчами
3. оценка сложности задачи: 3, по времени 1 час
"""

import csv

CALC = 30   # n+30
REPAYMENT = 1000


#@profile
def main():
    with open('input2.csv', newline='') as f:
        reader = csv.reader(f, delimiter=' ')
        data = list(reader)

    profits = {}
    n, m, s = data[0]
    balance = float(s)
    sum_profit = 0
    operations = {}

# вычислили профит по всем лотам
    for row in data[1:]:
        profits[" ".join(row)] = (CALC * int(row[3])) - ((float(row[2]) * 10) * int(row[3]) - REPAYMENT * int(row[3]))

# набираем самые профитные
    for k, v in sorted(profits.items(), key=lambda x: x[1], reverse=True):
        row = k.split(" ")
        cost = (float(row[2]) * 10) * int(row[3])
        if cost < balance:
            sum_profit += v
            balance -= cost
            operations[k] = row[0]

# output
    print(sum_profit)
    for k, v in sorted(operations.items(), key=lambda x: x[1]):
        print(k)
    print('')


if __name__ == "__main__":
    main()


