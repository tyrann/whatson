import praw

def get_comments(reddit_username):
    """ Get last comments of user "reddit_username" """
    user_agent = ("User tone analysis")
    reddit = praw.Reddit(user_agent=user_agent)
    objects_limit = 10
    user = reddit.get_redditor(reddit_username)

    comments = user.get_comments(limit=objects_limit)

    return comments
