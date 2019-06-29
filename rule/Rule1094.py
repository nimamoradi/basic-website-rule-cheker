from rule.Rule import Rule


class Rule1094(Rule):
    # https://rules.sonarsource.com/html/type/Code%20Smell/RSPEC-1094
    def task(self):
        # we will check that refresh meta is not on site

        metas = self.driver.find_elements_by_tag_name("meta")
        for meta in metas:
            http = meta.get_attribute("http-equiv")
            if http is not None:
                assert not http == "refresh", 'site should not refresh using meta'

        print('test passed 1094')
