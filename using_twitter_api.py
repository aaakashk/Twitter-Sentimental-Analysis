from textblob import TextBlob
import tweepy
from matplotlib import pyplot as plt

def authenticate():
    try:
        file = open("/Users/akashkumar/Codes/Python/Twitter_Sentimental_Analysis/keys.txt", "r")
        keys = file.read().splitlines()
        api_key = keys[0]
        api_key_secret = keys[1]
        access_token = keys[2]
        access_token_secret = keys[3]
        file.close()
    except FileNotFoundError as fnf_error:
        print("File Not Found: ", fnf_error)

    else:
        try:
            auth_handler = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_key_secret)
            auth_handler.set_access_token(access_token, access_token_secret)
        except tweepy.Unauthorized as u_error:
            print("Could not authorize you", u_error)
        except tweepy.TooManyRequests as tmr_error:
            print("Too many requests", tmr_error)
        except tweepy.HTTPException as error:
            print("HTTP Error:", error)
        else:
            api = tweepy.API(auth_handler)
            return api 

def get_tweets(api, search_term= "cricket", tweets_limit= 100):
    tweets = tweepy.Cursor(api.search_tweets, q=search_term, lang='en').items(tweets_limit)
    return tweets

def result(tweets):
    positive = 0
    negative = 0
    neutral = 0

    for tweet in tweets:
        final_text = tweet.text.replace('RT', '')
        if(final_text.startswith('#')):
            position = final_text.index(':')
            final_text = final_text[position+2:]
        if(final_text.startswith('@')):
            position = final_text.index(' ')
            final_text = final_text[position+2:]
        analysis = TextBlob(final_text)
        tweet_polarity = analysis.polarity
        if tweet_polarity > 0:
            positive += 1
        elif tweet_polarity < 0:
            negative += 1
        else:
            neutral += 1

    print(f'Positive tweets = {positive}')
    print(f'Negative tweets = {negative}')
    print(f'Neutral tweets = {neutral}')
    return [positive, negative, neutral]

def pie_chart(numbers):
    labels = ['positive', 'negative', 'neutral']
    plt.pie(numbers, labels= labels, autopct= '%1.1f%%')
    plt.title('reviews')
    plt.tight_layout()
    plt.show()

def bar_chart(numbers):
    labels = ['positive', 'negative', 'neutral']
    plt.bar(labels, numbers, width= 0.4)
    plt.title('Bar Chart')
    plt.xlabel('Type')
    plt.ylabel('Number of tweets')
    plt.show()

def main():
    api = authenticate()    
    tweets = get_tweets(api)
    numbers = result(tweets)
    pie_chart(numbers)
    bar_chart(numbers)

if __name__ == '__main__':
    main()