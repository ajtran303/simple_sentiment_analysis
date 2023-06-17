from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

def get_compound_score(text):
    return sia.polarity_scores(text)['compound']

def analyze_compound_score(score):
    if score >= 0.05:
        return 'positive sentiment'
    elif 0.05 > score >-0.05:
        return 'neutral sentiment'
    elif score <= -0.05:
        return 'negative sentiment'

if __name__ == '__main__':
    dataset = [
        "I love this product!",
        "The movie was amazing.",
        "The food at that restaurant is terrible.",
        "I feel disappointed with the service.",
        "This book is a masterpiece.",
        "The customer support was really helpful.",
        "I can't stand the traffic in this city.",
        "The concert exceeded my expectations.",
        "The weather ruined our plans for the day.",
        "I had a terrible experience with that company.",
        "The performance was outstanding!",
        "I'm so grateful for their assistance.",
        "The product failed to meet my expectations.",
        "I'm absolutely thrilled with the outcome.",
        "The hotel was a complete disaster.",
        "The quality of the product is top-notch.",
        "The service was prompt and efficient.",
        "I was pleasantly surprised by their performance.",
        "The app crashes frequently, very frustrating.",
        "I highly recommend this restaurant."
    ]

    dataset_scores = [(sentence, analyze_compound_score(get_compound_score(sentence))) for sentence in dataset]

    for data in dataset_scores:
        print(data)
