from rule.Rule import Rule


class Rule1935(Rule):

    def task(self):
        # The goal of this rule is to ban the usage of HTML "style" property to make sure that all CSS styles are
        # defined in CSS classes. Consolidating all styling into classes makes it easier to read, understand and
        # maintain.

        style_tags = self.driver.find_elements_by_xpath("//*[not(*)]")
        for style_tag in style_tags:
            style_att = style_tag.get_attribute("style")
            assert style_att is None, 'style attribute should not exist in html'

        print('test passed 1935')
