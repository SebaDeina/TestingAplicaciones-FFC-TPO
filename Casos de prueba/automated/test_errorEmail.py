# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestErrorEmail():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_errorEmail(self):
    self.driver.get("http://127.0.0.1:5000/")
    self.driver.set_window_size(1920, 1055)
    self.driver.find_element(By.LINK_TEXT, "Sign In").click()
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys("prueba@gmail.com")
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").click()
    element = self.driver.find_element(By.NAME, "email")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.NAME, "password").click()
    self.driver.find_element(By.NAME, "password").send_keys("sample")
    self.driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
  
