import unittest
from unittest.mock import patch
from io import StringIO
import datetime
import yaml
from module import welcome_user

class TestWelcomeUserFunction(unittest.TestCase):
    def assert_stdout(self, expected_output, mock_stdout):
        welcome_user()
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_welcome_user(self):
        test_data = self.load_test_data()
        for test_case in test_data['tests']:
            with self.subTest(test_case['name']):
                if 'assertions' in test_case:
                    for assertion in test_case['assertions']:
                        if assertion['type'] == 'stdout':
                            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                                with patch('datetime.datetime') as mock_datetime:
                                    mock_datetime.now.return_value = datetime.datetime(
                                        assertion['datetime_mock']['year'],
                                        assertion['datetime_mock']['month'],
                                        assertion['datetime_mock']['day'],
                                        assertion['datetime_mock']['hour'],
                                        assertion['datetime_mock']['minute'],
                                        assertion['datetime_mock']['second']
                                    )
                                    self.assert_stdout(assertion['expected_output'], mock_stdout)

    def load_test_data(self):
        with open('test_data.yaml', 'r') as file:
            return yaml.safe_load(file)

if __name__ == '__main__':
    unittest.main()
