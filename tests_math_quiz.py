import unittest
from math_quiz import generate_random_integer, generate_random_operator, perform_operation

class TestMathQuizFunctions(unittest.TestCase):
    def test_generate_random_integer(self):
        # Test if the generated integer is within the specified range
        for _ in range(100):
            random_int = generate_random_integer(1, 10)
            self.assertTrue(1 <= random_int <= 10)

    def test_generate_random_operator(self):
        # Test if the generated operator is one of the valid operators
        valid_operators = {'+', '-', '*'}
        for _ in range(100):
            random_operator = generate_random_operator()
            self.assertIn(random_operator, valid_operators)

    def test_perform_operation(self):
        # Test if the perform_operation function produces the correct result
        test_cases = [
            (2, 3, '+', ('2 + 3', 5)),
            (8, 4, '-', ('8 - 4', 4)),
            (5, 7, '*', ('5 * 7', 35)),
        ]

        for num1, num2, operator, expected_result in test_cases:
            with self.subTest(num1=num1, num2=num2, operator=operator):
                result = perform_operation(num1, num2, operator)
                self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
