# Simple Sentiment Analysis

## Local Setup

Fork and clone this repo.

Create and activate a virtual environment:

```
python3 -m venv .venv
source .venv/bin/activate
```

You will know the environment is activated because your command prompt will be prepended by `(.venv)`.

Install the packages (`python` becomes an alias for `python3` because the virtual environment is activated):

```
python -m pip install -r requirements.txt
```

When you are done with exploring this project, deactivate your virtual environment:

```
deactivate
```


## Run the demo

The demo will output tuples of sample sentences with their corresponding sentiments.

```
python main.py
```

## Acknowledgement

This project uses the pretrained VADER sentiment analysis tool included in NLTK.

> Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.