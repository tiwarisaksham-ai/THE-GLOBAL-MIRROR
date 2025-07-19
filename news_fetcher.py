import requests

API_KEY = "534b0ff2d8bbc293c9004c6fdbde328f"
CATEGORIES = ["world", "nation", "business", "technology", "entertainment", "sports"]

def get_all_news():
    all_news = []
    for category in CATEGORIES:
        url = f"https://gnews.io/api/v4/top-headlines?token={API_KEY}&lang=en&country=in&topic={category}"
        try:
            response = requests.get(url)
            data = response.json()
            articles = data.get("articles", [])
            print(f"✅ {len(articles)} articles fetched for {category}")

            for article in articles:
                all_news.append({
                    "title": article.get("title", "No Title"),
                    "link": article.get("url", "#"),
                    "image": article.get("image") or "/static/placeholder.jpg",
                    "description": article.get("description", ""),
                    "pubDate": article.get("publishedAt", "")[:10],
                    "category": category.capitalize()
                })

        except Exception as e:
            print(f"❌ Error fetching {category} news: {e}")
    print(f"\n🔔 Total articles fetched: {len(all_news)}")
    return all_news
