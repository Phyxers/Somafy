import tweepy
import csv
auth = tweepy.auth.OAuthHandler('q1PEJokzTBYsmzTWyX2lXpL7F',
               'NSzHIhtWCDHBFHEYCY0iNvblsnkE48Zw0x3D0CE0myK9qUGLAY')
auth.set_access_token('1072932674-C3xwAXsSUdZAGIVmMLiGh7wvfXQ5Ilii92JXuCt',
               'w4IoFPs9GlGPcYFHtTtGh6kDrGPjd8lF8XXRhAUHxUr6Q')

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