from flask import render_template
from . import main
from ..requests import get_top_news ,get_top_news_by_source, get_sources, get_news_by_category, search_news

@main.route("/")
def index():
    top_news = get_top_news()
    news_source = get_sources()
    news = get_top_news()
    categories = ["business",
                "entertainment",
                "general",
                "health",
                "science",
                "sports",
                "technology"
                ]
    return render_template("index.html", 
                            top_news = top_news,
                            sources = news_source,
                            news = news,
                            categories = categories)

@main.route("/source/<source>")
def source(source):
    top_news_by_source = get_top_news_by_source(source)
    news_source = get_sources()
    categories = ["business",
                "entertainment",
                "general",
                "health",
                "science",
                "sports",
                "technology"
                ]
    return render_template("source.html",
                            sources = top_news_by_source,
                            news_source = news_source,
                            categories = categories,
                            source = source)

@main.route("/category/<category>")
def category(category):
    news_category = get_news_by_category(category)
    categories = ["business",
                "entertainment",
                "general",
                "health",
                "science",
                "sports",
                "technology"
                ]
    return render_template("category.html",
                            news_category = news_category,
                            categories = categories,
                            category = category)

@main.route("/search/<query>")
def search(query):
    search_articles = search_news(query)
    categories = ["business",
                "entertainment",
                "general",
                "health",
                "science",
                "sports",
                "technology"
                ]
    return render_template("search.html",
                            search_articles = search_articles,
                            categories = categories)

