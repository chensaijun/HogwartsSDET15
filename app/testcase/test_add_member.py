#! /usr/bin/python 3
# -*- coding:UTF8 -*-
from app.page.app import App


class TestAddMember:
     def setup(self):
         self.app = App()
         self.main = self.app.start().goto_mainpage()

     def test_add_member(self):
         username = "test3"
         phonenum = "15400000003"
         result = self.main.goto_address().member_invite_menu_page().add_member_page1(username,phonenum).get_toast()
         assert "添加成功" == result
