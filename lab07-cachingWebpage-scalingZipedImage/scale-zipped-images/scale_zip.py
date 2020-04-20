import shutil
import zipfile
from pathlib import Path
from PIL import Image


class ZipProcessor:
    """Represents process of zipping and unzipping"""

    def __init__(self, zipname, extension):
        """Initializes variable"""
        self.extension = extension
        self.zipname = zipname
        self.temp_directory = Path("unzipped-{}".format(zipname[:-4]))

    def process_zip(self):
        """Run process"""
        self.unzip_files()
        self.process_files()
        self.zip_files()

    def unzip_files(self):
        """Unzip files"""
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.zipname) as zp:
            zp.extractall(str(self.temp_directory))

    def zip_files(self):
        """Zip files"""
        with zipfile.ZipFile(self.zipname, 'w') as file:
            for filename in self.temp_directory.iterdir():
                file.write(str(filename), filename.name)
        shutil.rmtree(str(self.temp_directory))


class ScaleZip(ZipProcessor):
    """Represents process of changing image extension"""

    def process_files(self):
        """Changes images extension"""
        for filename in self.temp_directory.iterdir():
            img = Image.open(str(filename))
            scaled = img.resize(self.extension)
            scaled.save(str(filename))


