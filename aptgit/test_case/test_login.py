from po.LoginPage import *
from common import function,myunit
import logging.config




# 读取日志文件配置文件
config_file=open(r'D:\pycharm\tianshu\config\log.cof',encoding='utf-8')
logging.config.fileConfig(config_file)

# 定义一个类类里面继承了我们之前封装的方法测试用例setup和teardown方法
class Test_LoginPage_001(myunit.TStarEnd):
    def test_login001(self):
        po=LoginPage(self.driver)
        po.Login_action('lijs','1234@abcd','1000','测试','1001')
        po.Login_action('lijs', '1234@abcd', '1000', '测试', '1001')



