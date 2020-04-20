class MyException(Exception):
    pass
def f1(x, y):
    try:
        f2(x)
    except MyException:
        print("Some useful info from f1")

def f2(y):
    try:
        f3()
    except MyException:
        print ("Some useful info from f2")
        raise MyException

def f3():
    print("Some useful info from f3")
    raise

f1(1,2)