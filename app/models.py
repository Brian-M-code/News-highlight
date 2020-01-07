class Article:
    """
    Creating class for the news article
    """
    def __init__(self, author, title, description, url, img, date, content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.img = img
        self.date = date
        self.content = content

class Source:
    """
    Creating class for the news source
    """
    def __init__(self, id, name):
        self.id = id
        self.name = name