from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

# to prevent the browser from closing automatically after the script finishes executing
chrome_option = ChromeOptions()
chrome_option.add_experimental_option('detach', True)

# init chrome driver
driver = webdriver.Chrome(options= chrome_option)
driver.maximize_window()

# go to url
driver.get("https://www.saucedemo.com/")

# login web-app
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
sleep(3)

# terminate chrome driver
driver.quit()
