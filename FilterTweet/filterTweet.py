import tweepy
import json
import csv
import tweepy
import re

def search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase):
    
    #create authentication for accessing Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    #initialize Tweepy API
    api = tweepy.API(auth)
    
    #get the name of the spreadsheet we will write to
    fname = '_'.join(re.findall(r"#(\w+)", hashtag_phrase))

    #open the spreadsheet we will write to
    with open('%s.csv' % (fname), 'w') as file:

        w = csv.writer(file)

        #write header row to spreadsheet
        w.writerow(['timestamp', 'tweet_text', 'username', 'all_hashtags', 'followers_count'])

        #for each tweet matching our hashtags, write relevant info to the spreadsheet
        for tweet in tweepy.Cursor(api.search, q=hashtag_phrase+' -filter:retweets', \
                                   lang="en", tweet_mode='extended').items(100):
            w.writerow([tweet.created_at, tweet.full_text.replace('\n',' ').encode('utf-8'), tweet.user.screen_name.encode('utf-8'), [e['text'] for e in tweet._json['entities']['hashtags']], tweet.user.followers_count])
    

  def filter_for_username(hashtag_phrase):
    
    fname = '_'.join(re.findall(r"#(\w+)", hashtag_phrase))
    # with read('%s.csv' % (fname), 'w') as file:
      
    with open('eggs.csv', newline='') as csvfile:
      spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
      for row in spamreader:
        print(', '.join(row))
          

consumer_key = "l5r2JUldwCupa3DDQLl671lhu"
consumer_secret = "gtN62JaWehSuLQueitKH3kz2z5JEp5UjqaOCw3yu2r00pqzkI3"
access_token = "2921319782-rVQsc8eQC5OW7cimj9vRdavL8F6vUpw4LlecTIl"
access_token_secret = "3zLYPqDgrZfazbXqHQDNxciYnTYPOkxSMcbcDeDuqL8du"
    
hashtag_phrase = input('Hashtag Phrase ')

if __name__ == '__main__':
    search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase)
    filter_for_username(hashtag_phrase)