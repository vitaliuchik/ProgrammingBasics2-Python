import random
import time
from linkedbst import LinkedBST


if __name__ == '__main__':
    f = open('words.txt')
    lines = f.readlines()
    f.close()

    words = []
    for i in range(10000):
        words.append(random.choice(lines)[:-1])

    # list testing
    start = time.time()
    for word in words:
        _ = words.index(word)
    finish = time.time()
    print(finish - start, 'sec')

    # binary tree testing
    # here you should change the recurssion limit to implement dictionary in tree
    # or you can change the size of the "lines"(зрізати) and choosed words 
    tree = LinkedBST()
    for line in lines:
        tree.add(line[:-1])

    start = time.time()
    for word in words:
        _ = tree.find(word)
    finish = time.time()
    print(finish - start, 'sec')

    # balansed binary tree testing
    tree.rebalance()

    start = time.time()
    for word in words:
        _ = tree.find(word)
    finish = time.time()
    print(finish - start, 'sec')
    