# Twitter-Sentimental-Analysis
Twitter Sentimental Analysis is a project based on NLP (Natural Language Processing ) which uses different python library to analyse the the tweets after inputing a keyword it categorize into 3 categories positive,negative and neutral.
# Problem statement :
Given a keyword we need analyse the tweets related to the keyword (for e.g. bitcoin so tweets would be analysed and seprated into 3 different categories postive,negative and neutral) ,so we need to identify the sentiment of that keyword in public.
# Aprpoach :
This was fairly a simple problem as we fetched the twitter data using twitter api which fetches the live data and we can control the number of tweets to be analysed.Using tweepy library we fetch the data and using another library textBlob we analyse the data which is NLP in which it tokenises the sentence into words and number them
# Concept used :
Concept used here was bag of words after tokenising the sentwnce we remove stop words (which is less useful words or special symbol required e.g. /,.,;) after that there are 3 different bags made of postive , negative and neutral which is then trained and machine can recognize any tweet on basis of it the majority of of used sentiment if postive would be considered as postive comment.
# Representation :
We represent our result in the form of both pychart and numerical percentage.
