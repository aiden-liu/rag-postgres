import sys
import os

# Add the services directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))

import unittest
from unittest.mock import patch, MagicMock
from services.chunk_data import chunk_data


class TestChunkDataFunction(unittest.TestCase):

    def test_chunk_text(self):
        # Test case for generic text splitting
        simple_text = """
        One of the most important things I didn't understand about the world when I was a child is the degree to which the returns for performance are superlinear.
        """
        result = chunk_data(simple_text, "text")
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

    def test_chunk_markdown(self):
        # Test case for markdown splitting
        markdown_text = """
        # Fun in California
        ## Driving
        Try driving on the 1 down to San Diego
        ### Food
        Make sure to eat a burrito while you're there
        ## Hiking
        Go to Yosemite
        """
        result = chunk_data(markdown_text, "markdown")
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

    def test_chunk_python_code(self):
        # Test case for Python code splitting
        python_text = """
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age

        p1 = Person("John", 36)

        for i in range(10):
            print(i)
        """
        result = chunk_data(python_text, "python")
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

    def test_chunk_javascript_code(self):
        # Test case for JavaScript code splitting
        javascript_text = """
        // Function is called, the return value will end up in x
        let x = myFunction(4, 3);

        function myFunction(a, b) {
            // Function returns the product of a and b
            return a * b;
        }
        """
        result = chunk_data(javascript_text, "javascript")
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)

    def test_chunk_default(self):
        # Test case for default text type handling
        simple_text = """
        This is a simple text document that should be handled by the default text splitter.
        """
        result = chunk_data(simple_text, "unknown")
        self.assertIsInstance(result, list)
        self.assertTrue(len(result) > 0)


if __name__ == '__main__':
    unittest.main()