import tweepy
from twitter_config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

def tweet(tweet_text):

	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

	try:
		api = tweepy.API(auth)
	except Exception as e:
		logging.debug('Failed to set up twitter api with OAuth: {}'.format(e))
		raise e

	try:
		api.update_status(tweet_text)
	except Exception as e:
		logging.debug('Failed to upadate status: {}'.format(e))
		raise e

