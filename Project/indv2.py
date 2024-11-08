#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import random


class RandomMatrix:

    def __init__(self, rows, cols, low, high):
        self.rows = rows
        self.cols = cols
        self.low = low
        self.high = high
        self.matrix = self.generate_matrix()

    def generate_matrix(self):
        return [
            [random.randint(self.low, self.high) for _ in range(self.cols)]
            for _ in range(self.rows)
        ]


def get_user_input():
    while True:
        try:
            rows = int(input("Введите количество строк: "))
            cols = int(input("Введите количество столбцов: "))
            low = int(input("Введите минимальное значение: "))
            high = int(input("Введите максимальное значение: "))

            if rows <= 0 or cols <= 0:
                raise ValueError(
                    "Количество строк и столбцов должно быть положительным."
                )
            if low > high:
                raise ValueError(
                    "Минимальное значение не может быть больше максимального."
                )

            return rows, cols, low, high
        except ValueError as e:
            print(f"Ошибка ввода: {e}")


def main():
    rows, cols, min_val, max_val = get_user_input()
    new_matrix = RandomMatrix(rows, cols, min_val, max_val)

    for row in new_matrix.matrix:
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    main()
