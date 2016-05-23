from file_reader import get_file

class Template:

    def __init__(self, template):
        self.template = get_file(template)

    def compile(self, variables=None):
        variables = variables or []
        template = self.template
        for key in variables:
            value = variables[key]
            template = template.replace('{{ %s }}' % key, value)
        return template
