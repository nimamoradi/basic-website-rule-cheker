from rule.Rule import Rule


class Rule1089(Rule):
    def runTest(self):
        fieldsets_with_legend = self.driver.find_elements_by_xpath("//fieldset/legend[1]")
        all_fieldsets = self.driver.find_elements_by_tag_name("fieldset")

        self.assertEqual(len(fieldsets_with_legend), len(all_fieldsets))

        print('test passed 1089')
