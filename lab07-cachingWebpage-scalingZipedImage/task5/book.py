class Book:

    def __init__(self, title, author, pages):
        self.title = title
        self.author= author
        self.pages = pages
        self.page = 1
        self.bookmarked = None

    def __str__(self):
        page_str = 'pages'
        if self.pages == 1:
            page_str = 'page'
        bookmark_str = str(self.page)
        if self.bookmarked:
            bookmark_str += ', page {} bookmarked'.format(self.bookmarked)
        return "Book<{} by {}: {} {}, currently on page {}>".format(self.title, \
            self.author, str(self.pages), page_str, bookmark_str)

    def getCurrentPage(self):
        return self.page

    def turnPage(self, page):
        self.page += page
        if self.page > self.pages:
            self.page = self.pages
        elif self.page < 1:
            self.page = 1

    def placeBookmark(self):
        self.bookmarked = self.page

    def removeBookmark(self):
        self.bookmarked = None

    def turnToBookmark(self):
        if self.bookmarked:
            self.page = self.bookmarked

    def getBookmarkedPage(self):
        return self.bookmarked

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and \
            self.pages == other.pages and self.page == other.page and \
            self.bookmarked == other.bookmarked

    def __ne__(self, other):
        return self.title != other.title or self.author != other.author or \
            self.pages != other.pages or self.page != other.page or \
            self.bookmarked != other.bookmarked
