import requests
from auth import CONSUMER_KEY
import time

# Pocket API endpoint for retrieving articles
RETRIEVE_URL = "https://getpocket.com/v3/get"

def retrieve_articles(access_token, count=30):
    """Retrieve all articles from Pocket using pagination"""
    all_articles = []
    offset = 0  # Start from the beginning

    while True:
        data = {
            "consumer_key": CONSUMER_KEY,
            "access_token": access_token,
            "count": count,
            "detailType": "complete",
            "offset": offset
        }

        response = requests.post(RETRIEVE_URL, data=data, verify=False)
        if response.status_code == 200:
            result = response.json()
            articles = result.get('list', {})

            if not articles:  # No more articles to retrieve
                break

            all_articles.extend(articles.values())


            if len(articles) < count:
                break

            # Update offset for next page
            offset += len(articles)

            # Add a small delay to avoid rate limiting
            time.sleep(1)

            # Print progress
            print(f"Retrieved {len(all_articles)} articles so far...")
        else:
            raise Exception(f"Failed to retrieve articles: {response.text}")

    print(f"\nTotal articles retrieved: {len(all_articles)}")
    return {"list": {article['item_id']: article for article in all_articles}}
