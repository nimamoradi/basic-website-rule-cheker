import unittest

from rule.CustomRule import CustomRule
from rule.Rule1092 import Rule1092
from rule.Rule1094 import Rule1094
from rule.Rule1101 import Rule1101
from rule.Rule1827 import Rule1827
from rule.Rule1935 import Rule1935


class RuleReport():
    def __init__(self, website_url):
        self.url = website_url

    def test(self):
        rule1935 = Rule1827(self.url)
        rule1935.task()

        #     rule1935.task()
        res_list = [(800, 600), (1024, 768), (1448, 1072), (2048, 1536)]
        for x_size, y_size in res_list:
            print('running test for res x = ', x_size, ' y = ', y_size)
            rule1935 = CustomRule(self.url, x=x_size, y=y_size)
            rule1935.task()


if __name__ == "__main__":
    #
    url = "file:///C:/Users/nima/Desktop/sample1.htm"

    test = RuleReport(website_url=url)
    test.test()