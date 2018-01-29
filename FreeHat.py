####################
# Nick Miethe
# 4/20/2017
# Simple test reddit bot which randomly posts a specified comment
####################

#!/usr/bin/python
import praw
import time
import random

def upvote(redditor):
	#comments_new = redditor.comments(limit=None)
	for comment in redditor.comments.new():
		comment.upvote()
			
def main():

	#reddit = praw.Reddit('bot2')
	reddit = praw.Reddit(client_id='####',
                     client_secret='####',
                     user_agent='####',
                     username='####',
                     password='####')
	
	while True:
		user = reddit.redditor('NessieB0t')
		upvote(user)
		count = random.randint(1,10)
		while count > 0:
			subreddit = reddit.subreddit('random')
			for submission in subreddit.new():
				for comment in submission.comments.list():
					comment.upvote()
				submission.reply("This thread has been visited by the Free Hat Fairy!")
				count -=1
				break
	
	
if __name__ == "__main__":
    main()
