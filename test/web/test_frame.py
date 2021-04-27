#! /usr/bin/python 3
# -*- coding:UTF8 -*-
from practice.web.base import Base

# 未嵌套frame
class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # 切换frame
        self.driver.switch_to.frame("iframeResult")
        print(self.driver.find_element_by_id("draggable").text)
        # 切换到父级frame
        self.driver.switch_to.parent_frame()
        print(self.driver.find_element_by_id("submitBTN").text)
