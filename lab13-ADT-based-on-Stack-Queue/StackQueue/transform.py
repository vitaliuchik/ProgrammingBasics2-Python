from arraystack import ArrayStack
from arrayqueue import ArrayQueue
import copy

def stackToQueue(stack):
    stack_copy = copy.deepcopy(stack)
    queue = ArrayQueue()
    while True:
        try:
            queue.add(stack_copy.pop())
        except KeyError:
            break
    return queue
    

def queueToStack(queue):
    queue_copy = copy.deepcopy(queue)
    stack = ArrayStack()
    while True:
        try:
            stack.add(queue_copy.pop())
        except KeyError:
            break
    return stack


if __name__ == '__main__':
    queue = stackToQueue(ArrayStack('abcde'))
    print('Deleting elements from queue:', end=' ')
    while True:
        try:
            print(queue.pop(), end=' ')
        except KeyError:
            break

    stack = queueToStack(ArrayQueue('12345'))
    print('\nDeleting elements from stack:', end=' ')
    while True:
        try:
            print(stack.pop(), end=' ')
        except KeyError:
            break