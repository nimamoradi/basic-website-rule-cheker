from rule.Rule import Rule


class Rule1092(Rule):

    def runTest(self):
        # which extension we consider as image
        image_extension_list = ['.png', '.gif', '.tif', '.jpg', '.jpeg']
        links = self.driver.find_elements_by_tag_name("a")
        for link in links:
            url = link.get_attribute("href")
            for ext in image_extension_list:
                self.assertFalse( url.endswith(ext), 'a tag with href of image ' + url + " with ext " + ext)

        print('test passed 1092')
