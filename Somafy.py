import tweepy
import csv
auth = tweepy.auth.OAuthHandler(' INSERT TWITTER OAUTH KEY HERE ')
auth.set_access_token(' INSERT TWITTER ACCESS TOKEN HERE ',
               ' INSERT TWITTER ACCESS TOKEN HERE ')


api = tweepy.API(auth)
query="somadefcon"
csvFile = open('playlist.csv', 'a')
csvWriter = csv.writer(csvFile)
for tweet in tweepy.Cursor(api.search,
              query,
              #rpp=100,
              #page=100,
              lang="en").items():
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])
    print tweet.created_at, tweet.text
csvFile.close()
