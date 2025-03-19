# Reddit to Circle Content Automation System

This project implements a robust scraping and automation system designed to scrape posts from Reddit based on specific keywords and topics, rewrite these posts using OpenAI's GPT-4, and post the rewritten content to a community on the Circle platform. The system runs continuously, scraping and posting new content at regular intervals without manual intervention.

## Features

- **Continuous Operation**: The system runs continuously, scraping and posting new content at regular intervals.
- **Error Handling**: Comprehensive error handling ensures stability and robustness.
- **Deduplication**: Ensures that there are no duplicate posts being scraped or posted to the community.
- **Post Tracking**: Tracks the IDs of scraped posts to prevent duplication.

## Technologies Used

- **Python**: The core programming language used for the implementation.
- **PRAW (Python Reddit API Wrapper)**: Used for scraping posts from Reddit.
- **OpenAI GPT-4**: Used for rewriting the scraped content.
- **Circle API**: Used for posting the rewritten content to the Circle community.
- **APScheduler**: Used for scheduling the scraping and posting tasks.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/ShwetaGote-py/InstgramScriper.git
    cd InstgramScriper
    ```

2. **Install Dependencies**:
    ```bash
    pip install praw openai requests schedule
    ```

## Configuration

1. **Set Up Environment Variables**: Create a `.env` file in the root directory of the project and add your API credentials.
    ```env
    REDDIT_CLIENT_ID=your_client_id
    REDDIT_CLIENT_SECRET=your_client_secret
    REDDIT_USER_AGENT=your_user_agent
    OPENAI_API_KEY=your_openai_api_key
    CIRCLE_API_KEY=your_circle_api_key
    ```

## Running the Script

To start the system, simply run the `reddit_circle_scraper.py` script:
```bash
python reddit_circle_scraper.py
```

## Example Code

Below is an example implementation of the system:

```python name=reddit_circle_scraper.py
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
    schedule.every(10).minutes.do(scrape_reddit_posts)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
