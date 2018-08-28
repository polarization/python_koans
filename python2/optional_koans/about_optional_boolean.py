#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutOptionalBoolean(Koan):

    def test_boolean(self):
        self.assertEqual(__, True.__class__)
        self.assertEqual(__, isinstance(True, bool))
        self.assertEqual(__, isinstance(True, int))
        self.assertEqual(__, True == 1)
        self.assertEqual(__, True is 1)
        self.assertEqual(__, True or False)
        self.assertEqual(__, True + 2)
