from rule.Rule import Rule


class Rule1090(Rule):

    def runTest(self):
        # Frames allow different web pages to be put together on the same visual space. Users without disabilities
        # can easily scan the contents of all frames at once. However, visually impaired users using screen readers
        # hear the page content linearly.
        frames = self.driver.find_elements_by_xpath('//frame')

        print('size ', len(frames))
        for frame in frames:
            title = frame.get_attribute("title")
            print('test', frame)
            self.assertTrue(title is not None or title != "", 'all frames should have title')
