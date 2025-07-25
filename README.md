# A Quality Detection System for Book Reviews Posted on Goodreads

---

## Overview
This project presents the foundation of an automated system for assessing the quality of book reviews collected from Goodreads, a widely used, public online book review platform.

Leveraging a large, publicly available dataset of free-text reviews written by Goodreads' end-users, interpretable linguistic and metadata features were extracted to first train a multinomial logistic regression model that classifies reviews into “quality levels.” This metadata‑driven baseline model was selected initially due to practical time and compute constraints, offering a fast, interpretable, and resource‑efficient method to begin exploring review quality at scale.

Current and ongoing work is focused on integrating transformer‑based models (starting with BERT) to directly analyze raw text for semantic depth, coherence, and contextual richness. Thereafter, future directions will include incorporating human‑labeled data to further refine model performance and experimenting with additional NLP architectures.



## Problem Statement: 
The goal is to design and implement a system that can effectively analyze free-text book reviews, and: 
1. Identify and flag malicious or inappropriate reviews, and
2. Highlight and prioritize high‑quality, informative contributions over lower-quality reviews

This project confronts this challenge by analyzing Goodreads’ free‑text review data to detect and categorize review quality issues based on:
- Rule‑based heuristics, 
- Feature engineering, and 
- Natural language processing (NLP) 

While this project currently focuses on the Goodreads review platform, the system is designed to be scalable and adaptable for other review platforms in the future.


## Project Scope, Dataset, Assumptions, and Target Users: 

### Scope: 
Due to the time and computational constraints of this project, the current implementation focuses exclusively on analyzing and evaluating the quality of user‑generated free-text book reviews within the Goodreads platform.

The system is designed to detect and categorize quality issues, which are organized into two tiers: 
1. Tier One: Reviews containing what is likely malicious content, such as harmful links, spam, or self‑promotional material.
2. Tier Two: Reviews scored on a "quality scale" based on substantiveness and appropriateness.

### Dataset: 
The raw datasets used in this project are based on user reviews that were assembled and introduced in prior research, specifically:
- Wan et al., 2018 (Monotonic Attention Networks for Contextual Word Representations).
- Wan et al., 2019 (Spoiler Detection in Movie Reviews).

The actual data referenced and processed in this project was pulled from Julian McAuley’s publicly available Goodreads dataset (goodreads_reviews_dedup.json.gz), which can be accessed here:
https://cseweb.ucsd.edu/~jmcauley/datasets/goodreads.html#datasets

The following key fields were then extracted from the raw dataset:

- user_id – anonymized identifier for the user
- review_id – anonymized identifier for the review
- review_text – free‑text content of the review
- rating – star rating (typically 1–5)
- date_added – timestamp of when the review was posted 
- n_votes – number of votes or “helpful” marks from other users

During pre-processesing, only reviews with non‑empty review_text and valid user_id, review_id, and date_added were retained. Non‑English reviews were also removed prior to processing via langdetect.

### Assumptions: 
The following assumptions were made in order to scope and implement this iteration of the project. Ideally, assumptions will be removed as more time and computational constraints are granted toward this project:
- Data Availability: The datasets curated and published by Julian McAuley are assumed to be accurate, complete, and representative of Goodreads’ public review ecosystem. 
- Metadata Reliability: Fields such as \textbf{user\_id}, \textbf{review\_id}, \textbf{rating}, and \textbf{date\_added} are assumed to be correctly associated with each review and free from systemic errors.
- Static Dataset: The analysis is based on a static dataset collected in 2017, and it is assumed that trends and anomalies detected remain relevant to the current Goodreads platform.
- Scope of Content: Only free‑text reviews are considered. Any data entry that does not contain a free-text review was excluded from the scope. Multimedia content (images, videos) and non‑review interactions (likes, comments, etc.) are outside the scope of this project.
- Data Language: All reviews analyzed are in English, or in "English slang". Reviews written in other languages were removed, based on language detection using the \texttt{langdetect} library.
- Link Presence Indicates Spam or Malicious Content: Any review containing a hyperlink (e.g., starting with \texttt{http://}, \texttt{https://}, or including patterns such as \texttt{www.}, \texttt{.com}, \texttt{.org}, or \texttt{.net}) is assumed to be spam, promotional content, or potentially malicious. These reviews are therefore flagged and considered low‑quality, regardless of other factors.

### Target Users: 

The primary end‑users and key players that this project is geared towards include: 
- Content Moderators: Those responsible for reviewing and removing malicious, inappropriate, or low‑quality reviews. 
- Platform Managers: Those who maintain the overall integrity of the review ecosystem and inform decisions about platform policies and features.
- End‑Users (Review Readers): Goodreads users who benefit from a cleaner, more trustworthy set of reviews when making book selections.
- Authors: Book writers who utilize platforms such as Goodreads to gain more reliable feedback and insights from genuine, high‑quality reviews.


## Methods 

The objective of this project is to lay the foundation for a system that (1) automatically flags malicious or overtly problematic reviews and (2) distinguishes and elevates more informative, substantive reviews over low‑quality content. To implement this, feature engineering, and model implementations were carried out: 

### Feature Engineering: 

The feature engineering process was broken down into two tiers:  
- Tier One: Flag reviews containing hyperlinks using regex patterns (e.g., http://, www., .com, .org, .net).
- Tier Two: Compute linguistic & metadata features:
  - Sentence count
  - word count
  - Avg. words per sentence
  - Lexical diversity 
  - n_votes (as a social signal)
  - Interaction features (sentence–word, sentence–complexity, lexical–sentence, etc.).

All continuous features are standardized (zero mean, unit variance).

### Model(s): (s) since there are more to come!

**Model 1: Multinomial Logistic Regression**: 

Why Logistic Regression? 
- **Computational Efficiency**: Extremely important given the scope of this project and large datasets
- **Interpretability**: Feature coefficients
- **Robustness**: As a simpler baseline before more complex models (BERT)

Below shows further details of the model implemented in this repository: 
- Multinomial Logistic Regression with 5 quality levels (1–5)
- Train/test split: 80/20
- Metrics: Accuracy, Precision, Recall, F1 score, Confusion Matrix



## Repository Structure: 
```plaintext

goodreads-detection-system/
├── datasets/                                       # Raw, cleaned, and processed data (large files excluded from GitHub)
│
├── scripts/
│   ├── load_data.py                                # Load raw JSON to CSV
│   ├── clean_data.py                               # Clean data (filter, dedupe, language)
│   ├── run_feature_engineering_tier1.py            # Adds link-flag feature
│   ├── run_feature_engineering_tier2.py            # Adds NLP-based features (sentence/word counts, lexical diversity, etc.)
│   ├── feature_engineer_labeling.py                # Adds interaction/ratio features and assigns substantiveness labels
│   ├── logistical_regression.py                    # Trains and evaluates a multinomial logistic regression model
│   ├── run_eda.py                                  # Exploratory data analysis
│   └── __init__.py
│
├── src/
│   ├── data_loading.py                             # Functions for loading data
│   ├── data_cleaning.py                            # Functions for cleaning data
│   ├── feature_engineering_tier1.py                # Link-detection feature
│   ├── feature_engineering_tier2.py                # NLP-based feature functions
│   ├── feature_engineer_labeling.py                # Functions for interaction features and labeling
│   └── __init__.py
│
├── notebooks/                                      # Archived notebooks used in early design/testing
│
├── README.md                                       # Project documentation
├── requirements.txt                                # Dependencies required to install to replicate project
├── .gitignore                                      # Ignore rules for github maintanence (e.g., large raw data)
└── LICENSE                                         # Project license file

```

## How to Run: 

### 1. Set Up the Environment
Create and activate a Python 3.10 environment, then install dependencies from requirements.txt:

```sh
conda create -n goodreads-nlp python=3.10
conda activate goodreads-nlp
pip install -r requirements.txt
python -m spacy download en_core_web_sm   # required spaCy model
```

### 2. Prepare Input Data
- Place your raw Goodreads JSON Lines dataset(s) in:

```sh
./datasets/raw/
 ```
- For example:
```sh
./datasets/raw/goodreads_reviews_mystery_thriller_crime.json
```
  
### 3. Run the Processing Pipeline
Here, each step is modular and can be run independently.

From the project root, run:
(a) Load raw JSON to CSV:

```sh
python scripts/load_data.py
```

You should get an output file within the datasets directory that appears similar to the following: 

```sh
datasets/loaded_and_cleaned/goodreads_reviews_<genre>_loaded.csv
```

(b) Clean the data (filter blanks, dedupe, remove non-English): 

Run: 

```sh
python scripts/clean_data.py
```

You should get an output file within the datasets directory that appears similar to the following: 

```sh
datasets/cleaned/goodreads_reviews_<genre>_clean.csv
```

(c) Tier 1 Feature Engineering (link detection): 

Run: 
```sh
python scripts/run_feature_engineering_tier1.py
```

Output → datasets/processed/goodreads_reviews_<genre>_with_links_flag.csv


(d) Tier 2 Feature Engineering (NLP features): 
Run: 

```sh
python scripts/run_feature_engineering_tier2.py
```
Output → datasets/processed/goodreads_reviews_with_nlp_features_substantiveness_v2.csv


(e) Tier 2 Labeling (interaction features + substantiveness score): 
Run: 

```sh
python scripts/run_feature_engineering_tier2_labeling.py
```

Output → datasets/processed_and_labeled_for_training/goodreads_reviews_substantiveness.csv


(f) Train Logistic Regression Baseline: 
Run: 

```sh
python scripts/train_logistic_regression.py
```

Outputs:

Accuracy, Classification Report, Confusion Matrix (printed to console)

### 4. (Optional) Run EDA
To visualize distributions and relationships:

```sh
python python scripts/run_eda.py
```

---

## Results: 

```sh
| Label                | Precision | Recall | F1‑Score | Support | 🔎 Interpretation                                                                                        |
| -------------------- | --------- | ------ | -------- | ------- | -------------------------------------------------------------------------------------------------------- |
| **1 (low quality)**  | 0.78      | 0.81   | 0.80     | 70,812  | Very good detection of low‑quality reviews.                                                            |
| **2**                | 0.76      | 0.66   | 0.70     | 65,091  | Recall is lower; many true “2”s are being predicted as something else (likely confusion with 1 or 3). |
| **3 (mid quality)**  | 0.69      | 0.69   | 0.69     | 66,404  | Balanced performance; still room to improve.                                                           |
| **4**                | 0.67      | 0.62   | 0.64     | 61,359  | Lower recall: the model struggles to identify some 4’s (maybe confusing them with 3’s or 5’s).        |
| **5 (high quality)** | 0.78      | 0.91   | 0.84     | 63,114  | Excellent detection of high‑quality reviews.                                                           |
```

Confusion Matrix Insights: 
```sh
Predicted →
True ↓     1     2     3     4     5
1       57597  8492  3642   611   470
2       15157 42636  3501  3453   344
3        1047  4948 45692 11344  3373
4          27     2 10952 38157 12221
5           0     0  2432  3459 57223
```

Key observations:
- Strong diagonal for 1 and 5: class 1 and 5 have high recall (81% and 91%) and low confusion.

- Mix between 2 and 1: 15k true “2”s are being predicted as “1” → thresholds for low‑quality vs slightly better might need tuning or more nuanced features.

- Overlap between 3 and 4: 11k true “3”s predicted as “4” and 10k true “4”s predicted as “3”.

- These mid‑quality boundaries are hardest for a linear model to separate.

### Summary
Logistic Regression gives us a great baseline!
- Accuracy: 73.8%
- High quality (5): Excellent detection (Recall 91%)
- Low quality (1): Strong detection (Recall 81%)
- Mid classes (2/3/4): Some confusion—room to improve


#### References 

- Wan, et al. (2018), Monotonic Attention Networks for Contextual Word Representations.
- Wan, et al. (2019), Spoiler Detection in Movie Reviews.
- Julian McAuley’s Goodreads dataset: Dataset Portal

---
#### Author:
Lauren Rutledge    
July 2025