from docutils.parsers.rst import directives, Directive
from docutils import nodes

class EndSummary(Directive):
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = True

    def run(self):
        attributes = {'format': 'html'}
        encoding = self.options.get('encoding', self.state
                                                    .document
                                                    .settings
                                                    .input_encoding)
        raw_node = nodes.raw('', '<!-- PELICAN_END_SUMMARY -->', **attributes)
        return [raw_node]

def register():
    directives.register_directive('end-summary', EndSummary)
