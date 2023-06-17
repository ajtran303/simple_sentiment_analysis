# Simple Sentiment Analysis

## Features

- Get the VADER compound score of text
- Get the human-readable meaning of a compound score
- Get a human-readable sentiment analysis of text

### Roadmap / Wishlist

- Develop a function that analyzes the other components of the VADER score (neg, neu, pos) and outputs "flavor" that can be added to the compound score analysis.

## Local Setup

Fork and clone this repo.

### Virtual Environment

Create and activate a virtual environment:

```
python3 -m venv .venv
source .venv/bin/activate
```

You will know the environment is activated because your command prompt will be prepended by `(.venv)`.

Install the packages:

```
python3 -m pip install -r requirements.txt
```

## Run the program

```
python3 main.py
```

A demo will print out on the screen and then you will be prompted to input text. When you submit your text with the `enter` key, the program will analyze the sentiment and return a result.

For example:
```
> Input text to analyze:
I'm so grateful for their assistance!
    The text has a positive sentiment.
```
You can exit the program by submitting `q`, `quit`, or `exit` or using a keyboard command: `ctrl+D` or `ctrl+C`.

When you are done with exploring this project, deactivate your virtual environment. This will remove the packages that were installed:

```
deactivate
```

If you want to play with the code again, you will have to follow the steps again in the above section, "Virtual Environment."


## Acknowledgement

This project uses the pretrained VADER sentiment analysis tool included in NLTK.

> Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.