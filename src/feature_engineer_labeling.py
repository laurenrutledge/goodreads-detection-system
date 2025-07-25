"""
feature_engineering_tier2_labeling.py
-------------------------------------
This file contains the reusable functions required for the labeling phase leading into the
logistic classification training phase of this project.

The functions included in this file carry out the following:
- Extra interaction/ratio feature creations, which are then added to the dataset in columns
- Assigning a substantiveness label based on thresholds that were pre-determined in effort to
evenly split responses amongst the 5 "quality ratings"

Author: Lauren Rutledge
Created: July 2025
"""

import pandas as pd

def add_interaction_and_ratio_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add interaction and ratio features to the DataFrame.
    """

    df['sentence_word_interaction'] = df['sentence_count'] * df['word_count']
    df['sentence_avgword_interaction'] = df['sentence_count'] * df['avg_words_per_sentence']
    df['lexical_sentence_interaction'] = df['lexical_diversity'] * df['sentence_count']

    # Ratio-based features
    df['words_per_sentence_ratio'] = df['word_count'] / (df['sentence_count'] + 1e-5)
    df['unique_words_per_sentence'] = (df['lexical_diversity'] * df['word_count']) / (df['sentence_count'] + 1e-5)
    return df



def assign_substantiveness_label(row: pd.Series) -> int:
    """
    This function assign a substantiveness label (1–5) based on thresholds.
    The thresholds were determined after eda was performed to ensure that the text-reviews
    in the training/test dataset would be evenly split amongst the 5 quality scores.
    """
    sc = row['sentence_count']
    awps = row['avg_words_per_sentence']
    wc = row['word_count']
    ld = row['lexical_diversity']
    nv = row['n_votes']
    # mp = row['mentions_person']

    if sc > 3 and wc > 60 and awps > 13 and ld > 0.675 and nv >= 0: # and mp >= 1:
        return 5
    if sc > 3 and wc > 40 and awps > 11 and ld > 0.6 and nv >= 0:
        return 4
    if sc >= 2 and wc >= 35 and awps >= 9 and ld > 0.575 and nv >= 0:
        return 3
    if sc >= 2 and wc >= 17 and awps >= 7 and ld > 0.50 and nv > -0.05:
        return 2
    return 1
