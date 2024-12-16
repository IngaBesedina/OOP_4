#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Напишите программу, которая запрашивает ввод двух значений.
Если хотя бы одно из них не является числом, 
то должна выполняться конкатенация, т. е. соединение, строк. 
В остальных случаях введенные числа суммируются.
"""


def addition(v1, v2):
    try:
        num1 = float(v1)
        num2 = float(v2)

        result = num1 + num2
        return result
    except ValueError:
        result = v1 + v2
        return result


def main():
    value1 = input("Первое значение: ")
    value2 = input("Второе значение: ")

    addition(value1, value2)


if __name__ == "__main__":
    main()
