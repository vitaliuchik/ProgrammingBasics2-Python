from vigenere_cipher import *
import unittest


class TestVigenere(unittest.TestCase):
    def setUp(self):
        self.cipher = VigenereCipher("TRAIN")
        self.cipher_low = VigenereCipher("TRain")

    def test_encode(self):
        self.assertEqual(self.cipher.encode("E"), "X")
        self.assertEqual(self.cipher.encode(
            "ENCODEDINPYTHON"), "XECWQXUIVCRKHWA")
        self.assertEqual(self.cipher.encode(
            "ENCODED IN PYTHON"), "XECWQXUIVCRKHWA")
        self.assertEqual(self.cipher_low.encode(
            "encoded in python"), "XECWQXUIVCRKHWA")

    def test_decode(self):
        self.assertEqual(self.cipher.decode(
            "XECWQXUIVCRKHWA"), "ENCODEDINPYTHON")

    def test_combine_character(self):
        self.assertEqual(combine_character("E", "T"), "X")
        self.assertEqual(combine_character("N", "R"), "E")

    def test_separate_character(self):
        self.assertEqual(separate_character("X", "T"), "E")
        self.assertEqual(separate_character("E", "R"), "N")

    def test_extend_keyword(self):
        self.assertEqual(self.cipher.extend_keyword(16), "TRAINTRAINTRAINT")


if __name__ == '__main__':
    unittest.main()