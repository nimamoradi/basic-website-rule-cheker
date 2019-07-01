import unittest
from selenium import webdriver

from rule.CustomRule import CustomRule
from rule.Rule1077 import Rule1077
from rule.Rule1089 import Rule1089
from rule.Rule1090 import Rule1090
from rule.Rule1092 import Rule1092
from rule.Rule1094 import Rule1094
from rule.Rule1096 import Rule1096
from rule.Rule1099 import Rule1099
from rule.Rule1101 import Rule1101
from rule.Rule1827 import Rule1827
from rule.Rule1934 import Rule1934
from rule.Rule1935 import Rule1935

if __name__ == '__main__':
    suite = unittest.TestSuite()
    url = "file:///C:/Users/nima/Desktop/sample2.htm"
    suite.addTests([Rule1077(url), Rule1089(url), Rule1090(url), Rule1092(url), Rule1094(url),
                    Rule1096(url), Rule1099(url), Rule1101(url), Rule1827(url), Rule1934(url),
                    Rule1935(url)])
    unittest.TextTestRunner().run(suite)

    res_list = [(800, 600), (1024, 768), (1448, 1072), (2048, 1536)]
    # chrome
    for x_size, y_size in res_list:
        print('running test for res x = ', x_size, ' y = ', y_size)
        rule1935 = CustomRule(web_url=url, x=x_size, y=y_size, web_driver=webdriver.Chrome())
        rule1935.runTest()
    # firefox
    for x_size, y_size in res_list:
        print('running test for res x = ', x_size, ' y = ', y_size)
        rule1935 = CustomRule(web_url=url, x=x_size, y=y_size, web_driver=webdriver.Firefox())
        rule1935.runTest()
