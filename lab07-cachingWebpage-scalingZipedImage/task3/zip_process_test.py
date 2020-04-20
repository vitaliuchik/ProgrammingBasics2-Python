from scale_zip import ScaleZip
from zip_replace import ZipReplace

if __name__ == '__main__':
    zip_name = str(input('Input file name (exp. images.zip): '))
    extension = tuple(map(int, str(input('Input extension (like this "640,480"): ')).split(',')))

    # my example!
    # zip_name = 'images.zip'
    # extension = (720, 180)

    ScaleZip(zip_name, extension).process_zip()

    ###############################################################

    ZipReplace('file.zip', 'father', 'changed_word').process_zip()
