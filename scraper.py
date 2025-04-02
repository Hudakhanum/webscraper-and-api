import requests
from bs4 import BeautifulSoup
import sqlite3

# AI news source (TechCrunch AI section)
URL = "https://techcrunch.com/tag/ai/"

def scrape_ai_news():
    response = requests.get(URL)
    if response.status_code != 200:
        print("❌ Failed to fetch AI news")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    articles = []

    # Extract news articles
    for article in soup.find_all("a", class_="post-block_title_link")[:5]:  # Limit to 5 articles
        title = article.get_text(strip=True)
        url = article["href"]
        articles.append((title, url))

    return articles

def save_to_db(articles):
    conn = sqlite3.connect("news.db")
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            url TEXT NOT NULL UNIQUE
        )
    """)

    # Insert articles (avoid duplicates)
    for title, url in articles:
        try:
            cursor.execute("INSERT INTO articles (title, url) VALUES (?, ?)", (title, url))
        except sqlite3.IntegrityError:
            pass  # Ignore duplicates

    conn.commit()
    conn.close()
    print(f"✅ {len(articles)} AI articles saved to database!")

if __name__ == "_main_":
    print("🔍 Fetching latest AI news...")
    articles = scrape_ai_news()
    save_to_db(articles)