from template import Template
from merger import merge

class Blog:

    def __init__(self, posts):
        self.posts = posts
        self.sort_posts_by_date()

    def sort_posts_by_date(self):
        self.posts.sort(key=lambda post: post.date, reverse=True)

    def compile(self, header, body, sidebar, footer):
        header, body, sidebar, footer = (Template(header), Template(body), Template(sidebar), Template(footer))
        compiled = ''
        for post in self.posts:
            compiled += body.compile({
                'title': post.title,
                'date': post.pretty_date,
                'content': self.indent(post.content)
            })
        compiled = merge(compiled, sidebar.compile(), 120)
        return (header.compile() + compiled + footer.compile())

    @staticmethod
    def indent(text, spaces=4):
        spacer = ' ' * spaces
        return text.replace('\n', '\n' + spacer)
