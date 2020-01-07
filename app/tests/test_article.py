import unittest
from app.models import Article

class TestArticle(unittest.TestCase):
    """
    Test Class to test the behaviour of the Movie class
    """
    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_article = Article("Bob", "Random Title", "Short","random.com","random.jpg","12/12/12", "None")
    
    def test_instance(self):
        """
        Tests if instance of the Article class
        """
        self.assertTrue(isinstance(self.new_article,Article))
    
    def test_init(self):
        """
        Tests for proper instantiation
        """
        self.assertEqual(self.new_article.author, "Bob")
        self.assertEqual(self.new_article.title, "Random Title")
        self.assertEqual(self.new_article.description, "Short")
        self.assertEqual(self.new_article.url, "random.com")
        self.assertEqual(self.new_article.img, "random.jpg")
        self.assertEqual(self.new_article.date, "12/12/12")
        self.assertEqual(self.new_article.content, "None")
        

if __name__ == "__main__":
    unittest.main()