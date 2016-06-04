from sys import argv
from blog import Blog
from rss_feed import RSSFeed
from archive import Archive

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
            flags['templates_directory'] + '/blog/sidebar.html',
            flags['templates_directory'] + '/blog/footer.html'
        ))
    elif flags['format'] == 'feed':
        print(rss_feed.compile(
            flags['templates_directory'] + '/feed/header.xml',
            flags['templates_directory'] + '/feed/item.xml',
            flags['templates_directory'] + '/feed/footer.xml'
        ))
    else:
        print('Format is not provided.')
