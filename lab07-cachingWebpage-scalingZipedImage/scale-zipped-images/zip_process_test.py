import scale_zip

if __name__ == '__main__':
    zip_name = str(input('Input file name (zip): '))
    extension = tuple(map(int, str(input('Input extension (like this "640,480"): ')).split(',')))

    # my example!
    # zip_name = 'images.zip'
    # extension = '480,1080'

    scale_zip.ScaleZip(zip_name, extension).process_zip()