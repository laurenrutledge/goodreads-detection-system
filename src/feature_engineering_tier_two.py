"""
feature_engineering_tier_two.py
----------------------------
This file contains the tier 2 NLP-based feature engineering functions for
the free-text Goodreads reviews. As of now, this consists of the following functions:
- Function that counts number of sentences in a review
- Function that counts number of words in a review
- Function to calculate a review's average words per sentence
- A function that calculates a review's lexical diversity
- A function that can detect PERSON - named entities within a review.

More functions may be added in the future.

Author: Lauren Rutledge
Created: July 2025
"""

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import spacy

# Ensure punkt tokenizer is available
nltk.download('punkt', quiet=True)

# Load spaCy English model once
nlp = spacy.load("en_core_web_sm")

def count_sentences(text: str) -> int:
    """Return number of sentences in text."""
    return len(sent_tokenize(text)) if isinstance(text, str) else 0

def count_words(text: str) -> int:
    """Return number of words in text."""
    return len(word_tokenize(text)) if isinstance(text, str) else 0

def avg_words_per_sentence(text: str) -> float:
    """Return average words per sentence."""
    s = count_sentences(text)
    w = count_words(text)
    return (w / s) if s > 0 else 0.0

def lexical_diversity(text: str) -> float:
    """Return lexical diversity: unique words / total words."""
    if not isinstance(text, str):
        return 0.0
    words = [w.lower() for w in word_tokenize(text) if w.isalpha()]
    return len(set(words)) / len(words) if words else 0.0

def mentions_person(text: str) -> int:
    """
    Returns 1 if the review mentions at least one PERSON entity (via spaCy),
    otherwise 0.
    """
    if not isinstance(text, str) or not text.strip():
        return 0
    doc = nlp(text)
    return int(any(ent.label_ == "PERSON" for ent in doc.ents))