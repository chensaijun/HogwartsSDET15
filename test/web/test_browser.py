#! /usr/bin/python 3
# -*- coding:UTF8 -*-
import shelve
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from practice.web.base import Base

"""
使用cookie 登录企业微信，完成导入联系人，加上断言验证
"""


class TestBrowser():
    def setup_method(self, method):
        """
        # 复用浏览器
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        :param method:
        :return:
        """

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()

    @pytest.mark.skip
    def test_baidu(self):
        self.driver.get("http://www.baidu.com")
        sleep(3)

    def test_weixin(self):
        # 获取cookies
        # print(self.driver.get_cookies())
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'lKID0iTX_shL1xS2MkirlnOydzYyDvS8NmSOJmCKweyv9cweCoI1XQUUzt734CGpotomXSX0q5VTxBedIl9VGLh73q-OrgHVX0GfV3254Et1zw1n9PJQJr_aPIT0FIGdMSPci89CYb03g0ZnzsqHw6VenoYw7ePN-TGFs7jBFWeswZj74Q5Kq0ZdJ7znRaC3ER2njBOxyah43qQv3009xbRWbkCCgd93BmwSurWX9Pm8iMwicb0Z5qNGsaP0TGcjWkccd7qn-wNbA-QTMPclWA'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1618394221, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '5s9aivn'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688851197686367'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325016163252'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '27269448902306689'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1649839107, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688851197686367'},
            {'domain': '.qq.com', 'httpOnly': False, 'name': 'qm_verifyimagesession', 'path': '/', 'secure': False,
             'value': 'h01b81681cf5e6fc07b110725b15498e13f5e7178ad7bf1caa086b48b029ea29e896d1f9e501eef0ab2'},
            {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': '981dc4cbf0dff97f1740d0b985b79f9895769dd36d07d8c72b528464bbba006e'},
            {'domain': '.qq.com', 'httpOnly': False, 'name': 'skey', 'path': '/', 'secure': False,
             'value': '@giNEcON5l'},
            {'domain': '.qq.com', 'httpOnly': False, 'name': 'qm_authimgs_id', 'path': '/', 'secure': False,
             'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1620954871, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_si', 'path': '/', 'secure': False,
             'value': 's8326784000'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '7959230390'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'iSM8bvjWDeaTXx5rb9eodbKy8vaomXbb4350nMONPJst6OO0aO-40kg7M_6l5RfE'},
            {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': False,
             'value': 'ssid=s6051332388'},
            {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'ZEqY8wx3Ww'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a1064943'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'uin', 'path': '/', 'secure': False,
                                    'value': 'o0985063495'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False,
             'value': ''},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '5505247232'}]
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        # 添加cookies
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

    def test_shelve(self):
        # cookie存储到shelve
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'lKID0iTX_shL1xS2MkirlnOydzYyDvS8NmSOJmCKweyv9cweCoI1XQUUzt734CGpotomXSX0q5VTxBedIl9VGLh73q-OrgHVX0GfV3254Et1zw1n9PJQJr_aPIT0FIGdMSPci89CYb03g0ZnzsqHw6VenoYw7ePN-TGFs7jBFWeswZj74Q5Kq0ZdJ7znRaC3ER2njBOxyah43qQv3009xbRWbkCCgd93BmwSurWX9Pm8iMwicb0Z5qNGsaP0TGcjWkccd7qn-wNbA-QTMPclWA'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1618394221, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '5s9aivn'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688851197686367'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325016163252'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '27269448902306689'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1649839107, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688851197686367'},
            {'domain': '.qq.com', 'httpOnly': False, 'name': 'qm_verifyimagesession', 'path': '/', 'secure': False,
             'value': 'h01b81681cf5e6fc07b110725b15498e13f5e7178ad7bf1caa086b48b029ea29e896d1f9e501eef0ab2'},
            {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': '981dc4cbf0dff97f1740d0b985b79f9895769dd36d07d8c72b528464bbba006e'},
            {'domain': '.qq.com', 'httpOnly': False, 'name': 'skey', 'path': '/', 'secure': False,
             'value': '@giNEcON5l'},
            {'domain': '.qq.com', 'httpOnly': False, 'name': 'qm_authimgs_id', 'path': '/', 'secure': False,
             'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1620954871, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'},
            {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_si', 'path': '/', 'secure': False,
             'value': 's8326784000'},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/',
             'secure': False, 'value': '7959230390'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'iSM8bvjWDeaTXx5rb9eodbKy8vaomXbb4350nMONPJst6OO0aO-40kg7M_6l5RfE'},
            {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': False,
             'value': 'ssid=s6051332388'},
            {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'ZEqY8wx3Ww'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a1064943'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'uin', 'path': '/', 'secure': False,
                                    'value': 'o0985063495'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False,
             'value': ''},
            {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/',
             'secure': False, 'value': '5505247232'}]
        # shelve--python的内置模块,专门对数据进行持久化存储的库,相当于小型的数据库
        # 可以通过key,value来把数据保存到shelve中
        db = shelve.open('cookies')
        db['cookie'] = cookies
        db.close()

    def test_qiyeweixin(self):
        db = shelve.open('cookies')
        cookies = db['cookie']
        db.close()
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

        self.driver.find_element_by_css_selector(".index_service_cnt_itemWrap:nth-child(2)").click()
        self.driver.find_element_by_css_selector(".js_go_template_import").click()
        self.driver.find_element_by_css_selector(".ww_fileImporter_fileContainer_uploadInputMask").send_keys(
            "C:/Users/1/PycharmProjects/practice_and_homework/practice/web/demo.xlsx")
        filename = self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_fileNames").text
        assert "demo.xlsx" == filename
        sleep(3)

