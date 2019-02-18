from selenium import webdriver
from common.base import Base
import time

#----------元素定位信息----------#
loc1 = ("id", "username")
loc2 = ("id", "password")
loc3 = ("id", "login_btn")

result_loc = ("xpth", "//div[@class='pull-left info']/p")

def _login(driver, host, user='admin', psw='123456'):

    '''普通登录函数'''
    ximopanda = Base(driver)
    driver.get(host)
    ximopanda.sendKeys(loc1, user)
    ximopanda.sendKeys(loc2, psw)
    ximopanda.click(loc3)
    time.sleep(2)

def _login_result(driver, _text):
    ximopanda = Base(driver)
    r = ximopanda.is_text_in_element(result_loc, _text)
    return r

def _get_alert(driver):
    ximopanda = Base(driver)
    try:
        alert = ximopanda.is_alert()
        text = alert.text
        alert.accept()
        return text
    except:
        return ""

if __name__ == "__main__":
    driver = webdriver.Chrome()
    _login(driver, "http://manage-sandbox.ximopanda.com/")