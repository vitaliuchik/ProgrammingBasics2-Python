from grayscaleimage import GrayscaleImage
from collections import Counter
import random


def fano_rec(fano, keys, freq):
    """Fano encoding (help function for encode())
    (dict, list, list) -> None"""
    ind = 0
    while sum(freq[:ind]) < sum(freq[ind:]):
        ind += 1

    for key in keys[:ind]:
        fano[key] = fano.get(key, '')
        fano[key] += '0'
    for key in keys[ind:]:
        fano[key] = fano.get(key, '')
        fano[key] += '1'
    if ind not in [0, 1]:
        fano_rec(fano, keys[:ind], freq[:ind])
    if (len(keys) - ind) not in [0, 1]:
        fano_rec(fano, keys[ind:], freq[ind:])


def encode(img):
    """Encodes n_row image to n integers uses fano algorithm.
    Encodes each value of image and for each row makes one integer,
    joining '1' at the begining and fano code of each value from the row
    and then transforming recieved binary to integer.

    (GrayscaleImage) -> (list, dict)"""

    lst_2D = [[img[row, col] for col in range(img.width())] for row in range(img.height())]
    lst_1D = [img[row, col] for col in range(img.width()) for row in range(img.height())]
    counter = dict(Counter(lst_1D))
    items = list(counter.items())
    items.sort(key=lambda x: x[1], reverse=True)
    keys = []
    freq = []
    for item in items:
        keys.append(item[0])
        freq.append(item[1])
    
    fano = dict()
    fano_rec(fano, keys, freq)

    encoded = []
    for row in lst_2D:
        result = '0b1'
        for el in row:
            result += fano[el]
        encoded.append(int(result, 2))
    return (encoded, fano)


def decode(encoded, fano):
    """Decodes image using fano algorithm.

    (list, dict) -> GrayscaleImage"""

    encoded = list(map(lambda x: bin(x)[3:], encoded))
    fano_reversed = {value: key for (key, value) in fano.items()}
    decoded = []
    for binary in encoded:
        row = []
        s = ''
        i = 1
        while binary != '':
            s = binary[:i]
            if s in list(fano_reversed.keys()):
                row.append(fano_reversed[s])
                s = ''
                binary = binary[i:]
                i = 1
            else:
                i += 1
        decoded.append(row)
    
    try:
        img = GrayscaleImage(len(decoded), len(decoded[0]))
    except IndexError:
        img = GrayscaleImage(0, 0)
    for row in range(img.height()):
        for col in range(img.width()):
            img[row, col] = decoded[row][col]
    return img

    

if __name__ == '__main__':
    img = GrayscaleImage(6, 4)
    for row in range(img.height()):
        for col in range(img.width()):
            img[row, col] = random.randint(0, 255)

    print("First image:")
    print(img)

    encoded, fano = encode(img)
    print("\nEncoded rows to integers:")
    print(encoded)
    print("\nFano code of intensity of each cell:")
    print(fano)

    decoded_img = decode(encoded, fano)
    print("\nDecoded image")
    print(decoded_img)
        
