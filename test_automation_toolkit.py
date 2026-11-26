import unittest
from unittest.mock import patch
from automation_toolkit import validate, run

class WorkflowTests(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(len(validate([{"argv":["python","--version"]}])), 1)

    def test_invalid(self):
        for value in [[], {}, [None], [{"argv":"echo hi"}], [{"argv":["echo"],"timeout":0}]]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                validate(value)

    @patch("automation_toolkit.subprocess.run")
    def test_execution(self, call):
        run([{"argv":["python","--version"],"timeout":5}])
        call.assert_called_once_with(["python","--version"],shell=False,check=True,timeout=5)
