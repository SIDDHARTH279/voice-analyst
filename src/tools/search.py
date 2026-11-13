from ddgs import DDGS


def search_web(query: str, limit: int = 5) -> list[dict]:

    try:
        result = DDGS().text(query, max_results=limit)

        return [
            {'title': r['title'],
             'url': r['href'],
             'snippet': r['body']} for r in result
        ]
    except Exception as e:
        return {e}


if __name__ == '__main__':
    print(search_web('Razorpay company overview'))
