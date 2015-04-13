import tweepy
auth = tweepy.auth.OAuthHandler('q1PEJokzTBYsmzTWyX2lXpL7F',
               'NSzHIhtWCDHBFHEYCY0iNvblsnkE48Zw0x3D0CE0myK9qUGLAY')
auth.set_access_token('1072932674-C3xwAXsSUdZAGIVmMLiGh7wvfXQ5Ilii92JXuCt',
               'w4IoFPs9GlGPcYFHtTtGh6kDrGPjd8lF8XXRhAUHxUr6Q')

api=tweepy.API(auth)
query = "somadefcon"
f = open('output.txt', 'w')
for tweet in tweepy.Cursor(api.search,
               query,
               count=100,
               result_type="recent",
               include_entities=True,
               lang="en").items():
    f.write(str(tweet.created_at) +'\n')
    f.write(tweet.text.encode('utf-8') + '\n')
    print tweet.created_at, tweet.text