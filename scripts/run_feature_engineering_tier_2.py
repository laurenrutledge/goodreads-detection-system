"""
run_feature_engineering_tier_2.py
--------------------------------
This file contains the script that runs all tier 2 (NLP-based) feature engineering functions
 Specifically, the main pipeline of this file:

1. Loads processed CSV (with link flags from tier 1 engineering)
2. Adds sentence counts, word counts, lexical diversity, and mentions_person columns per review
3. Saves the new CSV with Tier 2 features to another csv


Author: Lauren Rutledge
Created: July 2025
"""

import os
import sys
import pandas as pd


# Ensure project root is on path so relative paths work
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from src.feature_engineering_tier_two import (
    count_sentences,
    count_words,
    avg_words_per_sentence,
    lexical_diversity,
    mentions_person,
)

INPUT_FILE = os.path.join(PROJECT_ROOT, "datasets", "feature_engineered", "goodreads_reviews_mystery_thriller_crime_clean_tier_one.csv")
OUTPUT_FILE = os.path.join(PROJECT_ROOT, "datasets", "feature_engineered", "goodreads_reviews_tier_two.csv")

# ---------------------------------------------------------------------


def main():
    print(f"Loading input file: {INPUT_FILE}")
    df = pd.read_csv(INPUT_FILE)
    print(f"Loaded dataset with {len(df)} rows")


    print(" Computing Tier 2 NLP features...")

    df['sentence_count'] = df['review_text'].apply(count_sentences)
    df['word_count'] = df['review_text'].apply(count_words)
    df['avg_words_per_sentence'] = df['review_text'].apply(avg_words_per_sentence)
    df['lexical_diversity'] = df['review_text'].apply(lexical_diversity)
    df['mentions_person'] = df['review_text'].apply(mentions_person)


    print("\n--- Sample of engineered features ---")
    print(df[['review_text', 'sentence_count', 'word_count',
              'avg_words_per_sentence', 'lexical_diversity', 'mentions_person']].head())


    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f" Saved Tier 2 feature-engineered dataset to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()