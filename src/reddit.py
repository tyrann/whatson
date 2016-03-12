import praw

def get_comments(reddit_username, comments_limit=1):
    """ Get last comments of user "reddit_username" """
    user_agent = ("User tone analysis")
    reddit = praw.Reddit(user_agent=user_agent)
    user = reddit.get_redditor(reddit_username)

    comments = user.get_comments(limit=comments_limit)

    return comments
