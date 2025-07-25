"""
run_eda.py

This file contains the scripts that execute a preliminary exploratory data analysis
(EDA) on the cleaned Goodreads dataset.

In summary, this file contains scripts that print overview stats of the processed dataset
in addition to displaying a few plots.

Author: Lauren Rutledge
Created: July 2025
"""

import os
import sys

# ✅ Ensure we can import modules from project root if needed
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ===== CONFIG =====
INPUT_FILE = os.path.join(PROJECT_ROOT, "datasets", "feature_engineered", "goodreads_reviews_tier_two.csv")

# ---------------------------------------------------------------------------
def main():
    """
    Run EDA:
      1. Load processed CSV
      2. Print head/tail/info/shape
      3. Print describe() outputs
      4. Show histogram, boxplot, and pairplot for selected columns
    """

    # Load data
    df = pd.read_csv(INPUT_FILE)
    print(f"Loaded dataset: {INPUT_FILE}")
    print(f"Shape: {df.shape}\n")

    # Overview prints
    print("Head of data:")
    print(df.head(), "\n")

    print("Tail of data:")
    print(df.tail(), "\n")

    print("Info:")
    print(df.info(), "\n")

    print("Describe numeric:")
    print(df.describe(), "\n")

    print("Describe all columns:")
    print(df.describe(include='all'), "\n")

    # Plots
    print("Generating plots...")

    # Histogram for a numeric feature
    df['word_count'].hist(bins=30)
    plt.title("Histogram of Word Count")
    plt.xlabel("Word Count")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

    # Boxplot to detect outliers
    sns.boxplot(x=df['word_count'])
    plt.title("Boxplot of Word Count")
    plt.tight_layout()
    plt.show()

    # Pairwise plots of a few columns
    sns.pairplot(df[['n_votes', 'sentence_count', 'word_count', 'avg_words_per_sentence', 'lexical_diversity']])
    plt.suptitle("Pairplot of Selected Features", y=1.02)
    plt.show()

    print(" EDA complete.")


if __name__ == "__main__":
    main()