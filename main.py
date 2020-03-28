import praw
from wordcloud import WordCloud, STOPWORDS
import json

sub = "worldpolitics"

with open("credentials.json") as f:
    params = json.load(f)

reddit = praw.Reddit(client_id=params["client_id"],
                     client_secret=params["client_secret"],
                     user_agent="UltimateForm's reddit2cloud script")
allcomments = list()

for submission in reddit.subreddit(sub).hot(limit=10):
  submission.comments.replace_more(limit=0)
  commentlist=submission.comments.list()
  allcomments.extend(map(lambda x: x.body, commentlist))

stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords, background_color="white", width=1024, height=1024).generate(" ".join(allcomments))
wordcloud.to_file("{0}.wordcloud.png".format(sub))