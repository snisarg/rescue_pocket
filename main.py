import json
import urllib3
from save import process_articles, save_to_csv
from auth import authenticate
from read import retrieve_articles

# Disable SSL warnings since we're temporarily disabling verification
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():
    try:
        # Authenticate and get access token
        access_token = authenticate()

        # Retrieve articles
        articles = retrieve_articles(access_token)

        # Process and print filtered article data
        print("\nProcessing articles...")
        filtered_articles = process_articles(articles)

        # Print article titles
        print("\nYour Pocket Articles:")
        for item_id, item in filtered_articles.items():
            print(f"- {item.get('resolved_title', 'No title')}")

        # Save to CSV
        csv_file = save_to_csv(filtered_articles)
        print(f"\nArticles have been saved to: {csv_file}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
