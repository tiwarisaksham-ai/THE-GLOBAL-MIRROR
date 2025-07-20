from flask import Flask, render_template
from news_fetcher import get_all_news, start_background_fetch

app = Flask(__name__)

start_background_fetch()  # ✅ Start background thread AFTER app is defined

@app.route('/')
def homepage():
    all_news = get_all_news()
    return render_template("index.html", news_data=all_news)

if __name__ == '__main__':
    app.run(debug=True)
