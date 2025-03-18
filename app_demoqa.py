from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# to prevent the browser from closing automatically after the script finishes executing
chrome_option = ChromeOptions()
chrome_option.add_experimental_option('detach', True)
# chrome_option.add_argument("--headless=new")

# init chrome driver
driver = webdriver.Chrome(options= chrome_option)
driver.implicitly_wait(30)
driver.maximize_window()

# go to url
# driver.get("https://demoqa.com/menu")
driver.get("https://demoqa.com/droppable")

# menu_2 = driver.find_element(By.XPATH, "//a[normalize-space()='Main Item 2']")
# sub_sub_list = driver.find_element(By.XPATH, "//a[normalize-space()='SUB SUB LIST »']")
# specific_menu = driver.find_element(By.XPATH, "//a[normalize-space()='Sub Sub Item 2']")

tab_sample = driver.find_element(By.XPATH, "//a[@id='droppableExample-tab-simple']")
dragdable_box = driver.find_element(By.XPATH, "//div[@id='draggable']")
target_dragdable_box = driver.find_element(By.XPATH, "//div[@id='droppable']")


action = ActionChains(driver)

action.drag_and_drop(dragdable_box, target_dragdable_box)
sleep(3)
action.perform()


# try:
#   WebDriverWait(driver, 5).until(EC.alert_is_present())
#   driver.switch_to.alert.accept()
# except TimeoutException:
#   print('timeout trigger!')
#   pass

# terminate chrome driver
sleep(3)
driver.quit()
