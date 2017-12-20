from time import sleep
from random import randint
from selenium import webdriver
from pyvirtualdisplay import Display

class MuncherySpider():
    def __init__(self):
    	self.url_to_crawl = "https://172.22.2.6/connect/PortalMain"
	
    def login(self):
        print('getting pass the gate page...')
        self.display = Display(visible=0, size=(800, 600))
        self.display.start()
        self.driver = webdriver.Firefox('C:/Users/vedar/Desktop/TEST/')
        url = "https://172.22.2.6/connect/PortalMain"
        self.driver.get(url)
        sleep(5)
        while 1:
            try:
                form=self.driver.find_element_by_xpath('//*[@class="username_pass_table"]')
                form.find_element_by_xpath('.//*[@cpname="username"]').send_keys('16uec139')
                form.find_element_by_xpath('.//*[@cpname="password"]').send_keys('LNM@QE42')
                form.find_element_by_xpath('//*[@id="UserCheck_Login_Button"]').click()
                sleep(3*60*60)
            except:
                try:
                    self.driver.find_element_by_xpath('//*[@id="UserCheck_Logoff_Button"]').click()
                    sleep(5)
                except:
                    try:
                        self.driver.find_element_by_xpath('//*[@class="portal_link"]').click()
                        sleep(5)
                    except:
                        self.driver.quit()
         
        

Munchery = MuncherySpider()
Munchery.login()
