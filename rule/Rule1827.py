from rule.Rule import Rule

caption = 'caption'
col = 'col'
div = 'div'
embed = 'embed'
h1 = 'h1'
h2 = 'h2'
h3 = 'h3'
h4 = 'h4'
h5 = 'h5'
h6 = 'h6'
hr = 'hr'
iframe = 'iframe'
img = 'img'
legend = 'legend'
input = 'input'
object_tag = 'object'
p = 'p'
table = 'table'
tbody = 'tbody'
form = 'form'
th = 'th'
td = 'td'
body = 'body'
tr = 'tr'
tfoot = 'tfoot'
thead = 'thead'
a = 'a'
link = 'link'
br = 'br'
applet = 'applet'
button = 'button'
fieldset = 'fieldset'
frame = 'frame'
label = 'label'
marquee = 'marquee'
param = 'param'
select = 'select'
span = 'span'
textarea = 'textarea'
option = 'option'
script = 'script'
area = 'area'
head = 'head'
meta = 'meta'
li = 'li'
ul = 'ul'
html = 'html'
ol = 'ol'
pre = 'pre'
id_tag = 'id'


class Rule1827(Rule):
    def runTest(self):
        # adding rules
        attribute_dict = {'align': [caption, col, div, embed, h1, h2, h3, h4, h5, h6, hr, iframe, img, input, legend,
                                    object_tag, p, table, tbody, ], 'accept': [form], 'allowtransparency': [iframe],
                          'archive': [object_tag], 'axis': [th, td],
                          'background': [body, table, thead, tbody, tfoot, tr, td, th],
                          'bgcolor': [body, table, td, th, tr], 'border': [object_tag], 'bordercolor': [table],
                          'cellpadding': [table], 'cellspacing': [table],
                          'char': [col, tbody, thead, tfoot, td, th, tr],
                          'charoff': [col, tbody, thead, tfoot, td, th, tr], 'charset': [a, link],
                          'classid': [object_tag],
                          'clear': [br], 'code': [object_tag], 'codebase': [object_tag], 'codetype': [object_tag],
                          'coords': [a],
                          'datafld': [a, applet, button, div, fieldset, frame, iframe, img, input, label,
                                      legend, marquee, object_tag, param, select, span, textarea],
                          'dataformatas': [button, div, input, label, legend, marquee, object_tag, option, select, span,
                                           table], 'datapagesize': [table],
                          'datasrc': [a, applet, button, div, frame, iframe, img, input, label, legend, marquee,
                                      object_tag,
                                      option, select, span, table, textarea], 'declare': [script], 'for': [script],
                          'frame': [script], 'frameborder': [iframe], 'height': [th, td],
                          'hspace': [embed, iframe, img, input, object_tag], 'ismap': [input], 'langauge': [script],
                          'link': [body], 'lowsrc': [img], 'marginbottom': [body], 'marginheight': [body, iframe],
                          'marginleft': [body], 'marginrigth': [body], 'margintop': [body], 'marginwidth': [body],
                          'methods': [a, link], 'name': [a, embed, img, option], 'nohref': [area], 'noshade': [hr],
                          'nowrap': [head], 'rules': [table], 'scheme': [meta], 'scope': [id_tag], 'scrolling': [iframe],
                          'shape': [a], 'size': [hr], 'standby': [object_tag], 'summary': [table], 'text': [body],
                          'type': [li, param, ul], 'urn': [a, link], 'usemap': [input],
                          'valign': [col, tbody, thead, tfoot, td, th, tr], 'valuetype': [param], 'version': [html],
                          'vlink': [body], 'vspace': [ol, hr, pre, table, td, th],
                          }
        print(type(attribute_dict))
        for key, tags in attribute_dict.items():

            for tag in tags:
                for el in self.driver.find_elements_by_tag_name(tag):
                    val = el.get_attribute(key)
                    assert val is None or val is "", 'deprecated attribute usage, tag ' + tag + " attr " + key
        #
        print('test 1827 passed')
