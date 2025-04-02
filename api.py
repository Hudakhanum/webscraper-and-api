from fastapi import FastAPI, Query, HTTPException
import sqlite3

app = FastAPI()

def get_ai_news(query: str = None):
    conn = sqlite3.connect("news.db")
    cursor = conn.cursor()

    if query:
        cursor.execute("SELECT title, url FROM articles WHERE title LIKE ?", ('%' + query + '%',))
    else:
        cursor.execute("SELECT title, url FROM articles")

    news = cursor.fetchall()
    conn.close()

    return [{"title": row[0], "url": row[1]} for row in news]

@app.get("/news")
def fetch_news(q: str = Query(None, description="Search AI news")):
    news = get_ai_news(q)

