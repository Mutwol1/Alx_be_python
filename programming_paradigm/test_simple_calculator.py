from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test cases for SimpleCalculator class"""
    
    def setUp(self):
        """Set up test fixture"""
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        """Test addition operation"""
        self.assertEqual(self.calc.add(2, 3), 5)  # Positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)  # Negative and positive
        self.assertEqual(self.calc.add(-1, -1), -2)  # Negative numbers
        self.assertEqual(self.calc.add(0, 5), 5)  # Zero addition
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)  # Floating point
    
    def test_subtraction(self):
        """Test subtraction operation"""
        self.assertEqual(self.calc.subtract(5, 3), 2)  # Positive numbers
        self.assertEqual(self.calc.subtract(-1, 1), -2)  # Negative and positive
        self.assertEqual(self.calc.subtract(-1, -1), 0)  # Negative numbers
        self.assertEqual(self.calc.subtract(0, 5), -5)  # Zero subtraction
        self.assertEqual(self.calc.subtract(2.5, 1.5), 1.0)  # Floating point
    
    def test_multiplication(self):
        """Test multiplication operation"""
        self.assertEqual(self.calc.multiply(2, 3), 6)  # Positive numbers
        self.assertEqual(self.calc.multiply(-1, 1), -1)  # Negative and positive
        self.assertEqual(self.calc.multiply(-1, -1), 1)  # Negative numbers
        self.assertEqual(self.calc.multiply(0, 5), 0)  # Zero multiplication
        self.assertEqual(self.calc.multiply(2.5, 2), 5.0)  # Floating point
    
    def test_division(self):
        """Test division operation"""
        self.assertEqual(self.calc.divide(6, 3), 2)  # Positive numbers
        self.assertEqual(self.calc.divide(-1, 1), -1)  # Negative and positive
        self.assertEqual(self.calc.divide(-1, -1), 1)  # Negative numbers
        self.assertEqual(self.calc.divide(5, 2), 2.5)  # Floating point result
        self.assertEqual(self.calc.divide(0, 5), 0)  # Zero numerator
        
        # Test division by zero
        self.assertIsNone(self.calc.divide(5, 0))  # Should return None
        self.assertIsNone(self.calc.divide(0, 0))  # 0/0 should return None

if __name__ == '__main__':
    unittest.main()
