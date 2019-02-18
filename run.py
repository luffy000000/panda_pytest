import os
from tomorrow import threads

@threads(2)
def runcases(name='chrome', case_path=''):
    os.system("pytest -s --browser=%s %s" %(name, case_path))

if __name__ == "__main__":
    n = ["chrome", "firefox"]
    for i in n:
        runcases(name=i, case_path="case/test_yoyo_blogs.py")