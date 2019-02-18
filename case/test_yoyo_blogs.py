import pytest
import time

def test_01(driver):

    '''用例1-打开首页'''

    driver.get("https://www.cnblogs.com/yoyoketang")
    time.sleep(2)
    t = driver.title
    print(t)
    assert "上海-悠悠" in t

def test_02(driver):

    '''用例2-标签页'''

    driver.get("https://www.cnblogs.com/yoyketang/tag/pytest/")
    time.sleep(2)
    t = driver.title
    assert "pytest - 标签" in t

if __name__ == "__main__":
    pytest.main(["-s", "--browser=chrome", "test_yoyo_blogs.py"])
