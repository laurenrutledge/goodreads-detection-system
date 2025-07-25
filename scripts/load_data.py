"""
data_loading.py
---------------
This file contains the scripts that load the raw Goodreads JSON lines file and
extracts a subset of the relevant columns and save them into an initial snapshot, which
is saved into an intermediate CSV for further processing.

This script also prints basic info for sanity checks along the way.

Author: Lauren Rutledge
Created: July 2025
"""

import os
import sys

# Dynamically get the project root (one directory up from scripts/)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from src.data_loading import extract_genre, load_raw_json

RAW_FILE_PATH = os.path.join(PROJECT_ROOT, "datasets", "raw", "goodreads_reviews_mystery_thriller_crime.json")

# Other available datasets (commented out for now)
# RAW_FILE_PATH = os.path.join(PROJECT_ROOT, "datasets", "raw", "goodreads_reviews_children.json")
# RAW_FILE_PATH = os.path.join(PROJECT_ROOT, "datasets", "raw", "goodreads_reviews_comics_graphic.json")
# RAW_FILE_PATH = os.path.join(PROJECT_ROOT, "datasets", "raw", "goodreads_reviews_fantasy_paranormal.json")
# RAW_FILE_PATH = os.path.join(PROJECT_ROOT, "datasets", "raw", "goodreads_reviews_history_biography.json")
# RAW_FILE_PATH = os.path.join(PROJECT_ROOT, "datasets", "raw", "goodreads_reviews_poetry.json")
# RAW_FILE_PATH = os.path.join(PROJECT_ROOT, "datasets", "raw", "goodreads_reviews_romance.json")
# RAW_FILE_PATH = os.path.join(PROJECT_ROOT, "datasets", "raw", "goodreads_reviews_young_adult.json")

OUTPUT_DIR = os.path.join(PROJECT_ROOT, "datasets", "loaded_and_cleaned") # where to save after loading



REQUIRED_COLUMNS = [
    "user_id",
    "review_id",
    "review_text",
    "rating",
    "date_added",
    "n_votes",
]


## MAIN FUNCTION CALLS:
def main():

    """
    The function loads in the raw data from one of the many files above.
    Specifically, the function, in this order:
      1. Extracts currently working genre from the input file name.
      2. Loads JSON Lines into a DataFrame, keeping only required columns.
      3. Prints the dataset shape and preview.
      4. Saves the loaded DataFrame to an intermediate CSV in the datasets/loaded_and_cleaned folder
    """

    # Ensure output folder exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Extract genre from filename
    genre = extract_genre(RAW_FILE_PATH)
    print(f"Genre extracted: {genre}")

    # Load JSON Lines file
    df = load_raw_json(RAW_FILE_PATH, required_columns=REQUIRED_COLUMNS)
    print(f"Loaded raw file with {len(df)} rows and {len(df.columns)} columns")

    # Show a preview of the JSON lines
    print("\n--- Sample Rows ---")
    print(df.head())

    # Save to intermediate CSV in datasets/loaded_and_cleaned directory
    output_path = os.path.join(OUTPUT_DIR, f"goodreads_reviews_{genre}_loaded.csv")
    df.to_csv(output_path, index=False)
    print(f"Saved loaded data snapshot to: {output_path}")


# Run main() only if this script is executed directly
if __name__ == "__main__":
    main()