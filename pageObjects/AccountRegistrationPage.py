from selenium.webdriver.common.by import By


class AccountRegistrationPage():
    txt_firstname_name = "firstname"
    txt_lastname_name = "lastname"
    txt_email_name = "email"
    txt_telphone_name = "telephone"
    txt_password_name = "password"
    txt_confpassword_name = "confirm"
    #chk_subscribe_xpath = "//input[@id='input-newsletter-yes']"
    chk_policy_xpath = "//input[@name='agree']"
    btn_cont_xpath="//input[@value='Continue']"
    text_msg_conf_xpath="//h1[normalize-space()='Your Account Has Been Created!']"

    def __init__(self, driver):
        self.driver = driver

    def setFirstName(self,fname):
      self.driver.find_element(By.NAME,self.txt_firstname_name).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element(By.NAME,self.txt_lastname_name).send_keys(lname)

    def setEmail(self,email):
       useremail = self.driver.find_element(By.NAME,self.txt_email_name)
       useremail.clear()
       useremail.send_keys(email)

    def setTelephone(self, tel):
        self.driver.find_element(By.NAME, self.txt_telphone_name).send_keys(tel)

    def setPassword(self,pwd):
        userpwd = self.driver.find_element(By.NAME,self.txt_password_name)
        userpwd.clear()
        userpwd.send_keys(pwd)

    def setConfirmPassword(self, cnfpwd):
        self.driver.find_element(By.NAME, self.txt_confpassword_name).send_keys(cnfpwd)

    # def setsubscrib(self):
    #     self.driver.find_element(By.XPATH,self.chk_subscribe_xpath).click()

    def setPrivacyPolicy(self):
        self.driver.find_element(By.XPATH,self.chk_policy_xpath).click()

    def clickContinue(self):
        self.driver.find_element(By.XPATH,self.btn_cont_xpath).click()

    def getconfirmationmsg(self):
        try:
            return self.driver.find_element(By.XPATH,self.text_msg_conf_xpath).text
        except:
            None


