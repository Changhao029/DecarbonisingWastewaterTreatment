from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager 

class TestQuerytest():
  def setup_method(self, method=None):
    self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_querytest(self):
    self.driver.get("file:///home/xk/IT_Capstone_Project/main/DecarbonisingWastewaterTreatment/static/data_report.html#Data-Report")
    self.driver.find_element(By.CSS_SELECTOR, "form").click()
    self.driver.find_element(By.ID, "query_id").click()
    print(1)
    self.driver.find_element(By.ID, "query_id").send_keys("2")
    print(2)
    value = self.driver.find_element(By.ID, "query_id").get_attribute("value")
    print(3)
    assert value == "2"
    print(5)
    self.driver.find_element(By.CSS_SELECTOR, "body").click()
    self.driver.close()
 
if __name__=='__main__':
    test = TestQuerytest()
    test.setup_method()
    test.test_querytest()
    
    test.teardown_method()
