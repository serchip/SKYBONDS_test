"""
Долевое строительство
1. вычислительную сложность алгоритма: O(2*n)

по памяти норм

Filename: task1.1.py

Line #    Mem usage    Increment   Line Contents
================================================
    29   11.652 MiB   11.652 MiB   @profile
    30                             def chunks(iter, n):
    31   11.652 MiB    0.000 MiB       try:
    32   11.652 MiB    0.000 MiB           while True:
    33   11.664 MiB    0.000 MiB               i = 0
    34   11.664 MiB    0.000 MiB               res = []
    35   11.664 MiB    0.000 MiB               while i < n:
    36   11.664 MiB    0.004 MiB                   res.append(float(next(iter)[0]))
    37   11.664 MiB    0.000 MiB                   i += 1
    38   11.664 MiB   11.664 MiB               yield res
    39   11.664 MiB    0.000 MiB       except StopIteration:
    40   11.664 MiB   11.664 MiB           yield res


Line #    Mem usage    Increment   Line Contents
================================================
    42   11.652 MiB   11.652 MiB   @profile
    43                             def read_batch(ch_size):
    44   11.652 MiB    0.000 MiB       with open('input1.csv', newline='') as f:
    45   11.652 MiB    0.000 MiB           reader = csv.reader(f)
    46   11.652 MiB    0.000 MiB           the_first = True
    47   11.664 MiB   11.664 MiB           for batch in chunks(reader, ch_size):
    48   11.664 MiB    0.000 MiB               if the_first:
    49   11.652 MiB    0.000 MiB                   the_first = False
    50   11.652 MiB    0.000 MiB                   batch = batch[1:]
    51   11.664 MiB   11.664 MiB               yield batch


Line #    Mem usage    Increment   Line Contents
================================================
    54   11.645 MiB   11.645 MiB   @profile
    55                             def main():
    56   11.648 MiB    0.004 MiB       sum_of_shares = 0
    57   11.652 MiB   11.652 MiB       for b_data in read_batch(CHUNK_SIZE):
    58   11.652 MiB    0.000 MiB           sum_of_shares += sum(b_data)
    59                             # output
    60   11.664 MiB   11.664 MiB       for b_data in read_batch(CHUNK_SIZE):
    61   11.664 MiB    0.000 MiB           for i in b_data:
    62   11.664 MiB    0.012 MiB               print("%.3f" % round(i/sum_of_shares, 3))

2. ограничений на размер входных данных нет
3. оценка сложности задачи: 2, по времени 30 мин
"""

import csv
CHUNK_SIZE = 4

#@profile
def chunks(iter, n):
    try:
        while True:
            i = 0
            res = []
            while i < n:
                res.append(float(next(iter)[0]))
                i += 1
            yield res
    except StopIteration:
        yield res

#@profile
def read_batch(ch_size):
    with open('input1.csv', newline='') as f:
        reader = csv.reader(f)
        the_first = True
        for batch in chunks(reader, ch_size):
            if the_first:
                the_first = False
                batch = batch[1:]
            yield batch


#@profile
def main():
    sum_of_shares = 0
    for b_data in read_batch(CHUNK_SIZE):
        sum_of_shares += sum(b_data)
# output
    for b_data in read_batch(CHUNK_SIZE):
        for i in b_data:
            print("%.3f" % round(i/sum_of_shares, 3))


if __name__ == "__main__":
    main()


