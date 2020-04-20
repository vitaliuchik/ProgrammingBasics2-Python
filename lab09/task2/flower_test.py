from flower import Flower, Tulip, Rose, Chamomile, FlowerSet, Bucket

def test_flower():
    print('Testing flower class')
    fl = Tulip('green', 14, 100)
    assert(fl.getColor() == 'green')
    assert(fl.getPetalNum() == 14 )
    assert(fl.getPrice() == 100)

    f2 = Tulip('red', 14, 100)
    f3 = Tulip("green", 14, 100)
    assert(f2 != f3)
    assert(fl == f3)
    assert(isinstance(f2, Flower))
    assert(f2.getType() == 'Tulip')
    f4 = Chamomile(17, 160)
    f5 = Chamomile(18,160)

    assert(f4.lovesMe() == True)
    assert(f5.lovesMe() == False)
    assert(f4.getColor() == 'white')

    f_set = FlowerSet([fl, f2, f3, f4, f5])
    assert(f_set.getPrice() == 620)
    assert(f_set.getColors() == {'white', 'green', 'red'})

    f_set1 = FlowerSet([fl, f2])

    bckt = Bucket([f_set, f_set1])
    assert(bckt.getPrice() == 820)
    print('done')

test_flower()





