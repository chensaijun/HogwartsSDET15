#! /usr/bin/python 3
# -*- coding:UTF8 -*-
from homework.po2.base import Base
from homework.po2.main_page import MainPage


class TestAddMember:
    def setup(self):
        self.main = MainPage()

    def test_addmenber(self):
        username = "aa19"
        memberAdd_acctid = "aaaaa19"
        memberAdd_phone = "15100000032"
        # assert self.main.goto_addmenber().add_manber(username,memberAdd_acctid,memberAdd_phone)
        addmenber = self.main.goto_addmember()
        addmenber.add_mamber(username,memberAdd_acctid,memberAdd_phone)
        assert username in addmenber.get_member(username)

    def test_addmember1(self):
        username = "bbb121"
        memberAdd_acctid = "bbbabb21"
        memberAdd_phone = "15200000010"
        addmenber1 = self.main.goto_addmember1()
        addmenber1.add_mamber(username, memberAdd_acctid, memberAdd_phone)
        assert addmenber1.get_member(username)
