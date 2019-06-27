from rule.Rule1092 import Rule1092
from rule.Rule1094 import Rule1094


class RuleReport():
    def __init__(self, website_url):
        self.url = website_url

    def test(self):
        rule1094 = Rule1094(self.url)
        rule1094.task()


if __name__ == "__main__":
    #
    url = "file:///C:/Users/nima/Desktop/sample1.htm"

    test = RuleReport(website_url=url)
    test.test()