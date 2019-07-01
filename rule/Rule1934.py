from rule.Rule import Rule


class Rule1934(Rule):
    def runTest(self):
        links = self.driver.find_elements_by_tag_name("a")
        print(len(links))
        for link in links:
            name = link.get_attribute("name")
            print(name)
            self.assertTrue(name is None or name == '', 'a should not have name attribute')

