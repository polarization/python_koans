#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys

from . import path_to_enlightenment
from .sensei import Sensei
from .writeln_decorator import WritelnDecorator

class Mountain:
    def __init__(self):
        self.stream = WritelnDecorator(sys.stdout)
        self.tests = path_to_enlightenment.koans()
        self.lesson = Sensei(self.stream)
        self.optional_tests = path_to_enlightenment.koans("optional_koans.txt")

    def walk_the_path(self, args=None):
        "Run the koans tests with a custom runner output."

        if args and len(args) >=2:
            self.tests = unittest.TestLoader().loadTestsFromName("koans." + args[1])

        self.tests(self.lesson)
        self.lesson.learn()
        return self.lesson

    def walk_the_optional_path(self, args=None):
        """Run the optional koans tests with a custom runner output."""

        if args and len(args) >= 2:
            args.pop(0)
            test_names = ["optional_koans." + test_name for test_name in args]
            self.optional_tests = unittest.TestLoader().loadTestsFromNames(
                test_names)
        self.lesson.run_optional = True
        self.optional_tests(self.lesson)
        self.lesson.learn_optional()
        return self.lesson
