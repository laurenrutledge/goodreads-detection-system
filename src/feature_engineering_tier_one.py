"""
feature_engineering_tier_one.py
----------------------------
This file contains the tier 1 feature engineering functions for
the free-text Goodreads reviews. As of now, this consists of flagging
reviews that detect whether a review:
- contains a URL-like link.

More functions may be added in the future.

Author: Lauren Rutledge
Created: July 2025
"""

import pandas as pd
import re


def review_has_link(text: str) -> bool:
    """
    This function determines whether the given text contains a link (URL-like pattern).

    Parameters
    ----------
    text : str
        Free-form text from 'review_text' column.

    Returns
    -------
    bool
        True if a link-like pattern is found, False otherwise.
    """
    if pd.isna(text) or not isinstance(text, str):
        return False

    link_patterns_regex = [
        r'http[s]?://[^\s]+',   # http:// or https://
        r'www\.[^\s]+',         # www.something
        r'\b[^\s]+\.com\b',     # something.com as a whole word
        r'\b[^\s]+\.org\b',     # something.org as a whole word
        r'\b[^\s]+\.net\b',     # something.net as a whole word
    ]

    combined_pattern = "|".join(link_patterns_regex)
    return bool(re.search(combined_pattern, text, flags=re.IGNORECASE))

def add_link_flag(df: pd.DataFrame) -> pd.DataFrame:
    """
    This function adds a 'contains_link' boolean column to the DataFrame
    based on the 'review_text' column.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame with a 'review_text' column.

    Returns
    -------
    pd.DataFrame
        DataFrame with an added boolean 'contains_link' column.
    """

    df['contains_link'] = df['review_text'].apply(review_has_link)
    return df