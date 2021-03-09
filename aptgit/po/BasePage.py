from time import sleep


class Page():
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'http://172.20.10.58:8082/'
        # 延时等待10秒
        self.timeout = 10

    def _open(self, url):
        url_ = self.base_url + url
        # 窗口最大化
        self.driver.maximize_window()
        self.driver.get(url_)
        sleep(2)


    def open(self):
        self._open(self.url)
    # 封装一个函数元素定位方法
    def find_element(self, *loc):
        return self.driver.find_element(*loc)