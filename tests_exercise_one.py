import io
import sys
import unittest
from exercises.exercise import min_age


class ExerciseOneTests(unittest.TestCase):

    def test_allow(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        name = "jaider"
        age = 18
        min_age(name, age)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), f"{name} is allowed to drive\n")

    def test_not_allow(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        name = 'maria'
        age = 14
        min_age(name, age)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), f"{name} is not allowed to drive\n")

    def test_type_error(self):
        # prepare
        name = 'maria'
        age = "14"

        # assert
        with self.assertRaises(TypeError):
            min_age(name, age)


if __name__ == "__main__":
    unittest.main()
