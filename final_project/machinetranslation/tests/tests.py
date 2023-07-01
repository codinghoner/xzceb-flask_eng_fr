import unittest
from .translator import english_to_french, french_to_english

class TranslationTestCase(unittest.TestCase):
 
    def test_english_to_french_bonjour(self):
        english_word = 'Hello'
        expected_translation = 'Bonjour'  # Same word in French

        translated_word = english_to_french(english_word)

        self.assertEqual(translated_word, expected_translation, f"Translation of '{english_word}' should be '{expected_translation}', but got '{translated_word}' instead.")

    def test_french_to_english_bonjour(self):
        french_word = 'Bonjour'
        expected_translation = 'Hello'

        translated_word = french_to_english(french_word)

        self.assertEqual(translated_word, expected_translation, f"Translation of '{french_word}' should be '{expected_translation}', but got '{translated_word}' instead.")

if __name__ == '__main__':
    unittest.main()