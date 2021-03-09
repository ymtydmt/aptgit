import pytest
import os
import time
from common.function import *
import sys

path='D:\\pycharm\\tianshu\\'
sys.path.append(path)

# report_dir='test_report'
if __name__ == '__main__':
    # now = time.strftime("%Y-%m-%d %H_%M_%S")
    # report_name = report_dir + '/' + now + 'result.html'
    # 生成json测试用例保存在./report里面
    pytest.main(['-s','-q','--alluredir','test_report',r'D:\pycharm\tianshu\test_case\test_login.py'])
    # 调用os模块生产html样式的报告把他保存在test_report里面index

    with open('report_name','wb')as f:
         runer=os.system('allure generate test_report -o ./report --clean')
    # latest_report=latest_report(report_dir)
    # send_mail(latest_report)
