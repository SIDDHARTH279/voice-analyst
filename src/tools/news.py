from urllib.parse import quote
import feedparser

def get_news(company: str, limit: int = 5) -> list[dict]:
    try:
        url = (
            f"https://news.google.com/rss/search?q={quote(company + ' stock')}"
            "&hl=en-IN&gl=IN&ceid=IN:en"
        )
        feed = feedparser.parse(url)
        return [
            {
                'title': e.get('title'),
                'link': e.get('link'),
                'published': e.get('published')
            }
            for e in feed.entries[:limit]
        ]

    except Exception:
        return []


if __name__ == '__main__':
    for item in get_news('Zomato'):
        print(item['published'], '-', item['title'])