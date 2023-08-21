import unittest
import word_test

class TestWordPrefix(unittest.TestCase):
    def test_prefix(self):
        prefix ="pre"
        word = "preparation"
        result = prefix in word
        self.assertTrue(result)

if __name__ == "__main___":
    unittest.main()