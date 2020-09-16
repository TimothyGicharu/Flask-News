import unittest
from app.models import Source


class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_source = Source('abc-news', 'ABC News', 'Your top news source', 'https://abcnews.go.com"')

    def test_instance(self):

        self.assertTrue(isinstance(self.new_source, Source))        
