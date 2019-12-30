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

def process_results(news_list):
    '''
    Function that processes the news result and transform them to a list of objects
    
    Args:
        news_list: A list of dictionaries that contain news details
    
    Returns:
        news_results: A list of news objects
    
    '''
    news_results = []
    for news_item in news_list:
        title = news_item.get('title')
        description = news_item.get('description')
        publishedAt = news_item.get('publishedAt')
        content = news_item.get('content')
        url = news_item.get('url')
        img_url = news_item.get('urlToImage')
        
        date_time_obj = datetime.datetime.strptime(publishedAt, '%Y-%m-%dT%H:%M:%SZ')
        publishedAt = date_time_obj.date()
        
        if img_url:
                news_object = News(title,description,publishedAt,content,url,img_url)
                news_result.append(news_object)
                
    return news_results
                                                                                                                                                         