import unittest

from selenium import webdriver
from abc import ABCMeta, abstractmethod

from selenium.webdriver import DesiredCapabilities


class Rule(unittest.TestCase, metaclass=ABCMeta):

    def __init__(self, web_url):
        super().__init__()
        dc = DesiredCapabilities()

        self.url = web_url
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        # Alert(self.driver).dismiss()

    def __del__(self):
        self.driver.close()

    @abstractmethod
    def runTest(self):
        raise NotImplementedError("Please Implement this method")
