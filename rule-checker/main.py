from rule.Rule1092 import Rule1092


class RuleReport():
    def __init__(self, website_url):
        self.url = website_url

    def test(self):
        rule1092 = Rule1092(self.url)
        rule1092.task()


if __name__ == "__main__":
    #
    url = "http://example.com/"

    test = RuleReport(website_url=url)
    test.test()