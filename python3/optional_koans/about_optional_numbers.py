#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *
from fractions import *


class AboutOptionalNumbers(Koan):

    def test_complex_number(self):
        self.assertEqual(__, (1 + 2j) + (3 + 4j))

    def test_numeration_system(self):
        self.assertEqual((__, __, __), (bin(64), oct(64), hex(64)))
        self.assertEqual((__, __, __), (0b1000000, 0o100, 0xff))

    def test_bitwise_operation(self):
        x = 1
        self.assertEqual(__, (x << 2))
        self.assertEqual(__, x | 2)
        self.assertEqual(__, x & 1)
        self.assertEqual(__, x ^ 3)

    def test_fraction(self):
        self.assertEqual(__, Fraction(20, 60))
        self.assertEqual(__, Fraction(1, 3) + Fraction(1, 2))
        self.assertEqual(__, Fraction(1.25) + Fraction(0.5))
        self.assertEqual(__, 2.5.as_integer_ratio())
        self.assertEqual(__, Fraction(2.5.as_integer_ratio()))
