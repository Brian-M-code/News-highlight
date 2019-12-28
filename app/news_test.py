import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the News class
    '''
    
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News('Security officers killed in IED attack.','28/12/2019','https://www.nation.co.ke/counties/wajir/Security-officers-killed-in-Wajir-IED-attack/3444790-5400124-3yxf4w/index.html','https://img.youtube.com/vi/jVQJY7Ep-Dg/mqdefault.jpg')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))
        


if __name__ == '__main__':
    unittest.main()
