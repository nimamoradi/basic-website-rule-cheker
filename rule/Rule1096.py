from rule.Rule import Rule


class Rule1096(Rule):
    def runTest(self):
        # which extension we consider as image
        title = self.driver.find_element_by_xpath('/html/head/title')

        self.assertTrue(title is not None or title != "", 'all pages should have titles ')

        print('test passed 1096')
