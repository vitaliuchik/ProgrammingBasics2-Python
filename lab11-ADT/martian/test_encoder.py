from encoder import Encoder


if __name__ == '__main__':
    hello = Encoder('Hello')
    print(hello)
    print('Number of angles:', len(hello))
    # 8-9 indexes = 'o' = '6f' in hex
    print('10th angle:', hello[9])