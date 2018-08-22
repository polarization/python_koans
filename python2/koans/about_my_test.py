#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutMyAsserts(Koan):

    def test_my_assert_truth(self):
        self.assertTrue(False)  # This should be True
