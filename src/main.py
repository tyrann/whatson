#!/usr/bin/env python3
from reddit import get_comments
from watson_queries import query_watson

def get_mood_for_user(username, subreddit=None, comments_limit=1):
    """ Compute watson mood of user "username" on subreddit "subreddit" by
    looking at last comments. """

    comments = [str(x) for x in get_comments(username, comments_limit)]

    watson_queries = []
    for comment in comments:
        watson_queries.append(query_watson(comment))

    return watson_queries

def main():
    [print(x) for x in get_mood_for_user("timozattol")]

if __name__ == '__main__':
    main()
