import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class TestCreatelocation():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_createlocation(self):
        self.driver.get("http://www.learnwebservices.com/locations/server")
        self.driver.set_window_size(1226, 731)
        self.driver.find_element(By.ID, "nameInput").click()
        self.driver.find_element(By.ID, "nameInput").send_keys("a")
        self.driver.find_element(By.ID, "coordsInput").send_keys("1,1")
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        assert self.driver.find_element(By.CSS_SELECTOR, ".alert").text == "Location has saved"