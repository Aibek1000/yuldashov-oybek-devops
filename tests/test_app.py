import os
import unittest
from unittest.mock import patch
from app.main import student_info


class AppTests(unittest.TestCase):
    def test_default_data(self):
        with patch.dict(os.environ, {}, clear=True):
            text = student_info()
        for value in (
            "Name: Oybek",
            "Surname: Yuldashov",
            "Group: IT2-2307",
            "Student ID: 41559",
        ):
            self.assertIn(value, text)

    def test_environment_data(self):
        values = {
            "STUDENT_NAME": "TestName",
            "STUDENT_SURNAME": "TestSurname",
            "STUDENT_GROUP": "TestGroup",
            "STUDENT_ID": "12345",
        }
        with patch.dict(os.environ, values, clear=True):
            text = student_info()
        for value in values.values():
            self.assertIn(value, text)


if __name__ == "__main__":
    unittest.main()
