import csv
import json
from datetime import datetime

# Column mapping configuration for Pocket articles
COLUMN_MAPPING = {
    # Basic article information
    "item_id": True,
    "resolved_id": False,
    "given_url": True,
    "given_title": True,
    "resolved_title": True,
    "resolved_url": True,
    "excerpt": True,

    # Status and metadata
    "favorite": True,
    "status": True,
    "is_article": True,
    "is_index": False,
    "has_video": False,
    "has_image": False,

    # Time-related fields
    "time_added": True,
    "time_updated": True,
    "time_read": True,
    "time_favorited": True,

    # Content metrics
    "word_count": True,
    "time_to_read": True,
    "listen_duration_estimate": True,
    "lang": True,

    # Media and images
    "top_image_url": False,
    "images": False,
    "image": False,

    # Domain information
    "domain_metadata": False,

    # Additional metadata
    "sort_id": False,
    "tags": True
}

def filter_article_data(article):
    """Filter article data based on COLUMN_MAPPING configuration"""
    return {k: v for k, v in article.items() if COLUMN_MAPPING.get(k, False)}

def process_articles(articles):
    """Process all articles and return filtered data"""
    filtered_articles = {}
    for item_id, item in articles['list'].items():
        filtered_articles[item_id] = filter_article_data(item)
    return filtered_articles

def convert_timestamp(timestamp):
    """Convert Unix timestamp to readable datetime"""
    if timestamp and timestamp != "0":
        return datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')
    return ""

def format_tags(tags):
    """Format tags dictionary as a comma-separated string"""
    if tags:
        return ", ".join(tags.keys())
    return ""

def save_to_csv(articles, filename=None):
    """Save filtered articles to CSV file"""
    if not filename:
        filename = f"pocket_articles_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    # Get all possible fields from the first article
    if not articles:
        print("No articles to save")
        return

    first_article = next(iter(articles.values()))
    fieldnames = list(first_article.keys())

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for article in articles.values():
            # Create a copy of the article for modification
            row = article.copy()

            # Convert timestamps to readable format
            for field in ['time_added', 'time_updated', 'time_read', 'time_favorited']:
                if field in row:
                    row[field] = convert_timestamp(row[field])

            # Format tags
            if 'tags' in row:
                row['tags'] = format_tags(row['tags'])

            writer.writerow(row)

    print(f"Saved {len(articles)} articles to {filename}")
    return filename
