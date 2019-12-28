from app import app
import urllib.request,json
from .models import news

News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the news base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_News(country):
    '''
    Function that gets the json response to our url request
    '''
    
    get_news_url = base_url.format(country,api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
            get_news_data = url.read()
            get_news_response = json.loads(get_news_data)
            
            news_results = None
            
            if get_news_response['articles']:
                news_results_list = get_news_response(news_result_list)
                
    
    return news_results
                                                                                                                                                         