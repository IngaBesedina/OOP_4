#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from task1 import addition


def test_addition_with_nums():
    assert addition("1", "2") == 3
    assert addition("1.5", "2.5") == 4.0


def test_addition_with_str():
    assert addition("Hello", "World") == "HelloWorld"
    assert addition("123", "qwe") == "123qwe"
    assert addition("asd", "345") == "asd345"
