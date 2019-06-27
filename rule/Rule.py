from selenium import webdriver
from abc import ABCMeta, abstractmethod


class Rule(metaclass=ABCMeta):

    def __init__(self, web_url):
        self.url = web_url
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)

    def __del__(self):
        self.driver.close()

    @abstractmethod
    def task(self):
        raise NotImplementedError("Please Implement this method")
