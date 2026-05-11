import unittest
from main import calculate_pi


class TestPiCalculation(unittest.TestCase):
    """Test cases for the calculate_pi function"""
    
    def test_pi_5_digits(self):
        """Test that pi is calculated to 5 decimal places"""
        result = calculate_pi(5)
        expected = 3.14159  # Pi to 5 decimal places
        self.assertEqual(result, expected)
    
    def test_pi_accuracy(self):
        """Test that the calculated value is close to the actual value of pi"""
        result = calculate_pi(5)
        import math
        # Check if result is within a small tolerance of actual pi
        self.assertAlmostEqual(result, math.pi, places=5)
    
    def test_pi_3_digits(self):
        """Test pi calculation with 3 decimal places"""
        result = calculate_pi(3)
        expected = 3.142
        self.assertEqual(result, expected)
    
    def test_pi_1_digit(self):
        """Test pi calculation with 1 decimal place"""
        result = calculate_pi(1)
        expected = 3.1
        self.assertEqual(result, expected)
    
    def test_pi_default_parameter(self):
        """Test that default parameter is 5 digits"""
        result = calculate_pi()
        expected = 3.14159
        self.assertEqual(result, expected)
    
    def test_return_type(self):
        """Test that the function returns a float"""
        result = calculate_pi(5)
        self.assertIsInstance(result, float)


if __name__ == '__main__':
    # Run the tests
    print("Running tests for calculate_pi function...\n")
    unittest.main(verbosity=2)
