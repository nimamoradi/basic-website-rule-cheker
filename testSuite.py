import unittest

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
    suite.addTests([Rule1099(url), ])
    unittest.TextTestRunner().run(suite)

    # res_list = [(800, 600), (1024, 768), (1448, 1072), (2048, 1536)]
    # for x_size, y_size in res_list:
    #     print('running test for res x = ', x_size, ' y = ', y_size)
    #     rule1935 = CustomRule(url, x=x_size, y=y_size)
    #     rule1935.runTest()
