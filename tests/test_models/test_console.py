import unittest
from console import HBNBCommand
from io import StringIO
import sys

class TestConsole(unittest.TestCase):
    def setUp(self):
        self.backup = sys.stdout
        self.output = StringIO()
        sys.stdout = self.output
        self.console = HBNBCommand()

    def tearDown(self):
        sys.stdout = self.backup

    def test_quit(self):
        self.console.onecmd("quit")
        self.assertEqual(self.output.getvalue(), '')

    def test_EOF(self):
        self.console.onecmd("EOF")
        self.assertEqual(self.output.getvalue(), '\n')

    def test_create(self):
        self.console.onecmd("create User")
        self.assertTrue(len(self.output.getvalue()) > 0)

    def test_show(self):
        self.console.onecmd("create User")
        user_id = self.output.getvalue().strip()
        self.output.truncate(0)
        self.output.seek(0)
        self.console.onecmd(f"show User {user_id}")
        self.assertIn(user_id, self.output.getvalue())

if __name__ == '__main__':
    unittest.main()
