from os import walk
from sys import argv
from datetime import datetime
directories = {'posts': argv[1], 'templates': argv[2]}

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

class Archive:

    def __init__(self, directory):
        self.directory = directory

    def get_files_in_directory(self):
        for root, directories, files in walk(self.directory):
            return files

    def extract_post_from_filename(self, filename):
        title = filename[11:-5].replace('_', ' ')
        date = datetime.strptime(filename[:10], '%d-%m-%Y') 
        content = get_file(self.directory + '/' + filename)
        return Post(title, date, content)

    def get_posts(self):
        return [self.extract_post_from_filename(post_filename) \
            for post_filename in self.get_files_in_directory()]

class Blog:

    def __init__(self, posts):
        self.posts = posts

    def sort_posts_by_date(self):
        self.posts.sort(key=lambda post: post.date, reverse=True)

    def compile(self, header, footer):
        header, footer = (get_file(header), get_file(footer))
        body = '<pre>' + ''.join([post.format() for post in self.posts]) + '</pre>'
        return (header + body + footer)

archive = Archive(directories['posts'])
posts = archive.get_posts()
blog = Blog(posts)
blog.sort_posts_by_date()
print(blog.compile(directories['templates'] + '/header.html', directories['templates'] + '/footer.html'))
