from template import Template
class Blog:

    def __init__(self, posts):
        self.posts = posts
        self.sort_posts_by_date()

    def sort_posts_by_date(self):
        self.posts.sort(key=lambda post: post.date, reverse=True)

    def compile(self, header, body, footer):
        header, body, footer = (Template(header), Template(body), Template(footer))
        compiled = ''
        for post in self.posts:
            compiled += body.compile({
                'title': post.title,
                'date': post.pretty_date,
                'content': self.indent(post.content)
            })
        return (header.compile() + compiled + footer.compile())

    @staticmethod
    def indent(text, spaces=4):
        spacer = ' ' * spaces
        return text.replace('\n', '\n' + spacer)
