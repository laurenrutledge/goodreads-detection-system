"""
run_feature_engineering_tier2_labeling.py
-----------------------------------------
This file loads Tier 2 processed data, removes link-containing reviews,
adds additional interaction/ratio features. Once all features are determined /
documented, this file runs through a series of functions that assigns each text
review a substantiveness label (a score between 1 and 5). Finally, this file
contains the function that saves the labeled dataset for model training.

Author: Lauren Rutledge
Created: July 2025
"""

import os
import sys
import pandas as pd

# Ensure project root is on path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from src.feature_engineer_labeling import add_interaction_and_ratio_features, assign_substantiveness_label

# Input and output paths
INPUT_FILE = os.path.join(PROJECT_ROOT, "datasets", "feature_engineered", "goodreads_reviews_tier_two.csv")
OUTPUT_FILE = os.path.join(PROJECT_ROOT, "datasets", "processed_and_labeled_for_training", "goodreads_reviews_substantiveness.csv")


def main():
    print(f" Loading input file: {INPUT_FILE}")
    df = pd.read_csv(INPUT_FILE)
    print(f" Loaded dataset with {len(df)} rows")

    # Remove entries with links
    print("Removing link-containing reviews...")
    df = df[df['contains_link'] == False].copy()
    print(f"Remaining rows after removal: {len(df)}")

    # Add interaction and ratio features
    print("Adding interaction and ratio features...")
    df = add_interaction_and_ratio_features(df)

    # Assign substantiveness labels
    print("Assigning substantiveness labels...")
    df['substantiveness_label'] = df.apply(assign_substantiveness_label, axis=1)
    print("Label distribution:\n", df['substantiveness_label'].value_counts())

    # Save output
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f" Saved labeled dataset to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
