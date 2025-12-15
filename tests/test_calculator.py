"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException


class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self):
        """Test adding positive and negative numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self):
        """Test adding negative and positive numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self):
        """Test adding positive number with zero."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self):
        """Test adding zero with positive number."""
        # Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self):
        """Test adding floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_add_special(self):
        """Test adding floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 1
        b = 2
        expected = 3

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_add_large_distinct(self):
        """Test add where result differs from multiply/subtract."""
        calc = Calculator()
        assert calc.add(3, 4) == 7  # 3*4=12≠7, 3-4=-1≠7

    def test_add_zero_negative(self):
        """Test add covers zero with negative."""
        calc = Calculator()
        assert calc.add(0, -5) == -5



class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 4
        expected = 1

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_positive_numbers2(self):
        """Test subtracting positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 2
        expected = 3

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected


    def test_subtract_distinct(self):
        """Test subtract where result differs from add/multiply."""
        calc = Calculator()
        assert calc.subtract(5, 2) == 3

    def test_subtract_negative_numbers(self):
        """Test subtracting positive numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = -3
        expected = -2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_zero(self):
        """Test subtracting positive numbers."""
        # Arrange
        calc = Calculator()
        a = 2
        b = 0
        expected = 2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_psotive_negative(self):
        """Test subtracting positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = -5
        expected = 10

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected

    def test_subtract_negative_positive(self):
        """Test subtracting positive numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = 7
        expected = -12

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected


class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        # Arrange
        calc = Calculator()
        a = 3
        b = 8
        expected = 24

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_negative_numbers(self):
        """Test multiplying positive numbers."""
        # Arrange
        calc = Calculator()
        a = 3
        b = -4
        expected = -12

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_zero(self):
        """Test multiplying positive numbers."""
        # Arrange
        calc = Calculator()
        a = 6
        b = 0
        expected = 0

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_two_negative_numbers(self):
        """Test multiplying positive numbers."""
        # Arrange
        calc = Calculator()
        a = -3
        b = -6
        expected = 18

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected

    def test_multiply_float_negative(self):
        """Test multiplying positive numbers."""
        # Arrange
        calc = Calculator()
        a = -2.5
        b = 2
        expected = -5

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected
    
    def test_multiply_fractions(self):
        """Test multiply distinguishes from divide/add."""
        calc = Calculator()
        assert calc.multiply(6, 3) == 18

class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        # Arrange
        calc = Calculator()
        a = 6
        b = 3
        expected = 2

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_positive_numbers2(self):
        """Test dividing positive numbers."""
        # Arrange
        calc = Calculator()
        a = 2
        b = 4
        expected = 0.5

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_negative_numbers(self):
        """Test dividing positive numbers."""
        # Arrange
        calc = Calculator()
        a = -6
        b = 2
        expected = -3

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_float(self):
        """Test dividing positive numbers."""
        # Arrange
        calc = Calculator()
        a = 1
        b = 2
        expected = 0.5

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_negative_denominator(self):
        """Test dividing positive numbers."""
        # Arrange
        calc = Calculator()
        a = 6
        b = -2
        expected = -3

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_negatives(self):
        """Test dividing positive numbers."""
        # Arrange
        calc = Calculator()
        a = -6
        b = -2
        expected = 3

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_divide_by_zero(self):
        """Test dividing by zero raises an error."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0

        # Act + Assert
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calc.divide(a, b)

    def test_divide_distinct(self):
        """Test divide where result differs from multiply/add."""
        calc = Calculator()
        assert calc.divide(9, 3) == 3


class TestValidation:
    def test_add_above_max_raises(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(Calculator.MAX_VALUE + 1, 0)

    def test_add_below_min_raises(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(Calculator.MIN_VALUE - 1, 1)
   
    def test_subtract_below_max_raises(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.subtract(Calculator.MIN_VALUE - 1, 0)

    def test_multiply_below_min_raises(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.multiply(Calculator.MIN_VALUE - 1, 1)

    def test_multiply_first_arg_out_of_range_raises(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.multiply(Calculator.MAX_VALUE + 1, 1)

    def test_multiply_second_arg_out_of_range_raises(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.multiply(1, Calculator.MIN_VALUE - 1)

    def test_add_second_arg_out_of_range_raises(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(0, Calculator.MAX_VALUE + 1)

    def test_add_second_arg_below_min_raises(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(0, Calculator.MIN_VALUE - 1)

    def test_subtarct_second_arg_out_of_range_raises(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.subtract(0, Calculator.MAX_VALUE + 1)

    def test_subtarct_second_arg_below_min_raises(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.subtract(0, Calculator.MIN_VALUE - 1)

    def test_add_equal_max_is_allowed(self):
        calc = Calculator()
        assert calc.add(Calculator.MAX_VALUE, 0) == Calculator.MAX_VALUE

    def test_subtract_equal_max_is_allowed(self):
        calc = Calculator()
        assert calc.subtract(Calculator.MAX_VALUE, 0) == Calculator.MAX_VALUE

    def test_multiply_equal_max_is_allowed(self):
        calc = Calculator()
        assert calc.multiply(Calculator.MAX_VALUE, 1) == Calculator.MAX_VALUE

    def test_add_equal_min_is_allowed(self):
        calc = Calculator()
        assert calc.add(Calculator.MIN_VALUE, 0) == Calculator.MIN_VALUE

    def test_multiply_equal_min_is_allowed(self):
        calc = Calculator()
        assert calc.multiply(Calculator.MIN_VALUE, 1) == Calculator.MIN_VALUE

    def test_subtract_equal_min_is_allowed(self):
        calc = Calculator()
        assert calc.subtract(Calculator.MIN_VALUE, 0) == Calculator.MIN_VALUE

    def test_both_add_out_of_range(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(Calculator.MAX_VALUE + 1, Calculator.MIN_VALUE - 1)

    def test_validate_input_out_of_range_high(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(1000001, 1)

    def test_validate_input_out_of_range_low(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.add(-1000002, 1)

    def test_divide_first_arg_out_of_range_raises(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.divide(Calculator.MAX_VALUE + 1, 1)

    def test_divide_second_arg_out_of_range_raises(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException):
            calc.divide(1, Calculator.MIN_VALUE -1)

    def test_divide_by_zero_raises_value_error_with_correct_message(self):
        calc = Calculator()
        with pytest.raises(ValueError) as excinfo:
            calc.divide(1, 0)

        msg = str(excinfo.value)
        assert msg == "Cannot divide by zero"

    def test_validation_error_message_contains_value_and_range(self):
        calc = Calculator()
        with pytest.raises(InvalidInputException) as excinfo:
            calc.add(Calculator.MAX_VALUE + 1, 0)

        msg = str(excinfo.value)
        assert "outside the valid range" in msg
        assert str(Calculator.MIN_VALUE) in msg
        assert str(Calculator.MAX_VALUE) in msg

