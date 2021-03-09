from driver import *

# 测试用例类里面定义了测试用例启始方法
class TStarEnd():
    def setup(self):
        self.driver=browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()