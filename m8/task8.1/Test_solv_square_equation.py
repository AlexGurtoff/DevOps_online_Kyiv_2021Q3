import unittest
import solv_square_equation


class TestSolvSquareEquation(unittest.TestCase):

    def test_discriminant(self):
        self.assertEqual(solv_square_equation.discriminant(-1, -2, 15), 64)
        self.assertEqual(solv_square_equation.discriminant(5, 3, 7), None)

    def test_roots(self):
        self.assertEqual(solv_square_equation.roots(None, 5, 3, 7), [None, None])
        self.assertEqual(solv_square_equation.roots(0, 1, 12, 36), [-6.0, None])
        self.assertEqual(solv_square_equation.roots(64, -1, -2, 15), [-5.0, 3.0])

    def test_solv_square(self):
        self.assertEqual(solv_square_equation.solv_square(1, 12, 36), [-6.0, None])
        self.assertEqual(solv_square_equation.solv_square(5, 3, 7), [None, None])
        self.assertEqual(solv_square_equation.solv_square(-1, -2, 15), [-5.0, 3.0])


if __name__ == "__main__":
    unittest.main()
