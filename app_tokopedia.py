from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from time import sleep

# to prevent the browser from closing automatically after the script finishes executing
chrome_option = ChromeOptions()
chrome_option.add_experimental_option('detach', True)

# init chrome driver
driver = webdriver.Chrome(options= chrome_option)
driver.implicitly_wait(15)
driver.maximize_window()

# go to url
driver.get("https://www.tokopedia.com/")
sleep(3)
driver.find_element(By.CLASS_NAME, 'css-11hzwo5').click()

sleep(2)
driver.find_element(By.XPATH, '//button[@data-testid="modal-close"]').click()


# # waiting for ads pop up apears
# try:
#   WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//svg[@fill="none"]')))
#   ads_button = driver.find_element(By.XPATH, '//svg[@fill="none"]')
#   ads_button.click()

#   WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.XPATH, '//button[@data-testid="modal-close"]')))
#   modal_close = driver.find_element(By.XPATH, '//button[@data-testid="modal-close"]')
#   modal_close.click()
# except TimeoutException:
#   print('timeout trigger!')
#   pass

category_button = driver.find_element(By.XPATH, '//div[@data-testid="headerText"]')

sleep(2)
action = ActionChains(driver)
action.move_to_element(category_button)

print("cat butt hit")
sub_cat_button = driver.find_element(By.XPATH, '//a[@data-testid="showHide#6"]')
action.move_to_element(sub_cat_button)

print("sub cat butt hit")
specific_cat_button = driver.find_element(By.XPATH, "//a[normalize-space()='Celana Pendek Anak Laki-Laki']")
action.click(specific_cat_button)
action.perform()

# terminate chrome driver
sleep(5)
driver.quit()
