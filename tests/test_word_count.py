import unittest

from examples.word_count import count_words


class CountWordsTests(unittest.TestCase):
    def test_counts_words_separated_by_spaces(self):
        self.assertEqual(count_words("one two three"), 3)

    def test_empty_text_has_zero_words(self):
        self.assertEqual(count_words(""), 0)

    def test_whitespace_only_has_zero_words(self):
        self.assertEqual(count_words("  \n\t "), 0)

    def test_repeated_whitespace_is_one_separator(self):
        self.assertEqual(count_words("one\n\ttwo"), 2)


if __name__ == "__main__":
    unittest.main()
