class Source:
    '''
    Sources class to define Sources Objects
    '''

    def __init__(self, id, name, description, url):
        self.id = id
        self.name = name
        self.description = description
        self.url = url


class Article():
    def __init__(self, source, author, title, description, url, urlToImage, publishedAt, content):
        self.source = source
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
