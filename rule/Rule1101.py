from rule.Rule import Rule


class Rule1101(Rule):

    def runTest(self):
        # hashmap contains links
        links_dict = {}

        links = self.driver.find_elements_by_tag_name("a")
        for link in links:
            url = link.get_attribute("href")
            link_text = link.text
            if link_text in links_dict:
                print(link_text)
                assert url == links_dict[link_text],'link '+url + 'have different texts 1 - ' +link_text

            links_dict[link_text] = url

        print(links_dict)
        print('test passed 1101')
