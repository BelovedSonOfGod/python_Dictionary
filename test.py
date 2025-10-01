import unittest
from main import PersonalDictionary

class TestDictionaryClass(unittest.TestCase):
    def setUp(self):
        self.dictionaryItem=PersonalDictionary()
        self.dictionaryItem.addToDictionary("ab",4)

    def test_getExpectedValue(self):
        self.assertEqual(self.dictionaryItem.getValue("ab"),[4])

    def test_removeKey_exception(self):
        with self.assertRaises(IndexError):
            self.dictionaryItem.removeKey("sasa")

    def test_removeKey_successful(self):
        self.dictionaryItem.removeKey("ab")
        with self.assertRaises(IndexError):
            self.dictionaryItem.getValue("ab")

    def test_hashFunction(self):
        self.assertEqual(self.dictionaryItem.HashFunction("ab"), 195)

    def test_addAndUpdate(self):
        self.dictionaryItem.addToDictionary("ab",5)
        self.assertEqual(self.dictionaryItem.getValue("ab"),[5])

if __name__ == '__main__':
    unittest.main()