from machinetranslation import translator
import unittest

class TestE2FTranslator(unittest.TestCase):
    def runTest(self):
        self.assertIsNone(translator.englishToFrench(None))
        self.assertEqual(translator.englishToFrench("GoodBye"), 
        "Bonjour")
        self.assertEqual(translator.englishToFrench("Hello"), 
        "Bonjour")

class TestF2ETranslator(unittest.TestCase):
    def runTest(self):
        self.assertIsNone(translator.frenchToEnglish(None))
        self.assertEqual(translator.frenchToEnglish("Bonjour"), 
        "Hello")
        self.assertNotEqual(translator.frenchToEnglish("Bonjour"), 
        "GoodBye")


unittest.main()
