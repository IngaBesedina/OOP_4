#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from task2 import RandomMatrix


def test_generate_matrix():
    matrix = RandomMatrix(3, 3, 1, 9)
    expected_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    assert matrix.matrix == expected_matrix
