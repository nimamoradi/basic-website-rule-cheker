from selenium import webdriver
from abc import ABCMeta, abstractmethod

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.alert import Alert


class Rule(metaclass=ABCMeta):

    def __init__(self, web_url):
        dc = DesiredCapabilities()

        self.url = web_url
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        # Alert(self.driver).dismiss()

    def __del__(self):
        self.driver.close()

    @abstractmethod
    def task(self):
        raise NotImplementedError("Please Implement this method")
