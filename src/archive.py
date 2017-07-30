from os import walk
from datetime import datetime
from post import Post
from file_reader import get_file

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
