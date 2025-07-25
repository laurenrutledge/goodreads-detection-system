"""
data_cleaning.py
---------------
This file contains the script that cleans the Goodreads "read-in" / loaded dataset csv.
Specifically, the main pipeline of this file reads the loaded CSV produced by `load_data.py`,
applies cleaning steps, and saves a cleaned CSV in the loaded_and_cleaned directory.

Author: Lauren Rutledge
Created: July 2025
"""

import os
import sys

# Ensure we can import from src
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

import pandas as pd

from src.data_cleaning import (
    filter_valid_reviews,
    drop_duplicate_reviews,
    filter_english_reviews,
    save_cleaned_csv
)

from src.data_loading import extract_genre  # to re-extract genre from path

# ===== CONFIG =====
INPUT_FILE = os.path.join(PROJECT_ROOT, "datasets", "loaded_and_cleaned", "goodreads_reviews_mystery_thriller_crime_loaded.csv")
OUTPUT_DIR = os.path.join(PROJECT_ROOT, "datasets", "loaded_and_cleaned")

# ---------------------------------------------------------------------------
def main():
    """
    The function loads in the loaded data from one of the genre files and cleans the data
    to prepare for processing / feature engineering. Specifically, this file:
      1. Loads the intermediate CSV
      2. Filters for valid free-text reviews
      3. Drops duplicate reviews
      4. Filter to English reviews
      5. Save cleaned CSV
    """

    # Load the intermediate CSV
    df = pd.read_csv(INPUT_FILE)
    print(f"Loaded intermediate CSV with {len(df)} rows.")

    # Apply cleaning steps
    df = filter_valid_reviews(df)
    print(f"After filtering empty/invalid reviews: {len(df)} rows.")

    df = drop_duplicate_reviews(df)
    print(f"After dropping duplicates: {len(df)} rows.")

    df = filter_english_reviews(df)
    print(f"After filtering to English: {len(df)} rows.")

    # Determine genre from filename
    genre = extract_genre(INPUT_FILE)

    # Save cleaned CSV
    output_path = save_cleaned_csv(df, genre, output_dir=OUTPUT_DIR)
    print(f"Cleaned data saved to: {output_path}")


if __name__ == "__main__":
    main()