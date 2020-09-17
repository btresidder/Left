from docutils import nodes
from docutils.parsers.rst import Directive

class useless():
    pass

class Collapsible(Directive):

    def run(self):
        paragraph_node = nodes.paragraph(text='</p><h1>hello world<h1><p>')
        #html_node = """<b>This Worked</b>"""
        #self.body.append(html_node)
        return [paragraph_node]

def visit_collapsible_html(self, node):
    self.body.append(self.starttag(node, 'b'))
def depart_collapsible_html(self, node):
    self.body.append('test</b>')

def setup(app):
    app.add_directive("collapsible", Collapsible)
    app.add_node(useless, html=(visit_collapsible_html, depart_collapsible_html))

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
