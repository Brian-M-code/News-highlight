import unittest
from app.models import Source

class TestSource(unittest.TestCase):
    """
    Test Class to test the behaviour of the Source class
    """
    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_source = Source("abc-news","ABC News")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))

    def test_init(self):
        self.assertEqual(self.new_source.id, "abc-news")
        self.assertEqual(self.new_source.name, "ABC News")

if __name__ == "__main__":
    unittest.main()