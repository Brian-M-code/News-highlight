from flask import render_template
from . import main


@main.app_errorhandler(404)
def notfound(error):
    """
    This function renders the 404 error page
    """
    categories = ["business",
                "entertainment",
                "general",
                "health",
                "science",
                "sports",
                "technology"
                ]
    return render_template("notfound.html", categories = categories), 404