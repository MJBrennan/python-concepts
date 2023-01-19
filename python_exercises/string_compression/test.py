import unittest
import main.py


class TestStringCompression(unittest.TestCase):
    def test_string_compression(self):
        s = "aabcccccaaa"
        result = string_compression(s)
        self.assertEqual(result, "a2b1c5a3")

    def test_string_compression_original_string(self):
        s = "abcdefgh"
        result = string_compression(s)
        self.assertEqual(result, "abcdefgh")

    def test_string_compression_with_space_and_special_chars(self):
        s = "abcdefgh!@#"
        result = string_compression(s)
        self.assertEqual(result, "abcdefgh!@#")


if __name__ == '__main__':
    unittest.main()
