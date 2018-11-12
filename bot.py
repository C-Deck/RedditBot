import praw
import emailer
import logger


class Post:
    def __init__(self, postId, postURL, postName):
        self.postId = postId
        self.postURL = postURL
        self.postName = postName

reddit = praw.Reddit(client_id='lM7HHMXUco59Fw',
                     client_secret='9JowMnknvei6XQy_UlqSFtiE--Y',
                     user_agent='<console:DeckerRedditBot:1.0 (by /u/DeckerRedditBot)>  ',
                     username='DeckerRedditBot',
                     password='Hidden') #Password will be added later

for submission in reddit.subreddit('cscareerquestions').hot(limit=10):
    print(submission.title)
    postIds = logger.openFile()
    subId = submission.id
    if subId not in postIds:
        comments = submission.comments
        comments.replace_more(limit=0)
        comment_queue = submission.comments[:]  # Seed with top-level
        while comment_queue:
            comment = comment_queue.pop(0)
            if "Cal Poly" in comment.body or "cal poly" in comment.body:
                postFound = Post(subId, submission.url, submission.title)
                em = emailer.email(comment.body,"Cal Poly Mention", postFound)
                emailer.sendEmail(em)
                logger.log(subId)
            comment_queue.extend(comment.replies)
    else:
        print("Repeat Id")