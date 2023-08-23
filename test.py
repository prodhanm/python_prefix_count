import unittest

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

    def test_prefix4(self):
        prefix = 9
        word = "control-9"
        self.assertNotEqual(prefix,word)

    def test_prefix5(self):
        prefix = str(None)
        word = "prefer"
        result = prefix in word
        self.assertNotIsInstance(result,TypeError)

if __name__ == "__main___":
    unittest.main()