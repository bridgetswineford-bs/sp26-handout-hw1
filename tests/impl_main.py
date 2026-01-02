"""
Unit tests for main function.
"""

import sys
sys.path.append('.')
import unittest
from unittest.mock import patch, Mock
from src.main import main

class TestHousingPriorityCalculatorMain(unittest.TestCase):
    """Unit tests for main function of Housing Priority Calculator."""

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['2', '60', 'y', 'n'])
    def test_main_senior_graduating(self, mock_print: Mock) -> None:
        """Test main function for senior who is graduating.
        
        This test is provided as an example for syntax. Please update it to fit your scoring
        logic and expected outputs.
        """
        main()
        mock_print.assert_any_call("Hi, welcome to the Housing Score Calculator")
        mock_print.assert_any_call("Your housing score is 85. Thank you for using this tool.")