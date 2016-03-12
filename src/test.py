#!/usr/bin/env python3
from reddit import get_comments
from watson_queries import query_watson
from json_parser import parse
from plots import plot_emotions

def get_tone_for_user(username, subreddit=None, comments_limit=1):
    """ Compute watson mood of user "username" on subreddit "subreddit" by
    looking at last comments. """

    comments = [x.body for x in get_comments(username, comments_limit)]

    comment_to_tone = []
    for comment in comments:
        json_data = query_watson(comment)

        tone = parse(json_data)

        comment_to_tone.append((comment, tone))

    return comment_to_tone

def get_raw_tone(string):
    json_data = query_watson(string)
    tone = parse(json_data)
    return tone

def main():
    [plot_emotions(tone.etone) for tone in get_tone_for_user("timozattol")]
if __name__ == '__main__':
    main()
