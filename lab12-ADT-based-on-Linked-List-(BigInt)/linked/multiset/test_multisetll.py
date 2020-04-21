from multisetll import Multiset


if __name__ == '__main__':
    multy = Multiset()
    multy.add(1)
    multy.add(2)
    multy.add(3)
    multy.add(4)
    multy.add(5)
    multy.add(6)

    first, second = multy.split_half()
    print(first.remove_all())
    print(second.remove_all())

    multy2 = Multiset()
    multy2.add(1)
    multy2.add(2)
    multy2.add(3)
    multy2.add(4)
    multy2.add(5)
    multy2.add(6)
    multy2.add(7)
    print(multy2.remove_all())