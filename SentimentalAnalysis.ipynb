{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter The Keyword:Nisarg\n",
      "Positive tweets percentage: 26.923076923076923 %\n",
      "Negative tweets percentage: 9.615384615384615 %\n",
      "Neutral tweets percentage: 63.46153846153846 %\n",
      "Pie-Chart representation:\n",
      "\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 432x288 with 0 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import re \n",
    "import tweepy \n",
    "from tweepy import OAuthHandler \n",
    "from textblob import TextBlob \n",
    "import matplotlib.pyplot as plt\n",
    "query = input(\"Enter The Keyword:\")\n",
    "\n",
    "class TwitterClient(object): \n",
    "\n",
    "\tdef __init__(self): \n",
    "\n",
    "\t\tconsumer_key = 'Hi0hmJvJcUUxmtl0XL5tp0mjG'\n",
    "\t\tconsumer_secret = 'ce2U4Czd05cKJpURhhCwVqACoW7u27wfcYvbE4fESPQdt0NMq7'\n",
    "\t\taccess_token = '707077794455429120-WB1PlMIomZOXkS4kB6gz0itt76ETlnc'\n",
    "\t\taccess_token_secret = 'XY0JoWthhpg6bWZ6zsgiQHKEJkx0TtjEaZuNjUiyV1umb'\n",
    "\n",
    "\t\ttry: \n",
    "\t\t\tself.auth = OAuthHandler(consumer_key, consumer_secret) \n",
    "\t\t\tself.auth.set_access_token(access_token, access_token_secret) \n",
    "\t\t\tself.api = tweepy.API(self.auth) \n",
    "\t\texcept: \n",
    "\t\t\tprint(\"Error: Authentication Failed\") \n",
    "\n",
    "\tdef clean_tweet(self, tweet): \n",
    "\n",
    "\t\treturn ' '.join(re.sub(\"(@[A-Za-z0-9]+)|([^0-9A-Za-z \\t])|(\\w+:\\/\\/\\S+)\", \" \", tweet).split()) \n",
    "\n",
    "\tdef get_tweet_sentiment(self, tweet): \n",
    "\n",
    "\t\tanalysis = TextBlob(self.clean_tweet(tweet)) \n",
    "\n",
    "\t\tif analysis.sentiment.polarity > 0: \n",
    "\t\t\treturn 'positive'\n",
    "\t\telif analysis.sentiment.polarity == 0: \n",
    "\t\t\treturn 'neutral'\n",
    "\t\telse: \n",
    "\t\t\treturn 'negative'\n",
    "\n",
    "\tdef get_tweets(self, query, count = 10): \n",
    "\n",
    "\t\ttweets = [] \n",
    "\n",
    "\t\ttry: \n",
    "\n",
    "\t\t\tfetched_tweets = self.api.search(q = query, count = count) \n",
    "\t\t\tfor tweet in fetched_tweets: \n",
    "\n",
    "\t\t\t\tparsed_tweet = {} \n",
    "\t\t\t\tparsed_tweet['text'] = tweet.text \n",
    "\t\t\t\tparsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text) \n",
    "\n",
    "\t\t\t\tif tweet.retweet_count > 0: \n",
    "\t\t\t\t\tif parsed_tweet not in tweets: \n",
    "\t\t\t\t\t\ttweets.append(parsed_tweet) \n",
    "\t\t\t\telse: \n",
    "\t\t\t\t\ttweets.append(parsed_tweet) \n",
    "\n",
    "\t\t\treturn tweets \n",
    "\n",
    "\t\texcept tweepy.TweepError as e: \n",
    "\t\t\tprint(\"Error : \" + str(e)) \n",
    "\n",
    "def main(): \n",
    "\n",
    "\tapi = TwitterClient() \n",
    "\ttweets = api.get_tweets(query, count = 500) \n",
    "\n",
    "\n",
    "\tptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']  \n",
    "\tprint(\"Positive tweets percentage: {} %\".format(100*len(ptweets)/len(tweets))) \n",
    "\tntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative'] \n",
    "\tprint(\"Negative tweets percentage: {} %\".format(100*len(ntweets)/len(tweets))) \n",
    "\tprint(\"Neutral tweets percentage: {} %\".format(100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets))) \n",
    "\tptweetspie=100*len(ptweets)/len(tweets)\n",
    "\tntweetspie=100*len(ntweets)/len(tweets)\n",
    "\tneutraltweetspie = 100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets)\n",
    "\tsizes = [ptweetspie, ntweetspie, neutraltweetspie]\n",
    "\tlabels = 'Positive Tweets', 'Negative Tweets', 'Neutral Tweets'\n",
    "\texplode = (0, 0.1, 0.1)\n",
    "\tfig1, ax1 = plt.subplots()\n",
    "\tax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',\n",
    "        shadow=True, startangle=90)\n",
    "\tax1.axis('equal')  \n",
    "\tprint(\"Pie-Chart representation:\\n\")\n",
    "\tplt.show()\n",
    "\tplt.savefig('pie.jpeg')\n",
    "\n",
    "if __name__ == \"__main__\": \n",
    "\n",
    "\tmain() \n",
    "    \n",
    "    \n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
