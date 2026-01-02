"""
Unit tests for the HousingPriorityCalculator class.
"""

import sys
sys.path.append('.')
import unittest
from src.priority_calculator import (
    points_for_additional_questions,
    points_for_credits,
    points_for_class_year,
    points_for_graduation,
    calculate_total_score,
)


class TestHousingPriorityCalculator(unittest.TestCase):
    """Unit tests for the housing priority calculator."""

    def test_points_for_class_year_freshman(self) -> None:
        """Test points_for_class_year for freshman (year 1)."""
        # Based on YOUR scoring system, what should freshmen get?
        # If your system gives freshmen 10 points, then:
        # expected_points = 10
        pass

    def test_points_for_class_year_sophomore(self) -> None:
        """Test points_for_class_year for sophomore (year 2)."""
        # Based on YOUR scoring system, what should sophomores get?
        pass

    def test_points_for_class_year_junior(self) -> None:
        """Test points_for_class_year for junior (year 3)."""
        # Based on YOUR scoring system, what should juniors get?
        pass

    def test_points_for_class_year_senior(self) -> None:
        """Test points_for_class_year for senior (year 4)."""
        # Based on YOUR scoring system, what should seniors get?
        pass

    def test_points_for_graduation_true(self) -> None:
        """Test points_for_graduation when graduating."""
        # How many points should graduating students get?
        pass

    def test_points_for_graduation_false(self) -> None:
        """Test points_for_graduation when not graduating."""
        # How many points should non-graduating students get?
        pass

    def test_points_for_credits_zero(self) -> None:
        """Test points_for_credits with 0 credits."""
        # What should 0 credits give?
        pass

    def test_points_for_credits_low(self) -> None:
        """Test points_for_credits with low credit count (e.g., 7)."""
        pass

    def test_points_for_credits_medium(self) -> None:
        """Test points_for_credits with medium credit count (e.g., 15)."""
        # Test your scoring system with 15 credits
        pass

    def test_points_for_credits_high(self) -> None:
        """Test points_for_credits with high credit count (e.g., 30)."""
        # Test your scoring system with 30 credits
        pass

    def test_points_for_additional_questions_all_true(self) -> None:
        """Test points_for_additional_questions with all True responses."""
        # Based on YOUR additional questions and scoring, what should all True yield?
        pass

    def test_points_for_additional_questions_all_false(self) -> None:
        """Test points_for_additional_questions with all False responses."""
        pass

    def test_points_for_additional_questions_mixed(self) -> None:
        """Test points_for_additional_questions with mixed responses."""
        pass

    def test_calculate_total_score_freshman_scenario(self) -> None:
        """Test calculate_total_score for a freshman scenario."""
        # Calculate expected total based on YOUR scoring system
        pass

    def test_calculate_total_score_senior_graduating_scenario(self) -> None:
        """Test calculate_total_score for a graduating senior scenario."""
        pass

    def test_calculate_total_score_senior_non_graduating_scenario(self) -> None:
        """Test calculate_total_score for a non-graduating senior scenario."""
        pass

    def test_calculate_total_score_edge_cases(self) -> None:
        """Test calculate_total_score with edge cases."""
        # Test edge cases as needed based on your priority scoring system.

        # Note: you don't need to test for negative credits or invalid years,
        # since your question asker should be disallowing negative inputs anyway.
        pass
