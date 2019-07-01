from rule.Rule import Rule


class CustomRule(Rule):
    def __init__(self, web_url, x, y):
        super().__init__(web_url)
        self.driver.set_window_size(x, y)

    def runTest(self):
        # which extension we consider as image

        input1 = self.driver.find_element_by_xpath('/html/body/div/form/span[1]')
        input2 = self.driver.find_element_by_xpath('//*[@id="field2"]')
        input3 = self.driver.find_element_by_xpath('//*[@id="field3"]')
        input4 = self.driver.find_element_by_xpath('//*[@id="field4"]')

        items = [input1, input2, input3, input4, ]

        for item in items:
            for ot_item in items:
                if item is not ot_item:
                    assert not (check_collision_vertical(item, ot_item)
                                and check_collision_horizontal(item,
                                                               ot_item)), 'first failed for ' + item.get_attribute(
                        'id') + ' with ' + ot_item.get_attribute('id')

        print('custom test passed')


def check_collision_vertical(item1, item2):
    return item1.location['x'] <= item2.location['x'] <= item1.location['x'] + item1.size['width']


def check_collision_horizontal(item1, item2):
    return item1.location['y'] <= item2.location['y'] <= item1.location['y'] + item1.size['height']
