import unittest

from rule.CustomRule import CustomRule
from rule.Rule1092 import Rule1092
from rule.Rule1094 import Rule1094
from rule.Rule1101 import Rule1101
from rule.Rule1827 import Rule1827
from rule.Rule1935 import Rule1935

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests([Rule1092(), Rule1094(), Rule1101(), Rule1827(), Rule1935(), ])
    unittest.TextTestRunner().run(suite)
