#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    try:
        value1 = input("Первое значение: ")
        value2 = input("Второе значение: ")

        num1 = float(value1)
        num2 = float(value2)

        result = num1 + num2
        print(f"Результат: {result}")

    except ValueError:
        result = value1 + value2
        print(f"Результат: {result}")


if __name__ == "__main__":
    main()
