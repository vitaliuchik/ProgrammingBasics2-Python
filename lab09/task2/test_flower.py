import unittest
from flower import Flower, Tulip, Rose, Chamomile, FlowerSet, Bucket

class TestFlower(unittest.TestCase):
    def setUp(self):
        self.f1 = Tulip("Pink", 14, 100)
        self.f2 = Rose("White", 27, 200)
        self.f3 = Chamomile(26, 50)
        self.f4 = Chamomile(25, 50)

    def test_color(self):
        self.assertEqual(self.f1.getColor(), "Pink")
        self.assertEqual(self.f2.getColor(), "White")
        self.assertEqual(self.f3.getColor(), "White")
        self.assertEqual(self.f4.getColor(), "White")
        
    def test_price(self):
        self.assertEqual(self.f1.getPrice(), 100)
        self.assertEqual(self.f2.getPrice(), 200)
        self.assertEqual(self.f3.getPrice(), 50)
        self.assertEqual(self.f4.getPrice(), 50)
        
    def test_petal_num(self):
        self.assertEqual(self.f1.getPetals(), 14)
        self.assertEqual(self.f2.getPetals(), 27)
        self.assertEqual(self.f3.getPetals(), 26)
        self.assertEqual(self.f4.getPetals(), 25)


class TestChamomile(unittest.TestCase):
    def setUp(self):
        self.f1 = Chamomile(26, 50)
        self.f2 = Chamomile(25, 50)
    
    def test_loves_me(self):
        self.assertFalse(self.f1.lovesMe())
        self.assertTrue(self.f2.lovesMe())

class TestFlowerSet(unittest.TestCase):
    def sutUp(self):
        self.f1 = Tulip("Pink", 14, 100)
        self.f2 = Rose("White", 27, 200)
        self.f3 = Chamomile(26, 50)
        self.f4 = Chamomile(25, 50)
        f_set = FlowerSet([f1, f2, f3, f4])
    
    def test_flowers(self):
        self.assertEqual(self.f_set.getFlowers() == {f1, f2, f3, f4})
        
    def test_colors(self):
        self.assertEqual(self.f_set.getColors() == {"Pink", "White"})
        
    def test_price(self):
        self.assertEqual(self.f_set.getPrice() == 400)
        
class TestBucket(unittest.TestCase):
    def setUp(self):
        self.f1 = Tulip("Pink", 14, 100)
        self.f2 = Rose("White", 27, 200)
        self.f3 = Chamomile(26, 50)
        self.f4 = Chamomile(25, 50)
        f_set1 = FlowerSet([f1, f2, f3, f4])

        self.f5 = Rose("Red", 27, 200)
        self.f6 = Chamomile(17, 50)
        f_set2 = TestFlowerSet([f5, f6])

    def test_price(self): 
        self.assertEqual(self.f_set1.getPrice() == 400)
        self.assertEqual(self.f_set2.getPrice() == 250)