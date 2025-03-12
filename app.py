from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# to prevent the browser from closing automatically after the script finishes executing
chrome_option = ChromeOptions()
chrome_option.add_experimental_option('detach', True)

# to make in run in Background
# chrome_option.add_argument("--headless=new")

# init chrome driver
driver = webdriver.Chrome(options= chrome_option)
driver.implicitly_wait(5) # can be general stuff for waiting time boundaries
driver.maximize_window()

# go to url
driver.get("https://www.saucedemo.com/")

# login web-app
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
# sleep(3)

# click select-option filter
select_option = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
select_option.select_by_value('hilo')

# find all button (add-to-cart)
buttons_add_to_cart = driver.find_elements(By.XPATH, '//button[@class="btn btn_primary btn_small btn_inventory "]')

# get max 3 item or less
# item_to_add_to_cart = 3 if len(buttons_add_to_cart) > 3 else len(buttons_add_to_cart)
for i in range(3):
  buttons_add_to_cart[i].click()

# check if item added to cart succesfully
# driver.find_element(By.ID, "shopping_cart_container").click()

# click burger button
driver.find_element(By.ID, 'react-burger-menu-btn').click()

try:
  WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, 'about_sidebar_link')))

  driver.find_element(By.ID, 'about_sidebar_link').click()
except TimeoutException:
  print('timeout trigger!')
  pass

# terminate chrome driver
driver.quit()
