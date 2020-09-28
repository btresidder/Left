import sphinx
from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst import directives
from sphinx.builders import latex

options = [] # Stores titles
index = 0    # Counter for titles list

# Class represents the node used to start the <details> tag
class start(nodes.Structural, nodes.Element):
    pass

# Class represents the node used to end the <details> tag
class finish(nodes.Structural, nodes.Element):
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
        options.append(self.options['title'])
        
        # This is the content of the collapsible
        # nested_parse needed so other directives can be inside the collapsible
        par = nodes.paragraph()
        self.state.nested_parse(self.content, self.content_offset, par)
        
        # Creates the classes to call the other methods
        html_node = start()
        html_node += par
        html_node += finish()
        
        return [html_node]

# Visit and depart methods come as pairs
# Visit creates the collapsible
# The <details> tag is left open so rst (including directives) can be inserted
def visit_collapsible_html(self, node):

    global index
    
    # Collapsible is made with <details> tags
    # The title is represented in <summary> tags
    code = """<details style="margin:0 0 24px 25px;"><summary style="margin:0 0 0 -20px;"><b>"""
    code += options[index]
    code += """</b></summary>"""
    
    index += 1
    
    self.body.append(code)

def depart_collapsible_html(self, node):
    pass

def visit_col_html(self, node):
    pass

# Closes the <details> tag after rst has been inserted
def depart_col_html(self, node):
    code = """</details>"""
    self.body.append(code) 
    
def build_type(app):
    print("builder is: ")
    print(app.builder)
    print("builder type is: ")
    print(type(app.builder))
    print("object type is: ")
    print(type(sphinx.builders.latex.LaTeXBuilders))
    if type(app.builder) == type(sphinx.builders.latex.LaTeXBuilder):
        print ("this is latex")
    print("done")

# Setups up directives and nodes
def setup(app):
    app.add_directive("collapsible", Collapsible)
    app.add_node(start, html=(visit_collapsible_html, depart_collapsible_html))
    app.add_node(finish, html=(visit_col_html, depart_col_html))
    app.connect('builder-inited', build_type)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
