from blog import Blog
from template import Template

class RSSFeed(Blog):

    def compile(self, header, body, footer):
        header, body, footer = (Template(header), Template(body), Template(footer))
        compiled = ''
        for post in self.posts:
            compiled += body.compile({
                'title': post.title,
                'description': post.excerpt
            })
        return (header.compile() + compiled + footer.compile())
