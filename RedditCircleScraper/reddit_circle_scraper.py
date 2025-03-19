import praw
import openai
import requests
import schedule
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Reddit API credentials
reddit = praw.Reddit(
    client_id='your_client_id',
    client_secret='your_client_secret',
    user_agent='your_user_agent'
)

# OpenAI API credentials
openai.api_key = 'your_openai_api_key'

# Circle API endpoint and credentials
CIRCLE_API_ENDPOINT = "https://api-v1.circle.so"
CIRCLE_API_KEY = "your_circle_api_key"

# Keywords and topics to search for
KEYWORDS = ["python", "web scraping", "automation"]

# Storage for post IDs
scraped_post_ids = set()

def scrape_reddit_posts():
    logging.info("Scraping Reddit posts...")
    for keyword in KEYWORDS:
        for submission in reddit.subreddit('all').search(keyword, limit=10):
            if submission.id not in scraped_post_ids:
                scraped_post_ids.add(submission.id)
                rewritten_content = rewrite_content(submission.title, submission.selftext)
                post_to_circle(rewritten_content)

def rewrite_content(title, content):
    logging.info("Rewriting content using GPT-4...")
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=f"Rewrite the following content:\n\nTitle: {title}\n\nContent: {content}",
        max_tokens=1024
    )
    return response['choices'][0]['text'].strip()

def post_to_circle(content):
    logging.info("Posting content to Circle community...")
    headers = {
        "Authorization": f"Bearer {CIRCLE_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "content": content
    }
    response = requests.post(f"{CIRCLE_API_ENDPOINT}/v1/posts", headers=headers, json=data)
    response.raise_for_status()

def main():
    # Schedule the scraping and posting job
    #schedule.every(10).minutes.do(scrape_reddit_posts)

    while True:
        schedule.run_pending()
        time.sleep(1)
    
    #scrape_reddit_posts()

if __name__ == "__main__":
    main()