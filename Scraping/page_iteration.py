import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from Scraping.data_fatching import Fatching

class Page(Fatching):
    def __int__(self, driver:WebDriver):
        self.driver = driver

    def next_page(self, state, district, sub_district, block, village):
        Fatching_instance = Fatching(self.driver)
        Fatching_instance.fatch_required_data(state=state, district=district, sub_district=sub_district, block=block, village=village)
        try:
            i = 2
            while True:
                page = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,f'''[href="javascript:__doPostBack('ctl00$ContentPlaceHolder1$GridView1','Page${i}')"]''')))
                self.driver.execute_script("arguments[0].click();",page)
                time.sleep(1)
                Fatching_instance.fatch_required_data(state=state, district=district, sub_district=sub_district, block=block, village=village)
                i = i + 1
        except TimeoutException:
            return
        except Exception as e:
            if "no such element:" in str(e) or "Unable to locate element:" in str(e):
                return
            else:
                raise





