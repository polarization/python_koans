#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from runner.koan import *


class AboutNumbers(Koan):

    def test_basic_calculations(self):
        self.assertEqual(__, 13 / 2)
        self.assertEqual(__, 13.0 / 2)
        self.assertEqual(__, 13 // 2)
        self.assertEqual(__, 2 ** 10)
        self.assertEqual(__, 10 % 3)
        self.assertEqual(__, abs(-10))
        self.assertEqual(__, round(2.4))
        self.assertEqual(__, round(2.6))
        self.assertEqual(__, sum([1, 2, 3, 4, 5]))
        self.assertEqual(__, max([1, 2, 3, 4, 5]))
        self.assertEqual(__, min([1, 2, 3, 4, 5]))

    def test_math_operations(self):
        self.assertEqual(__, math.sqrt(81))
        self.assertEqual(__, math.sin(math.pi / 2))
        self.assertEqual(__, math.factorial(5))
        self.assertEqual(__, math.log(100, 10))
