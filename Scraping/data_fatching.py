from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
# from Scraping.constants import page_list

class Fatching:
    def __init__(self, driver:WebDriver):
        self.driver = driver


    def fatch_required_data(self,state, district, sub_district, block, village):
        page_list = list()
        Result = self.driver.find_element(By.ID, 'ContentPlaceHolder1_GridView1').text
        Result_list = Result.split("\n")
        Result_list.pop(0)
        Result_list.pop(-1)
        print(Result_list)
        name = ()
        for m in Result_list:
            individual_farmer_info = list()
            l = m.split(" ")
            l.pop(0)
            name = ""
            gender = l.pop(-1)
            for i in l:
                name = name + " " + str(i)
            individual_farmer_info.append(name.strip())
            individual_farmer_info.append(gender)
            individual_farmer_info.append(state)
            individual_farmer_info.append(district)
            individual_farmer_info.append(sub_district)
            individual_farmer_info.append(block)
            individual_farmer_info.append(village)
            page_list.append(individual_farmer_info)
            print(individual_farmer_info)
            del individual_farmer_info

