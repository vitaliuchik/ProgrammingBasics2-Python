import unittest

class TestMachine(unittest.TestCase):
    def setUp(self):
        self.tm1 = TextMachine((75, 125), (25, 245))

    def test_str(self):
        self.assertEqual(str(tm1), "Text Machine:<75 texts; ₴1.25 each>; "
                        "<25 texts; ₴2.45 each>""")

    def test_is_empty(self):
        self.assertEqual(tm1.is_empty(), False)

    def test_still_owe(self):
        self.assertEqual(tm1.still_owe(), (125, 245))

    def test_insert_money(self):
        self.assertEqual(tm1.insert_money((20, 'short')),\
             ("Still owe ₴1.05", 20))
        self.assertEqual(tm1.insert_money((5, 'short')),\
             ("Still owe ₴1.00", 25))


if __name__ == "__main__":
    unittest.main()