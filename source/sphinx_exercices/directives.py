from docutils import nodes
from docutils.parsers.rst import directives
from .utils import ExerciceNumbering

class ExerciceDirective(Directive):
    has_content = True

    def run(self):
        numbering = self.state.document.settings.env.temp_data.setdefault('exercice_numbering', ExerciceNumbering())
        number = numbering.get_next_exercice_number()

        # Insérer le contenu de l'exercice avec le numéro
        content = '\n'.join(self.content)
        node = exercice(content)
        node += nodes.title(f'Exercice {number}', f'Exercice {number}')
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]

class exercice(nodes.Admonition, nodes.Element):
    pass

def visit_exercice_node(self, node):
    self.visit_admonition(node)

def depart_exercice_node(self, node):
    self.depart_admonition(node)

def setup(app):
    app.add_node(exercice, html=(visit_exercice_node, depart_exercice_node))
    app.add_directive('exercice', ExerciceDirective)
    return {'version': '0.1'}
