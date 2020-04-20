from PIL import Image
from zip_processor import ZipProcessor



class ScaleZip():
    """Represents process of changing image extension"""
    def __init__(self, zipname, extension):
        self.process = ZipProcessor(zipname)
        self.extension = extension

    def process_files(self):
        """Changes images extension"""
        for filename in self.process.temp_directory.iterdir():
            img = Image.open(str(filename))
            scaled = img.resize(self.extension)
            scaled.save(str(filename))

    def process_zip(self):
        """Run process"""
        self.process.unzip_files()
        self.process_files()
        self.process.zip_files()

