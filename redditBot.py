import praw
import getPlayerStats

#create reddit obj
r = praw.Reddit(user_agent='Python NBA Player Stats Bot by /u/username')

#login, may need ('username', 'password')
r.login('bot_username', 'bot_password')
aready_done = []

while True:
	subreddit = r.get_subreddit('nba')
	for comment in subreddit.get_new(limit=MAXPOSTS):
		#turns comment tree into unordered list
		flatten_comments = praw.helpers.flatten_tree(submission.comments)
		for comment in flat_comments:
			if "%/stats?" in comment.body and comment.id not in already_done:
				#get player name
				splitComment = comment.body.split('%')
				playerName = splitComment[0]
				#reply
				comment.reply(playerStats(player_name))
				already_done.add(comment.id)


