import requests
from .models import Article

# config api and urls
api_key = None
top_news_url = None
top_news_by_source_url = None
category_news_url = None
search_news_url = None
news_sources_url = None

def configure_requests(app):
    global api_key, top_news_url, top_news_by_source_url, category_news_url, search_news_url, news_sources_url
    api_key = app.config["NEWS_API_KEY"]
    top_news_url = app.config["TOP_NEWS_URL"]
    top_news_by_source_url = app.config["TOP_NEWS_BY_SOURCE_URL"]
    category_news_url = app.config["CATEGORY_NEWS_URL"]
    search_news_url = app.config["SEARCH_NEWS_URL"]
    news_sources_url = app.config["NEWS_SOURCES_URL"]



def get_top_news():
    get_top_news_url = top_news_url.format(api_key)
    get_news_response = requests.get(get_top_news_url).json()
    
    if get_news_response["articles"]:
        news_results_list = get_news_response["articles"]
        top_news_results = process(news_results_list)

    return top_news_results

def get_top_news_by_source(source):
    get_top_news_by_source_url = top_news_by_source_url.format(source, api_key)
    get_top_news_by_source_response = requests.get(get_top_news_by_source_url).json()

    if get_top_news_by_source_response["articles"]:
        news_source_results_list = get_top_news_by_source_response["articles"]
        top_news_by_source_results = process(news_source_results_list)

    return top_news_by_source_results

def get_news_by_category(category):
    get_news_by_category_url = category_news_url.format(category, api_key)
    category_response = requests.get(get_news_by_category_url).json()

    if category_response["articles"]:
        category_list = category_response["articles"]
        category_results = process(category_list)

    return category_results

def get_sources():
    get_news_sources_url = news_sources_url.format(api_key)
    get_sources_response = requests.get(get_news_sources_url).json()

    return get_sources_response["sources"]

def search_news(query):
    get_search_url = search_news_url.format(query, api_key)
    search_response = requests.get(get_search_url).json()

    if search_response["articles"]:
        results_list = search_response["articles"]
        search_results = process(results_list)

    return search_results

def process(news_list):
    top_news_results = []
    for item in news_list:
        author = item.get("author")
        title = item.get("title")
        description = item.get("description")
        url = item.get("url")
        img = item.get("urlToImage")
        date = item.get("publishedAt")
        content = item.get("content")

        if img:
            news_object = Article(author, title, description, url, img, date, content)
            top_news_results.append(news_object)

    return top_news_results








