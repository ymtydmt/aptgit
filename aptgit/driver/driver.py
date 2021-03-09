from selenium import webdriver

def browser():
    # driver=webdriver.Firefox()
    # 打开chrome浏览器
    driver=webdriver.Chrome()
    # driver=webdriver.Ie()
    # driver=webdriver.PhantomJS()

    #打开指定的网址
    driver.get("http://172.20.10.58:8082/")

    return driver

if __name__ == '__main__':
    browser()