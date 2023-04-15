from transformers import pipeline
import matplotlib.pyplot as plt
from wordcloud import WordCloud

sentiment_pipeline = pipeline("sentiment-analysis")

def get_sentiment_score(text):
    sentiment = sentiment_pipeline(text)
    sentiment['score'] *= 100
    sentiment['score'] = int(sentiment['score'] * 100) / 100
    return sentiment
    
def generate_word_cloud(text):
    wordcloud = WordCloud().generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.figure()
    plt.axis("off")
    plt.show()

def generate_matplotlib_graph(data):
    sentimentScores = [get_sentiment_score(text)['score'] for text in data]
    xCoords = [i for i in range(len(data))]
    
    fig, ax = plt.subplots()
    
    fig.plot(xCoords, sentimentScores)
    
    return fig

