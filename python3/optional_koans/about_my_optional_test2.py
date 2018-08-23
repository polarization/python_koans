#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutOptionalAsserts2(Koan):

    def test_my_assert_truth(self):
        self.assertTrue(False)  # This should be True

    def test_my_assert_truth2(self):
        self.assertTrue(False)  # This should be True
