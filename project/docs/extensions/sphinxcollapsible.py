from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives

# Class represents the node used to start the <details> tag
class b(nodes.Structural, nodes.Element):
    pass

# Class represents the node used to end the <details> tag
class c(nodes.Structural, nodes.Element):
    pass

# The main class
class Collapsible(Directive):

    # Gets content from the directive
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {'title': directives.unchanged,}
    has_content = True
    add_index = True
    
    def run(self):
        
        # Needed to get access to options
        global options
        options = self.options
        
        # This is the content of the collapsible
        # nested_parse needed so other directives can be inside the collapsible
        par = nodes.paragraph()
        self.state.nested_parse(self.content, self.content_offset, par)
        
        # Creates the classes to call the other methods
        html_node = b()
        html_node += par
        html_node += c()
        
        return [html_node]

# Visit and depart methods come as pairs
# Visit creates the collapsible
# The <details> tag is left open so rst (including directives) can be inserted
def visit_collapsible_html(self, node):

    # Collapsible is made with <details> tags
    # The title is represented in <summary> tags
    code = """<details style="margin:0 0 24px 25px;"><summary style="margin:0 0 0 -20px;"><b>"""
    code += options["title"]
    code += """</b></summary>"""
    self.body.append(code)

def depart_collapsible_html(self, node):
    pass

def visit_col_html(self, node):
    pass

# Closes the <details> tag after rst has been inserted
def depart_col_html(self, node):
    code = """</details>"""
    self.body.append(code) 

# Setups up directives and nodes
def setup(app):
    app.add_directive("collapsible", Collapsible)
    app.add_node(b, html=(visit_collapsible_html, depart_collapsible_html))
    app.add_node(c, html=(visit_col_html, depart_col_html))

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
