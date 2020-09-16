class News:
    '''
    News class to define News objects
    '''

    def __init__(self,title,description,publishedAt,content,url,urlToImage):
        self.title = title
        self.description = description
        self.publishedAt = publishedAt
        self.content = content
        self.url = url
        self.urlToImage = urlToImage