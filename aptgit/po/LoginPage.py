from po.BasePage import  *
from selenium.webdriver.common.by import By
from time import sleep


# 定义一个类吧我们的元素定位写入一个类里面使用的时候直接调用就好了

class LoginPage(Page):
    url=''

    username_loc=(By.NAME,'username')
    password_loc=(By.NAME,'password')
    submit_loc=(By.CLASS_NAME,'login-btn')
    shouye_loc=(By.LINK_TEXT,'天枢产品管理')
    zidian_loc=(By.LINK_TEXT,'基础信息管理')
    zd_loc=(By.LINK_TEXT,'字典管理')
    jr_loc=(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div/table/tbody/tr/td/a[1]/span')
    tm_loc=(By.NAME,'dictItem')
    mc_loc=(By.NAME,'itemName')
    # qd_loc=(By.XPATH,'//*[@id="index_add_form"]/table/tbody/tr[3]/td[2]/a[1]/span')
    qx_loc=(By.XPATH,'//*[@id="index_add_form"]/table/tbody/tr[3]/td[2]/a[2]/span')
    ck_loc=(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div/table/tbody/tr/td/a[3]/span/span')
    cxtm_loc=(By.XPATH,'//*[@id="search_form"]/table/tbody/tr[1]/td[2]/span/span/input')
    qd_loc=(By.XPATH,'//*[@id="search_form"]/table/tbody/tr[2]/td[2]/a[1]/span/span')
    xd_loc=(By.XPATH,'//*[@id="1$cell$1"]/div')
    xg_loc=(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div/table/tbody/tr/td/a[2]/span')
    xgqx_loc=(By.XPATH,'//*[@id="index_update_form"]/table/tbody/tr[3]/td[2]/a[2]/span')






    def type_username(self,username):
        self.find_element(*self.username_loc).clear()
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self,password):
        self.find_element(*self.password_loc).clear()
        self.find_element(*self.password_loc).send_keys(password)

    def type_submit(self):
        self.find_element(*self.submit_loc).click()
    def type_shouye(self):
        self.find_element(*self.shouye_loc).click()
    def type_zidian(self):
        self.find_element(*self.zidian_loc).click()
    def type_zd(self):
        self.find_element(*self.zd_loc).click()
        sleep(5)
    def type_zj(self):
        self.driver.switch_to.frame("mini-iframe-9")
        sleep(5)
    def type_jr(self):
        self.find_element(*self.jr_loc).click()
    def type_tm(self,dictItem):
        self.find_element(*self.tm_loc).send_keys(dictItem)
    def type_mc(self,itemName):
        self.find_element(*self.mc_loc).send_keys(itemName)
    # def type_qd(self):
    #     self.find_element(*self.qd_loc).click()
    def type_qx(self):
        self.find_element(*self.qx_loc).click()
    def type_ck(self):
        self.find_element(*self.ck_loc).click()
    def type_cxtm(self,cxtm):
        self.find_element(*self.cxtm_loc).send_keys(cxtm)
    def type_qd(self):
        self.find_element(*self.qd_loc).click()
    def type_xd(self):
        self.find_element(*self.xd_loc).click()
    def type_xg(self):
        self.find_element(*self.xg_loc).click()
    def type_xgqx(self):
        self.find_element(*self.xgqx_loc).click()




    def Login_action(self,username,password,dictItem,itemName,cxtm):
        self.open()
        self.driver.implicitly_wait(6)
        self.type_username(username)
        self.type_password(password)
        self.type_submit()
        self.type_shouye()
        self.type_zidian()
        self.type_zd()
        self.type_zj()
        sleep(4)
        self.type_jr()
        sleep(4)
        self.type_tm(dictItem)
        sleep(4)
        self.type_mc(itemName)
        # sleep(4)
        # self.type_qd()
        sleep(3)
        self.type_qx()
        sleep(3)
        self.type_ck()
        self.type_cxtm(cxtm)
        sleep(2)
        self.type_qd()
        sleep(2)
        self.type_xd()
        sleep(2)
        self.type_xg()
        sleep(2)
        self.type_xgqx()