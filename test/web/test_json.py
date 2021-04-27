#! /usr/bin/python 3
# -*- coding:UTF8 -*-
from time import sleep

from practice.web.base import Base


class TestJs(Base):
    def test_js(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        # execute_script执行js，return 返回js的返回结果
        ele = self.driver.execute_script("return document.getElementById('su')")
        ele.click()
        # 获取当前页面的滚动条纵坐标位置
        # 滚动到底部，点击下一页
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        self.driver.find_element_by_xpath("//*[@id='page']/div/a[10]").click()
        sleep(3)
        for code in[
            'return document.title','return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))


    # 修改时间控件：时间控件一般都是readonly
    # 取消日期的readonly属性
    # 给value赋值
    def test_js_time(self):
        self.driver.get("https://www.12306.cn/index/")
        self.driver.execute_script("document.getElementById('train_date')")
        print(self.driver.execute_script(
            "return a = document.getElementById('train_date') ,document.getElementById('train_date').removeAttribute('readonly'),a.value = '2020-12-03'"))
