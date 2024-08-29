import os
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import service
from selenium.webdriver.remote.webdriver import WebDriver

from Scraping.page_iteration import Page




class Scraping(webdriver.Chrome, Page):
    page_list = list()
    def __init__(self, driver_path=r"C:\SeleniumDrivers",
                 teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Scraping, self).__init__(options=options)
        self.implicitly_wait(15)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        BASE_PATH="https://pmkisan.gov.in/Rpt_BeneficiaryStatus_pub.aspx"
        self.get(BASE_PATH)

    def state_info(self):
        state_text = self.find_element(By.ID,'ContentPlaceHolder1_DropDownState')
        state_list = (state_text.text).split("\n")
        state_list.pop(0)
        return state_list

    def district_info(self):
        district_text = self.find_element(By.ID,'ContentPlaceHolder1_DropDownDistrict')
        district_list = (district_text.text).split("\n")
        district_list.pop(0)
        return district_list

    def sub_district_info(self):
        sub_district_text = self.find_element(By.ID,'ContentPlaceHolder1_DropDownSubDistrict')
        sub_district_list = (sub_district_text.text).split("\n")
        sub_district_list.pop(0)
        return sub_district_list

    def block_info(self):
        block_text = self.find_element(By.ID,'ContentPlaceHolder1_DropDownBlock')
        block_list = (block_text.text).split("\n")
        block_list.pop(0)
        return block_list

    def village_info(self):
        village_text = self.find_element(By.ID,'ContentPlaceHolder1_DropDownVillage')
        village_list = (village_text.text).split("\n")
        village_list.pop(0)
        return village_list

    def select_state(self,state):
        self.find_element(By.XPATH, '//*[@id="ContentPlaceHolder1_DropDownState"]').send_keys(state)
        time.sleep(1)

    def select_district(self,district):
        self.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_DropDownDistrict"]').send_keys(district)
        time.sleep(1)

    def select_sub_district(self,sub_district):
        self.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_DropDownSubDistrict"]').send_keys(sub_district)
        time.sleep(1)

    def select_block(self,block):
        self.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_DropDownBlock"]').send_keys(block)
        time.sleep(1)

    def select_village(self,village):
        self.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_DropDownVillage"]').send_keys(village)
        time.sleep(2)

    def click_search(self, state, district, sub_district, block, village):
        self.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_btnsubmit"]').click()
        time.sleep(1)
        #Page.next_page(state, district, sub_district, block, village)
        #Page.next_page(state=state, district=district, sub_district=sub_district, block=block, village=village)
        # Assuming you have a class named 'Page'
        page_instance = Page(self)
        page_instance.next_page(state=state, district=district, sub_district=sub_district, block=block, village=village)



    def final_result(self):
        DataStoring.show_data()


