from docutils import nodes
from docutils.parsers.rst import Directive

class b(nodes.Structural, nodes.Element):
    pass

class Collapsible(Directive):
    def run(self):
        html_node = b()
        return [html_node]

def visit_collapsible_html(self, node):
    pass

def depart_collapsible_html(self, node):
    code = """<details><summary><b>"""
    code += """Dropdown Title"""
    code += """</b></summary>"""
    
    code += """<p>here is some text</p>"""
    code += """</details>"""
    self.body.append(code)


def setup(app):
    app.add_directive("collapsible", Collapsible)
    app.add_node(b, html=(visit_collapsible_html, depart_collapsible_html))

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
