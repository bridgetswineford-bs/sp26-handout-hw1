"""
Unit tests for the HousingQuestionAsker class.
"""

import unittest
from unittest.mock import patch, Mock
from src.question_asker import (
    ask_additional_questions,
    ask_class_year,
    ask_credits_earned,
    ask_graduation_status,
)


class TestHousingQuestionAsker(unittest.TestCase):
    """Unit tests for question asker."""

    @patch('builtins.input', side_effect=['3'])
    def test_ask_class_year_valid_input(self, _: Mock) -> None:
        """Test ask_class_year with valid user input.

        We use @patch('builtins.input', ...) to simulate user input 
        that would normally be typed.
        
        This first test is written for you. 
        Use this test as an example to complete the rest of the tests.
        """
        result = ask_class_year()
        self.assertEqual(result, 3) # Check that it returned 3

    @patch('builtins.input', side_effect=['1'])
    def test_ask_class_year_freshman(self, _: Mock) -> None:
        """Test ask_class_year returns 1 for freshman."""

    @patch('builtins.input', side_effect=['4'])
    def test_ask_class_year_senior(self, _: Mock) -> None:
        """Test ask_class_year returns 4 for senior."""

    @patch('builtins.input', side_effect=['-4', '2'])
    def test_ask_class_year_invalid_then_valid(self, _: Mock) -> None:
        """Test ask_class_year with invalid input followed by valid input."""

    @patch('builtins.input', side_effect=['0', '5', '2'])
    def test_ask_class_year_out_of_range_then_valid(self, _: Mock) -> None:
        """Test ask_class_year with out-of-range inputs (0, 5) then valid input."""

    @patch('builtins.input', side_effect=['y'])
    def test_ask_graduation_status_yes(self, _: Mock) -> None:
        """Test ask_graduation_status with 'y' input."""

    @patch('builtins.input', side_effect=['Y'])
    def test_ask_graduation_status_uppercase_yes(self, _: Mock) -> None:
        """Test ask_graduation_status with 'Y' input (uppercase)."""

    @patch('builtins.input', side_effect=['n'])
    def test_ask_graduation_status_no(self, _: Mock) -> None:
        """Test ask_graduation_status with 'n' input."""

    @patch('builtins.input', side_effect=['N'])
    def test_ask_graduation_status_uppercase_no(self, _: Mock) -> None:
        """Test ask_graduation_status with 'N' input (uppercase)."""

    @patch('builtins.input', side_effect=['maybe', 'yes', 'y'])
    def test_ask_graduation_status_invalid_then_valid(self, _: Mock) -> None:
        """Test ask_graduation_status with invalid inputs followed by valid input."""

    @patch('builtins.input', side_effect=['15'])
    def test_ask_credits_earned_valid(self, _: Mock) -> None:
        """Test ask_credits_earned with valid input."""

    @patch('builtins.input', side_effect=['0'])
    def test_ask_credits_earned_zero(self, _: Mock) -> None:
        """Test ask_credits_earned with zero credits."""

    @patch('builtins.input', side_effect=['120'])
    def test_ask_credits_earned_high_number(self, _: Mock) -> None:
        """Test ask_credits_earned with high credit count."""

    @patch('builtins.input', side_effect=['-5', '-10', '20'])
    def test_ask_credits_earned_invalid_then_valid(self, _: Mock) -> None:
        """Test ask_credits_earned with invalid inputs followed by valid input."""

    @patch('builtins.input', side_effect=['y', 'n', 'y', 'n', 'y'])
    def test_ask_additional_questions_basic(self, _: Mock) -> None:
        """Test ask_additional_questions with basic y/n responses."""
        result = ask_additional_questions()
        # Remember: these tests need to pass for ANY implementation of ask_additional_questions.
        # We cannot assume that the questions are the same as the ones you chose.
        # We can only know that the result is a dictionary with boolean values that correspond
        # to the user's yes/no answers.

    @patch('builtins.input', side_effect=['n', 'y', 'n', 'y', 'n'])
    def test_ask_additional_questions_reverse(self, _: Mock) -> None:
        """Test ask_additional_questions with n/y responses."""
        result = ask_additional_questions()

    @patch('builtins.input', side_effect=['Y', 'N', 'Y', 'N', 'Y'])
    def test_ask_additional_questions_uppercase(self, _: Mock) -> None:
        """Test ask_additional_questions with uppercase responses."""
        result = ask_additional_questions()

    @patch('builtins.input', side_effect=['invalid', 'y', 'maybe', 'n', 'yes', 'no', 'y', 'n', 'y'])
    def test_ask_additional_questions_with_invalid_input(self, _: Mock) -> None:
        """Test ask_additional_questions with some invalid inputs."""
        result = ask_additional_questions()
