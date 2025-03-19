from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
import pytest
from data_provider import DataProvider

login_data = DataProvider.login_data

@pytest.fixture
def setup():
  # init setup part
  chrome_option = ChromeOptions()
  chrome_option.add_experimental_option('detach', True)
  chrome_option.add_argument("--headless=new")

  # init chrome driver
  driver = webdriver.Chrome(options= chrome_option)
  driver.implicitly_wait(5) # can be general stuff for waiting time boundaries
  driver.maximize_window()

  # go to url
  driver.get("https://www.saucedemo.com/")

  # yield driver
  yield driver

  # tear down
  driver.quit()

def test_login_web(setup):
  # login web-app
  setup.find_element(By.ID, "user-name").send_keys("standard_user")
  setup.find_element(By.ID, "password").send_keys("secret_sauce")
  setup.find_element(By.XPATH, '//*[@id="login-button"]').click()

  current_url = setup.current_url
  current_tagline = setup.find_element(By.XPATH, '//span[@data-test="title"]').text
  len_products = len(setup.find_elements(By.XPATH, '//div[@data-test="inventory-list"]'))
  cart_icon = setup.find_element(By.XPATH, '//div[@id="shopping_cart_container"]')
  
  assert current_url == "https://www.saucedemo.com/inventory.html"
  assert current_tagline == "Products"
  assert len_products > 0
  assert cart_icon.is_displayed()

@pytest.mark.parametrize('username, password, error_message', login_data)
def test_negative_case_login_web(username, password, error_message, setup):
  # login web-app
  setup.find_element(By.ID, "user-name").send_keys(username)
  setup.find_element(By.ID, "password").send_keys(password)
  setup.find_element(By.ID, 'login-button').click()

  current_url = setup.current_url
  error_text = setup.find_element(By.XPATH, '//h3[@data-test="error"]')
  
  assert current_url == "https://www.saucedemo.com/"
  assert error_text.is_displayed()
  assert error_text.text == error_message
