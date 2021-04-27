#! /usr/bin/python 3
# -*- coding:UTF8 -*-
from time import sleep

from practice.web.base import Base


class TestFile(Base):
    def test_file(self):
        self.driver.get("https://image.baidu.com")
        self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]").click()
        # 在文件夹中复制地址时，文件夹中的地址是用 \ 来分隔不同文件夹的，而Python识别地址时只能识别用 / 分隔的地址
        self.driver.find_element_by_id("stfile").send_keys(
            "c:/Users/1/PycharmProjects/practice_and_homework/practice/web/image/image.png")
        sleep(3)