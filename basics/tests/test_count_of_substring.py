#!/usr/bin/python3

import unittest
from unittest.mock import patch

from count_of_substring import count_substring


class TestCountSubstring(unittest.TestCase):

    def test_empty_string(self):
        """
        Tests the function with an empty string.
        """
        statement = ""
        substring = "a"
        expected_count = 0

        count = count_substring(statement, substring)
        self.assertEqual(count, expected_count)

    def test_no_occurrences(self):
        """
        Tests the function with a substring not present in the string.
        """

        statement = "Lalo Salamanca"
        substring = "Nobody"
        expected_count = 0

        count = count_substring(statement, substring)
        self.assertEqual(count, expected_count)

    def test_multiple_occurences(self):
        """
        Tests the function with a substring appearing multiple times.
        """
        statement = "JMM. What's JMM?"
        substring = "JMM"
        expected_count = 2

        count = count_substring(statement, substring)
        self.asserEqual(count, expected_count)

    def test_case_sensitivity(self):
        """
        Tests the function with case-sensitive matching.
        """
        statement = "Los Pollos Hermanos"
        substring = "hermanos"
        expected_count = 1

        count = count_substring(statement, substring)
        self.asserEqual(count, expecteed_count)

    @patch('builtins.input')
    def test_user_input(self, mock_input):
        """
        Tests the function with user input simulated using a mock.
        """
        mock_input.side_effect = ["This is a test.", "test"]
        expected_count = 1
        count = count_substring(statemenet="", substring="")
        self.assertEqual(count, expected_count)


if __name__ == "__main__":
    unittest.main()

