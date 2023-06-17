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

def analyze_text_sentiment(text):
    score = get_compound_score(text)
    result = analyze_compound_score(score)
    return 'The text has a ' + result + '.'

if __name__ == '__main__':
    def _demo():
        dataset = [
            "I love this product!",
            "The food at that restaurant is terrible.",
            "I can't stand the traffic in this city.",
        ]

        results = [(sentence, analyze_text_sentiment(sentence)) for sentence in dataset]

        print('Simple Sentiment Analysis')
        print('Running demo:')
        print()

        for sentence, sentiment in results:
            print('    ', sentence)
            print('        ', sentiment)
            print()

    def _goodbye():
        print('Thanks and goodbye!')
        quit()

    _demo()

    print('Hint: type "quit" to exit!')
    print()

    EXIT_CONDITIONS = {'q', 'quit', 'exit'}

    while True:
        try:
            print('> Input text to analyze:')
            text = input().lower()

            if text in EXIT_CONDITIONS:
                _goodbye()
            else:
                print('    ', analyze_text_sentiment(text))
                print()
        except EOFError:
            _goodbye()
        except KeyboardInterrupt:
            _goodbye()
