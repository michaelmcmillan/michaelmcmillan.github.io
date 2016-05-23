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
