from urllib.request import urlopen 
import time

class WebPage:
    """Cashin webpage"""
    def __init__(self, url):
        """Initializes web-page by url"""
        self.url = url
        self._content = None
        self.last_update = time.time()

    @property
    def content(self):
        """Return content of web-page"""
        
        # reloads page every 10 sec
        reload_time = 10
        now = time.time()
        if not self._content or (now - self.last_update > reload_time):
            print("Retrieving New Page...")
            self._content = urlopen(self.url).read()
            self.last_update = time.time()
        else:
            print("Hasn't reloaded yet.")
        return self._content







# super().__init__(filename)
# self.search ...