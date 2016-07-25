#!/Users/FSQMcAfee/Twitter/markov-text/.venv/bin/python

# Markov Text Generator - Twitter Bot
# 
# Finlay McAfee

from twitter.tweet import tweet
from db import Db
from gen import Generator
from sql import Sql
from rnd import Rnd

import sqlite3
import sys
import logging

logging.basicConfig(filename="markov_tweet.log",level=logging.DEBUG)
WORD_SEPARATOR = ' '
TWITTER_CHAR_LIMIT = 140

def main(name):

	db = Db(sqlite3.connect(name + '.db'), Sql())
	generator = Generator(name, db, Rnd())

	s = generator.generate(WORD_SEPARATOR)
	attempts = 0

	while (not is_tweet_valid(s)):

		logging.debug('Attempt {} ...\n'.format(attempts))

		s = generator.generate(WORD_SEPARATOR)
		logging.info('GENERATED: {}\n'.format(s))

		attempts += 1

	logging.debug('Attempt was valid! Now trying to tweet ...\n')

	try:
		tweet(s)
		logging.info('Success! Tweeted: {}\n'.format(s))
	except Exception as e:
		logging.debug('Tweet was unsuccessful: \n Raised following error: {}\n'.format(e))

def is_tweet_valid(tweet_str):

	l = len(tweet_str)
	valid = l <= TWITTER_CHAR_LIMIT and l > 0

	return valid
			

if __name__ == '__main__':

	import sys

	args = sys.argv
	name = args[1]

	if not len(args) == 2:
		raise ValueError('Usage: python markov_tweet.py <model name>')

	logging.debug('Using {}.py database to generate a tweet\n'.format(name))

	main(name)


