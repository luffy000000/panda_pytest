import pytest
import time
from pages.loginpage import _login, _login_result, _get_alert


test_login_data = [("admin", "123456", "admin"), ("admin1", "123123", "")]

class TestLogin():
    @pytest.fixture(scope="function", auto=True)
    def startPage(self, driver, host):
        print("---让每个用列都从登录首页开始:---start!---")
        driver.get(host)
        driver.delete_all_cookies()
        driver.refresh()

    def test_login_success(self, driver, host):
        _login(driver, host, "admin", "123456")
        result1 = _login_result(driver, "admin")
        print("登录结果:%s" % result1)
        assert result1

    def test_login_fail(self, driver, host):
        _login(driver, host, "admin1", "123123")
        result = _get

    @pytest.mark.parametrize("user, psw, expect", test_login_data)
    def test_login(self, user, psw, expect):
        self.login(user, psw)
        result = self.ximopanda.get_text(login_user)
        print("登录结果，获取到用户名：%s" %result)
        assert result == expect



if __name__ == "__main__":
    pytest.main(['-s', 'test_login.py'])

