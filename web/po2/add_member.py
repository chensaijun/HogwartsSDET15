#! /usr/bin/python 3
# -*- coding:UTF8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from web.po2.base import Base


class AddMemberPage(Base):
    # def __init__(self,driver:WebDriver):
    #     self.driver = driver

    def add_mamber(self, username, memberAdd_acctid, memberAdd_phone):

        self.find(By.ID, "username").send_keys(username)
        self.find(By.ID, "memberAdd_acctid").send_keys(memberAdd_acctid)
        self.find(By.ID, "memberAdd_phone").send_keys(memberAdd_phone)
        self.find(By.CSS_SELECTOR, ".js_member_editor_form>div:nth-child(1) .js_btn_save").click()
        checkbox = (By.CSS_SELECTOR,".ww_checkbox")
        self.wait_for_click(checkbox)

        return True

    def get_member(self, value):
        # 验证联系人添加是否成功

        total_list = []
        while True:
            contactlist = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            titlelist = [element.get_attribute("title") for element in contactlist]
            # print(titlelist)
            if value in titlelist:
                return True
            total_list = total_list + titlelist


            result: str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
            num, total = result.split('/', 1)

            if int(num) == int(total):
                return False
            else:
                self.find(By.CSS_SELECTOR, ".ww_commonImg_PageNavArrowRightNormal").click()