from selenium.common.exceptions import NoSuchElementException

from rule.Rule import Rule


class Rule1099(Rule):

    def runTest(self):

        driver = self.driver
        # we can not use driver in try catch directly
        try:
            elems = driver.find_elements_by_xpath('//img')
            for elem in elems:
                w = elem.get_attribute('width')
                h = elem.get_attribute('height')
                alt = elem.get_attribute('alt')
                # alt will be checked somewhere else
                self.assertTrue(
                    w is not None and w != '' and w != '0',
                    'lack of required attributes "img->width"'
                )
                self.assertTrue(
                    h is not None and h != '' and h != '0',
                    'lack of required attributes "img->height"'
                )

            elems.clear()
        except NoSuchElementException as exception:
            pass
