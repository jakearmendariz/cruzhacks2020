

import tweepy

auth = tweepy.OAuthHandler("l5r2JUldwCupa3DDQLl671lhu","gtN62JaWehSuLQueitKH3kz2z5JEp5UjqaOCw3yu2r00pqzkI3")
auth.set_access_token("2921319782-rVQsc8eQC5OW7cimj9vRdavL8F6vUpw4LlecTIl","3zLYPqDgrZfazbXqHQDNxciYnTYPOkxSMcbcDeDuqL8du")
api = tweepy.API(auth)

print("test")

tweets = api.home_timeline()
for tweet in tweets:
    print(tweet.text)