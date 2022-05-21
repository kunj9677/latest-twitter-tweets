import tweepy
class SA:
    def __init__(self):
        self.tweets = None
        self.tweet_text = None

    def download_data(self):
        consumer_key = "MDMZGYzKk5SbVSE4emfQH3pSx"
        consumer_secret = "BBjosetus9mWgKkQRv0aufdCVNqTFjCEx6Ioh2CSIctMbrcHCn"
        access_token = "56099269-JX0spVGgeGzrzywM5xQAwgaGTv61Hc2PT3boYu617"
        access_token_secret = "AISZlKmDSCl32sWpgIjYmZkeDbwkaMex1sjWnk9VT8LTr"
        
        auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
        api = tweepy.API(auth)
        keyward = input("Enter Keyward: ")
        tweet_count = int(input("Enter No. of tweets you want to search: "))
        self.tweets = api.search_tweets(q=keyward, count=tweet_count)
        for tweet in self.tweets:
            print(tweet.text,end="\n\n")
t1 = SA()
t1.download_data()

        #public_tweets = api.home_timeline()
        #for tweet in public_tweets:
        #    print(tweet.text)
