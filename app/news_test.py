import unittest
from models import news
News = news.News


class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.news_highlight = News('COVID-19 Billionaires', 'Covid-19 funds looted by politicians', '12/9/2020', 'Covid money stolen in Kenya',
                                   'https://www.standardmedia.co.ke/the-standard-insider/article/2001381008/the-corona-billionaires-why-some-businesses-are-thriving', 'https://ichef.bbci.co.uk/news/1024/cpsprodpb/17B33/production/_112157079_gettyimages-1035862892-1.jpg')

    def test_instance(self):

        self.assertTrue(isinstance(self.news_highlight, News))


if __name__ == '__main__':
    unittest.main()
