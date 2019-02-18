import pytest
import time

def test_blog(driver):
    driver.get("https://www.cnblogs.com/yoyoketang/")
    time.sleep(3)
    t = driver.title
    print("测试结果：%s" % t)
    assert "上海-悠悠" in t, "失败原因：打开博客园失败"

if __name__ == "__main__":
    pytest.main(['-v', 'test_1.py'])