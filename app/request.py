from app import app
import urllib.request, json
from  .models import Source, Article
from datetime import datetime

Article = articles.Article
Source = sources.Source

# Getting the API key
api_key = None

# Getting the news source base url
source_base_url = None
article_base_url = None

def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    source_base_url = app.config['NEWS_SOURCE_BASE_URL']
    article_base_url = app.config['ARTICLE_BASE_URL']

def get_source():
    '''
    Function that gets the json response to out url request
    '''
    get_source_url = source_base_url.format(api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_sourceResults(source_results_list)

    return source_results

def process_sourceResults(source_list):

    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')

        source_object = Source(id,name, description, url)
        source_results.append(source_object)

    return source_results

def get_source_articles(id):
    get_source_articles_url = article_base_url.format(id, api_key)

    with urllib.request.urlopen(get_source_articles_url) as url:
        source_articles_data = url.read()
        source_articles_response = json.loads(source_articles_data)

    source_articles_result = None
    if source_articles_response['articles']:
            source_articles_list = source_articles_response['articles']
            source_articles_result = process_articleResults(source_articles_list)

    return source_articles_result

def process_articleResults(article_list):

    article_results = []
    for article in article_list:
        source = article.get('source')
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('publishedAt')
        content = article.get('content')

        publishedAt = datetime.strptime(publishedAt, "%Y-%m-%dT%H:%M:%SZ").date()


        article_object = Article(source, author, title, description, url, urlToImage, publishedAt, content)
        article_results.append(article_object)

    return article_results