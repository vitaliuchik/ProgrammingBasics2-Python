import zipfile
from zip_processor import ZipProcessor

class ZipReplace():
    """Represents process of changing file's text"""
    def __init__(self, filename, search_string, replace_string):
        self.process = ZipProcessor(filename)
        self.search_string = search_string
        self.replace_string = replace_string

    def process_files(self):
        """Changes file's text"""
        for filename in self.process.temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()
            contents = contents.replace(
                self.search_string, self.replace_string)
            with filename.open("w") as file:
                file.write(contents)

    def process_zip(self):
        """Run process"""
        self.process.unzip_files()
        self.process_files()
        self.process.zip_files()