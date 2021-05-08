#! /usr/bin/python 3
# -*- coding:UTF8 -*-
from frame.main import Main


class TestSearch:
    # def setup(self):
    #     self.main = Main()

    def test_search(self):
        # self.main.goto_market()
        Main().goto_market().goto_search().search()