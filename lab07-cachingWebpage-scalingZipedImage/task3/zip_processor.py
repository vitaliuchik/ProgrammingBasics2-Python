import shutil
import zipfile
from pathlib import Path

class ZipProcessor:
    """Represents process of zipping and unzipping"""

    def __init__(self, zipname):
        """Initializes variable"""
        self.zipname = zipname
        self.temp_directory = Path("unzipped-{}".format(zipname[:-4]))

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