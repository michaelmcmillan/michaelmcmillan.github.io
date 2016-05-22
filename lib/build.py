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
    def headline(self):
        return '%s - %s' % (self.date.strftime('%d-%m-%Y'), self.title)

    def format(self):
        return '%s\n\n%s\n\n' % (self.headline, self.content)

    @property
    def excerpt(self):
        return self.content[:256] + ' ...'

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
            if post_filename.startswith('draft') == False]

class Blog:

    def __init__(self, posts):
        self.posts = posts
        self.sort_posts_by_date()

    def sort_posts_by_date(self):
        self.posts.sort(key=lambda post: post.date, reverse=True)

    def compile(self, header, footer):
        header, body, footer = (get_file(header), '', get_file(footer))
        body += '<pre>\n'
        for index, post in enumerate(self.posts):
            body += self.indent(post.format()) \
                if index > 0 else \
                '    ' + self.indent(post.format())
        body += '</pre>\n'
        return (header + body + footer)

    @staticmethod
    def indent(text, spaces=4):
        spacer = ' ' * spaces
        return text.replace('\n', '\n' + spacer)

class RSSFeed(Blog):

    def compile(self, header, footer):
        header, body, footer = (get_file(header), '', get_file(footer))
        for post in self.posts:
            body += '<item>\n'
            body += self.indent('<title>%s</title>\n' % post.title)
            body += self.indent('<description>\n%s\n</description>' % post.excerpt)
            body += '\n</item>\n\n'
        return (header + body + footer)

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
            flags['templates_directory'] + '/blog_header.html',
            flags['templates_directory'] + '/blog_footer.html'
        ))
    elif flags['format'] == 'feed':
        print(rss_feed.compile(
            flags['templates_directory'] +'/feed_header.xml',
            flags['templates_directory'] + '/feed_footer.xml'
        ))
