from tweepy.streaming import  StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables for Twitter API credentials
access_token = "1677445837-wsYS4aeOlZYmjhH6CEiIWnjGBe6xdscMF30C6Ni"
access_token_secret = "Dyos1nLjOjMxYg1XKJOTYA9ufidcj1EFMrpimVByN6ayx"
consumer_key = "hMcH6HhbLejdz5me3rKZcKVbS"
consumer_secret = "IAdBY55qZV6E6NOcoO8U5qwuzSjCbTj0gaQWMTHokj2ilFkuUb"

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status, "error")

if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])
