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

# click select-option filter
driver.find_element(By.CLASS_NAME, "product_sort_container").click()
driver.find_element(By.XPATH, '//*[@id="header_container"]/div[2]/div/span/select/option[4]').click()

# find all button (add-to-cart)
buttons_add_to_cart = driver.find_elements(By.CSS_SELECTOR, '.btn.btn_primary.btn_small.btn_inventory')

# get max 3 item or less
item_to_add_to_cart = 3 if len(buttons_add_to_cart) > 3 else len(buttons_add_to_cart)
for i in range(item_to_add_to_cart):
  buttons_add_to_cart[i].click()

# check if item added to cart succesfully
driver.find_element(By.ID, "shopping_cart_container").click()
sleep(5)

# terminate chrome driver
driver.quit()
