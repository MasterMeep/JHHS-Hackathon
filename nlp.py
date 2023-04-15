from transformers import pipeline
import matplotlib.pyplot as plt
from wordcloud import WordCloud

sentiment_pipeline = pipeline("sentiment-analysis")

def get_sentiment_score(text):
    sentences = text.split(".")
    total = 0
    for sentence in sentences:
        sentiment = sentiment_pipeline(sentence)
        if sentiment[0]['label'] == 'POSITIVE':
            total += sentiment[0]['score']
        elif sentiment[0]['label'] == 'NEGATIVE':
            total -= sentiment[0]['score']
        
    total = int(total* 10000)/100
    
    return total
    
def generate_word_cloud(text):
    wordcloud = WordCloud().generate(text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.figure()
    plt.axis("off")
    plt.show()

def generate_matplotlib_graph(data, dates):
    sentimentScores = [get_sentiment_score(text)['score'] for text in data]
    
    fig, ax = plt.subplots()
    
    fig.plot(dates, sentimentScores)
    
    return fig

print(get_sentiment_score("it was alright"))
