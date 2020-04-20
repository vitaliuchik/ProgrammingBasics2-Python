import unittest
from all_prefixes import all_prefixes

class TestPrefixes(unittest.TestCase):
    def test_prefixes1(self):
        self.assertEqual(all_prefixes('matan'), \
            {'m', 'ma', 'mat', 'mata', 'matan'})
    
    def test_prefixes2(self):
        self.assertEqual(all_prefixes('maman'), \
            {'m', 'ma', 'mam', 'mama', 'maman', 'man'})

    def test_prefixes3(self):
        avangard = {'ава', 'ан', 'авангард', 'ангар', 'ангард', \
            'ав', 'аванга', 'анга', 'анг', 'ар', 'авангар', 'аванг', \
            'а', 'аван', 'ард'}
        self.assertEqual(all_prefixes('авангард'), avangard)

    def test_prefixes4(self):
        self.assertEqual(all_prefixes('!fh!-'), \
            {'!', '!f', '!fh', '!fh!', '!fh!-', '!-'})



if __name__ == '__main__':
    unittest.main()