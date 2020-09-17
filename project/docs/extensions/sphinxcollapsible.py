from docutils import nodes
from docutils.parsers.rst import Directive

# Needed to run the visit and depart methods
# No idea why this class has to exist but its how sphinx works
class b(nodes.Structural, nodes.Element):
    pass

# The main class
class Collapsible(Directive):
    # Directives.unchanged means u get raw value from the rst
    option_spec = {'title': directives.unchanged}
    
    def run(self):
        # Needed to get access to options
        options = self.options
        
        # Creates the class to call the other methods
        html_node = b()
        return [html_node]

# Visit and depart methods come as a pair
# Visit is not actually used in this case
def visit_collapsible_html(self, node):
    pass

# Creates the collapsible
def depart_collapsible_html(self, node):
    # The title is represented in <summary> tags
    code = """<details><summary><b>"""
    code += options["title"]
    code += """</b></summary>"""
    
    # The content of the collapsible goes after the </summary>
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
