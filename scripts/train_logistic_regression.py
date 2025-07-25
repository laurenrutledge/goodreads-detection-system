"""
train_logistic_regression.py
----------------------------
This file contains the implementation of the multinomial logistic regression model
that is used on the processed Goodreads dataset to classify free-text book review
quality levels (1–5). Specifically, this script does the following:
1. Loads processed & labeled data
2. Selects features and target
3. Splits the dataset into a train/test (80-20)
4. Scales features
5. Trains the logistic regression model
6. Evaluates model with accuracy, a classification report, and a confusion matrix

More functions may be added in the future.

Author: Lauren Rutledge
Created: July 2025
"""

"""
train_logistic_regression.py
----------------------------
Trains a multinomial logistic regression model on the processed Goodreads dataset
to classify review quality levels (1–5).

Steps:
1. Load processed & labeled data
2. Select features and target
3. Split into train/test
4. Scale features
5. Train logistic regression
6. Evaluate model with accuracy, classification report, and confusion matrix

Author: Lauren Rutledge
Created: July 2025
"""


import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Ensure project root is in path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

# ----------------------------------------------------------------------
# Input file
INPUT_FILE = os.path.join(PROJECT_ROOT, "datasets", "processed_and_labeled_for_training", "goodreads_reviews_substantiveness.csv")

def main():

    # Load data
    print(f"Loading dataset: {INPUT_FILE}")
    df = pd.read_csv(INPUT_FILE)
    print(f"Loaded dataset with {len(df)} rows")

    # Filter out rows with links (if not already done)
    df = df[df['contains_link'] == False].copy()
    print(f"Rows after filtering links: {len(df)}")
    print("Label distribution:\n", df['substantiveness_label'].value_counts())

    # Features and target
    features = [
        'n_votes',
        'sentence_count',
        'word_count',
        'avg_words_per_sentence',
        'lexical_diversity',
        'sentence_word_interaction',
        'sentence_avgword_interaction',
        'lexical_sentence_interaction',
        'words_per_sentence_ratio',
        'unique_words_per_sentence'
    ]

    X = df[features]
    y = df['substantiveness_label']

    # Split train/test 80/20
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Scale the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train logistic regression
    print("Training Logistic Regression model now.")
    log_reg = LogisticRegression(max_iter=1000, solver='lbfgs', multi_class='multinomial')
    log_reg.fit(X_train_scaled, y_train)

    # Predictions
    y_pred = log_reg.predict(X_test_scaled)

    # Metrics
    print("\nEvaluation Metrics")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

if __name__ == "__main__":
    main()
