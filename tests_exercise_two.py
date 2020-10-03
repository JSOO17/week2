import io
import sys
import unittest
from unittest.mock import patch
from undecorated import undecorated
from exercises.exercise_two import colors_valid


class ExerciseTwoTests(unittest.TestCase):

    @patch('builtins.input', return_value='rojo')
    def test_in_color(self, mock_input):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        color = mock_input()
        function = undecorated(colors_valid)
        result = function(color)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), f"{color.lower()} is in colors\n")
        self.assertFalse(result)

    @patch('builtins.input', return_value='verde')
    def test_in_not_color(self, mock_input):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        color = mock_input()
        color = mock_input()
        function = undecorated(colors_valid)
        result = function(color)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "Not a valid color and continue the loop.\n")
        self.assertTrue(result)

    @patch('builtins.input', return_value='exit')
    def test_exit_color(self, mock_input):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        color = mock_input()
        color = mock_input()
        function = undecorated(colors_valid)
        result = function(color)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "bye\n")
        self.assertFalse(result)

    @patch('builtins.input', side_effect=['verde', 'rojo'])
    def test_exit_color(self, mock_input):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        color = mock_input()
        result = colors_valid(color)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), 'Not a valid color and continue the loop.\nrojo is in colors\n')
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
