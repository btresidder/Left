from docutils import nodes
from docutils.parsers.rst import Directive

class b(nodes.Structural, nodes.Element):
    pass

class Collapsible(Directive):

    def run(self):
        #html_node = nodes.raw(text='''<b>hello world</b>''')
        
        #html_node = """<b>This Worked</b>"""
        #self.body.append(html_node)
        
        html_node = b()
        
        return [html_node]

def visit_collapsible_html(self, node):
    #self.body.append(self.starttag(node, 'b'))
    pass

def depart_collapsible_html(self, node):
    #self.body.append('test</b>')
    code = """<b>hello world</b>"""
    self.body.append(code)


def setup(app):
    app.add_directive("collapsible", Collapsible)
    app.add_node(b, html=(visit_collapsible_html, depart_collapsible_html))

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
