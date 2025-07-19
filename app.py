from flask import Flask, render_template
from news_fetcher import get_all_news

app = Flask(__name__)

@app.route('/')
def homepage():
    all_news = get_all_news()
    return render_template("index.html", news_data=all_news)

if __name__ == '__main__':
    app.run(debug=True)
