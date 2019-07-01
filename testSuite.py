import unittest

from rule.CustomRule import CustomRule
from rule.Rule1092 import Rule1092
from rule.Rule1094 import Rule1094
from rule.Rule1101 import Rule1101
from rule.Rule1827 import Rule1827
from rule.Rule1935 import Rule1935

if __name__ == '__main__':
    suite = unittest.TestSuite()
    url = "http://www.example.com/"
    suite.addTests([Rule1092(url), Rule1094(url), Rule1101(url), Rule1827(url), Rule1935(url)])
    unittest.TextTestRunner().run(suite)

    res_list = [(800, 600), (1024, 768), (1448, 1072), (2048, 1536)]
    for x_size, y_size in res_list:
        print('running test for res x = ', x_size, ' y = ', y_size)
        rule1935 = CustomRule(url, x=x_size, y=y_size)
        rule1935.runTest()
