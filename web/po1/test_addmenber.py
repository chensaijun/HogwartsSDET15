#! /usr/bin/python 3
# -*- coding:UTF8 -*-
from web.po1.index_page import IndexPage


class TestAddMenber:
    def setup(self):
        self.index = IndexPage()

    def test_addmenber(self):
        assert self.index.goto_Importmenber().Importmenber()
