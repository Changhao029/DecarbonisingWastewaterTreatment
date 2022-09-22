import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager 

'''
Automation Testing
  Page function: 
    including input, click, drag and select
'''
class Testpagefunction():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_pagefunction(self):
    #self.driver.get("file:///home/xk/IT_Capstone_Project/main/DecarbonisingWastewaterTreatment/static/data_report.html")
    self.driver.get("http://localhost:50003/DecarbonisingWastewaterTreatment/static/data_report.html")
    self.driver.set_window_size(1846, 861)

    #Test - Query function by id
    #Test - Input boxes are editable
    element_id = self.driver.find_element(By.ID, "query_id")
    assert element_id.is_enabled() is True

    #Test - Input value is correct
    element_id.send_keys("1")
    assert element_id.get_attribute('value') == '1'
    self.driver.find_element(By.CSS_SELECTOR, ".query_download:nth-child(1)").click()
    element_id.clear()

    #Test - Query function by station
    #Test - Input boxes are editable
    element_station = self.driver.find_element(By.ID, "query_station")
    assert element_station.is_enabled() is True

    #Test - Input value is correct
    element_station.send_keys("231825A")
    assert element_station.get_attribute('value') == '231825A'
    self.driver.find_element(By.CSS_SELECTOR, ".query_download:nth-child(1)").click()

    #Test - Page turn button clickable
    next_button = self.driver.find_element(By.LINK_TEXT, "Next")
    assert next_button.is_enabled() == True
    next_button.click()

    previous_button = self.driver.find_element(By.LINK_TEXT, "Previous")
    assert previous_button.is_enabled() == True
    previous_button.click()

    #Test - Download button clickable
    download_button  = self.driver.find_element(By.CSS_SELECTOR, ".query_download:nth-child(2)")
    assert download_button.is_enabled() == True
    download_button.click()

    self.driver.close()

  def test_visual(self):
    #self.driver.get("file:///home/xk/IT_Capstone_Project/main/DecarbonisingWastewaterTreatment/static/data_report.html")
    self.driver.get("http://localhost:50003/DecarbonisingWastewaterTreatment/static/data_report.html")
    self.driver.set_window_size(1846, 861)
    self.driver.find_element(By.ID, "Data Center").click()

    time.sleep(2)

    #Test - Every visualization could drag and select
    element = self.driver.find_element(By.CSS_SELECTOR, "#container1 canvas")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()

    element = self.driver.find_element(By.CSS_SELECTOR, "#container1 canvas")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()

    self.driver.close()


if __name__=='__main__':
    test = Testpagefunction()
    test.setup_method()
    test.test_pagefunction()
    test.test_visual()
    
    test.teardown_method()
