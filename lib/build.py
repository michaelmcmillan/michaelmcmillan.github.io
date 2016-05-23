from os import walk
from sys import argv
from datetime import datetime

def get_file(path):
    with open(path, 'r') as data:
        return data.read()

class Post:

    def __init__(self, title, date, content):
        self.date = date
        self.title = title
        self.content = content

    @property
    def pretty_date(self):
        return self.date.strftime('%d-%m-%Y')

    @property
    def excerpt(self):
        return self.content[:256] + ' ...'

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

class Archive:

    def __init__(self, directory):
        self.directory = directory

    def get_files_in_directory(self):
        for root, directories, files in walk(self.directory):
            return files

    def extract_post_from_filename(self, filename):
        title = filename[11:].replace('_', ' ')
        date = datetime.strptime(filename[:10], '%Y-%m-%d') 
        content = get_file(self.directory + '/' + filename)
        return Post(title, date, content)

    def get_posts(self):
        return [self.extract_post_from_filename(post_filename) \
            for post_filename in self.get_files_in_directory() \
            if not post_filename.startswith('draft')]

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

if __name__ == '__main__':

    flags = {
        'format': argv[1],
        'posts_directory': argv[2],
        'templates_directory': argv[3]
    }

    posts = Archive(flags['posts_directory']).get_posts()
    blog, rss_feed = (Blog(posts), RSSFeed(posts))

    if flags['format'] == 'blog':
        print(blog.compile(
            flags['templates_directory'] + '/blog/header.html',
            flags['templates_directory'] + '/blog/post.html',
            flags['templates_directory'] + '/blog/footer.html'
        ))
    elif flags['format'] == 'feed':
        print(rss_feed.compile(
            flags['templates_directory'] + '/feed/header.xml',
            flags['templates_directory'] + '/feed/item.xml',
            flags['templates_directory'] + '/feed/footer.xml'
        ))
