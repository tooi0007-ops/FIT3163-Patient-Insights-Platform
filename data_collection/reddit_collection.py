"""
Prototype Reddit data collection module for the
FIT3163 Patient Insights Platform.

This module is intended to retrieve publicly available
diabetes-related Reddit posts using PRAW if appropriate
Reddit Data API access is granted.
"""

import praw
import pandas as pd


def create_reddit_client(client_id, client_secret, user_agent):
    reddit = praw.Reddit(
        client_id=client_id,
        client_secret=client_secret,
        user_agent=user_agent
    )

    return reddit


def collect_posts(reddit, subreddit_name, limit=100):
    subreddit = reddit.subreddit(subreddit_name)

    posts = []

    for post in subreddit.new(limit=limit):
        posts.append({
            "post_id": post.id,
            "title": post.title,
            "body": post.selftext,
            "created_utc": post.created_utc
        })

    return pd.DataFrame(posts)


# Data collection is not executed automatically.
# Appropriate Reddit API access is required before use.
