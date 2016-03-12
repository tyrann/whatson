#!/usr/bin/env python3
from reddit import get_comments
from watson_queries import query_watson
from json_parser import parse
from plot import plot

def get_mood_for_user(username, subreddit=None, comments_limit=1):
    """ Compute watson mood of user "username" on subreddit "subreddit" by
    looking at last comments. """

    comments = [str(x) for x in get_comments(username, comments_limit)]

    watson_tones = []
    for comment in comments:
        json_data = query_watson(comment)

        tone = parse(json_data)

        watson_tones.append(tone)

        plot(tone.etone.anger, tone.etone.disgust, tone.etone.fear, tone.etone.joy, tone.etone.sadness)

    return watson_tones

def main():
    [print(x) for x in get_mood_for_user("timozattol")]

if __name__ == '__main__':
    main()
