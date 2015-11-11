#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time
from time import sleep
from random import randint
import ottawacityjobs as p

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'your consumer key'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'your consumer secret key'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = 'your access key'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'your access secret key'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def post_tweets(results, language="en"):
    """This will POST the tweet to Twitter"""
    for job in results:
        if language == 'en':
            greeting = "Job with the city of #Ottawa #ref:" + str(randint(0,99)) + " "
        else:
            greeting = "Offre d'emploi de la ville d'#Ottawa #ref:" + str(randint(0,99)) + " "
        job_position = ( greeting +job['POSITION']) if (len( greeting +job['POSITION']) < 117) else job['POSITION'][0:115]
        line = job_position + " " + job['JOBURL'] 
        api.update_status(status=line)
        sleep(60* randint(1,10))#every 10 minutes
        """
        try:
            api.update_status(status=line)
        except:
            print('Did I send the tweet?')
        pass
        """

def job_language(language="en"):
    """This will web scrape the website in French or English"""
    results = p.get_website_content(language) #Retrieves the full jobs description
    results = p.get_jobs(results) #retrieve all the jobs title and their url
    post_tweets(results, language)

if __name__ == '__main__':
    """ main function """
    job_language('en')
    job_language('fr')

