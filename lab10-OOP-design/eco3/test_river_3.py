from river_3 import River


if __name__ == '__main__':
    # print enter to update one year
    river1 = River(100)
    print('start:', river1, '\n')

    k = 0
    while True:
        k += 1 
        river1.update_river()
        print('\nresult:', river1)
        print('Bears:', river1.number_animal("Bear"))
        print('Fish:', river1.number_animal("Fish"))
        print('Otters:', river1.number_animal("Otter"))
        print('Years: ', k)
        input()
