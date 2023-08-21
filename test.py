import unittest
import word_test

class TestWordPrefix(unittest.TestCase):
    def test_prefix(self):
        prefix ="pre"
        word = "preparation"
        result = prefix in word
        self.assertTrue(result)

    def test_prefix2(self):
        prefix = "pro"
        word = "primer"
        result = prefix in word
        self.assertFalse(result)

    def test_prefix3(self):
        prefix = "pro"
        word = "provocation"
        result = prefix in word
        self.assertTrue(result)


if __name__ == "__main___":
    unittest.main()