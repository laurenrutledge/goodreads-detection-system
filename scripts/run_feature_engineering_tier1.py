"""
run_feature_engineering_tier1.py
--------------------------------
This file contains the script that runs all tier 1 feature engineering.
Specifically, the main pipeline of this file:
- Loads cleaned dataset
- Flags reviews that contain links
- Saves processed dataset with new column

Author: Lauren Rutledge
Created: July 2025
"""

import os
import sys

# Ensure we can import from src
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

import pandas as pd
from src.feature_engineering_tier_one import add_link_flag
from src.data_loading import extract_genre

# ===== CONFIG =====
INPUT_FILE = os.path.join(PROJECT_ROOT, "datasets", "cleaned", "goodreads_reviews_mystery_thriller_crime_clean.csv")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "datasets", "feature_engineered")

# ---------------------------------------------------------------------------
def main():
    """
    This function of this file is the main pipeline for Tier 1 feature engineering.
    In this order, the function:
      1. Loads cleaned dataset
      2. Flags reviews that appear to cnotain a links
      3. Saves processed dataset to the feature_engineered sub folder with new column containing
        boolean values
    """

    # Load cleaned data
    df = pd.read_csv(INPUT_FILE)
    print(f"Loaded cleaned dataset with {len(df)} rows")

    # Add link flag
    df = add_link_flag(df)
    print(f"Number of reviews containing links: {df['contains_link'].sum()}")

    # Inspect and print a few rows
    print(df[['review_text', 'contains_link']].head())

    # Save processed CSV
    genre = extract_genre(INPUT_FILE)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, f"goodreads_reviews_{genre}_tier_one.csv")
    df.to_csv(output_path, index=False)
    print(f"Saved processed dataset with link flag to: {output_path}")

    # : show first 5 flagged rows
    print(df[df['contains_link']][['review_text', 'contains_link']].head())


if __name__ == "__main__":
    main()