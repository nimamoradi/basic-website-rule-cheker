import unittest

from selenium import webdriver
from abc import ABCMeta, abstractmethod

from selenium.webdriver import DesiredCapabilities


class Rule(unittest.TestCase, metaclass=ABCMeta):

    def __init__(self, web_url, web_driver=webdriver.Chrome()):
        super().__init__()
        dc = DesiredCapabilities()

        self.url = web_url
        self.driver = web_driver
        self.driver.get(self.url)
        # Alert(self.driver).dismiss()

    def __del__(self):
        self.driver.close()

    @abstractmethod
    def runTest(self):
        raise NotImplementedError("Please Implement this method")
