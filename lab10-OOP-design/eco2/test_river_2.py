from river_2 import River


if __name__ == '__main__':
    # one year update
    river1 = River(10)
    print('start:', river1)
    river1.update_river()
    print('result:', river1)
    print('Bears:', river1.number_animal("Bear"))
    print('Fish:', river1.number_animal("Fish"))
