from rule.Rule import Rule


class Rule1077(Rule):
    def runTest(self):
        all_inputs = self.driver.find_elements_by_tag_name("input")
        all_images = self.driver.find_elements_by_tag_name("img")

        for image in all_images:
            alt = image.get_attribute('alt')
            self.assertTrue(alt is not None or alt != "", 'all images should have alt ')

        for _input in all_inputs:
            alt = _input.get_attribute('alt')
            self.assertFalse(alt is None or alt == "", 'all inputs should have alt ')
