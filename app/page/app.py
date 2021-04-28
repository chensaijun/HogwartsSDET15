#! /usr/bin/python 3
# -*- coding:UTF8 -*-c
from appium import webdriver

from app.page.main_page import MainPage


class App:
    def start(self,driver = None):
        if driver == None:
            disired_caps = {
                "platformName": "android",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.LaunchSplashActivity",
                "noReset": True,
                "dontStopAppOnReset": True,
                "skipDeviceInitialization": True,
                "unicodeKeyBoard": True,
                "resetKeyBoard": True,
                'skipServerInstallation': 'true'
            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", disired_caps)
            self.driver.implicitly_wait(10)
        else:
            # 重启app
            self.driver.launch_app()
        #return self返回的是类的实例
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()

    def close(self):
        self.driver.quit()

    def goto_mainpage(self) ->MainPage:
        return MainPage(self.driver)
