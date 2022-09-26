from pickle import TRUE
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager 

'''
Automation Testing
  Browser page control functions: 
    including start, close and page jumping
'''
class Testbasiccontrol():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_basiccontrol(self):
    #Open html
    #self.driver.get("file:///home/xk/IT_Capstone_Project/main/DecarbonisingWastewaterTreatment/static/data_report.html")
    self.driver.get("http://localhost:50003/DecarbonisingWastewaterTreatment/static/data_report.html")
    self.driver.set_window_size(1846, 861)

    #Test - the center page buttons are clickable
    center_button = self.driver.find_element(By.ID, "Data Center")
    assert center_button.is_enabled() == True


    #Test - the center page buttons could offer page jump
    center_button.click()
    page_title = self.driver.find_element(By.CSS_SELECTOR, ".section-title").text
    assert page_title == "DATA CENTER"

    #Test - the report page buttons are clickable
    report_button = self.driver.find_element(By.ID, "Data Report")
    assert report_button.is_enabled() == True
    report_button.click()

    #Test - the center page buttons could offer page jump
    page_title = self.driver.find_element(By.CSS_SELECTOR, ".section-title").text
    assert page_title == "DATA REPORT"

    #Close html
    self.driver.close()
  
if __name__=='__main__':
    test = Testbasiccontrol()
    test.setup_method()
    test.test_basiccontrol()
    
    test.teardown_method()