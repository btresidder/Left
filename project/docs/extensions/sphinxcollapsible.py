from docutils import nodes
from docutils.parsers.rst import Directive

class Collapsible(Directive):

    def run(self):
        paragraph_node = nodes.paragraph(text='</p><h1>hello world<h1><p>')
        html_node = """<b>This Worked</b>"""
        self.body.append(html_node)
        return [paragraph_node]

def setup(app):
    app.add_directive("collapsible", Collapsible)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
