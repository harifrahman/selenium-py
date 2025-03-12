from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from time import sleep

# to prevent the browser from closing automatically after the script finishes executing
chrome_option = ChromeOptions()
chrome_option.add_experimental_option('detach', True)
chrome_option.add_argument("--headless=new")

# init chrome driver
driver = webdriver.Chrome(options= chrome_option)
driver.implicitly_wait(30)
driver.maximize_window()

# go to url
driver.get("https://demoqa.com/alerts")
driver.find_element(By.ID, 'timerAlertButton').click()

try:
  WebDriverWait(driver, 5).until(EC.alert_is_present())
  driver.switch_to.alert.accept()
except TimeoutException:
  print('timeout trigger!')
  pass

# terminate chrome driver
sleep(7)
driver.quit()
