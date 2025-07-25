"""
data_cleaning.py
---------------
This file contains the all functions that are accessed by scripts/load_data.py:
Each of the functions here clean the loaded Goodreads dataset. Specifically, there is a
function for each of the following:

- Remove empty or invalid review_text
- Drop rows with missing required fields
- Drop duplicate reviews
- Filter to English-language reviews
- Save cleaned data
Author: Lauren Rutledge
Created: July 2025
"""



import pandas as pd
import os
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0  # deterministic

def filter_valid_reviews(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove rows where `review_text` is null/empty/whitespace
    and drop rows with missing `user_id`, `review_id`, or `date_added`.
    """
    df = df[df['review_text'].notnull()]
    df = df[df['review_text'].str.strip() != '']
    df = df.dropna(subset=['user_id', 'review_id', 'date_added'])
    return df

def drop_duplicate_reviews(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate reviews with same user_id, review_id, and review_text.
    """
    return df.drop_duplicates(subset=['user_id', 'review_id', 'review_text'])

def review_is_english(text: str) -> bool:
    """
    Returns True if the first 200 chars of the text review is detected as English ('en').
    Empty strings are considered True (assumes filtered earlier).
    """
    if not text or text.isspace():
        return True
    try:
        return detect(text[:200]) == 'en'
    except:
        return False

def filter_english_reviews(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filter DataFrame rows to only those whose `review_text` is English.
    """
    mask = df['review_text'].apply(review_is_english)
    return df[mask]

def save_cleaned_csv(df: pd.DataFrame, genre: str, output_dir: str = "datasets/cleaned") -> str:
    """
    Save cleaned DataFrame to a CSV file in the specified output_dir.

    Returns the path to the saved file.
    """
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"goodreads_reviews_{genre}_clean.csv")
    df.to_csv(output_path, index=False)
    return output_path