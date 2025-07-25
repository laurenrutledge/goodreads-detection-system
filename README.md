# A Quality Detection System for Book Reviews Posted on Goodreads


## Overview
This project presents the foundation of an automated system for assessing the quality of book reviews collected from Goodreads, a widely used, public online book review platform.

Leveraging a large, publicly available dataset of free-text reviews written by Goodreads' end-users, interpretable linguistic and metadata features were extracted to first train a multinomial logistic regression model that classifies reviews into “quality levels.” This metadata‑driven baseline model was selected initially due to practical time and compute constraints, offering a fast, interpretable, and resource‑efficient method to begin exploring review quality at scale.

Current and ongoing work is focused on integrating transformer‑based models (starting with BERT) to directly analyze raw text for semantic depth, coherence, and contextual richness. Thereafter, future directions will include incorporating human‑labeled data to further refine model performance and experimenting with additional NLP architectures.

--

## Problem Statement: 
The goal is to design and implement a system that can effectively analyze free-text book reviews, and: 
1. Identify and flag malicious or inappropriate reviews, and
2. Highlight and prioritize high‑quality, informative contributions over lower-quality reviews

This project confronts this challenge by analyzing Goodreads’ free‑text review data to detect and categorize review quality issues based on:
- Rule‑based heuristics, 
- Feature engineering, and 
- Natural language processing (NLP) 

While this project currently focuses on Goodreads, the system is designed to be scalable and adaptable for other review platforms in the future.


## Project Scope, Dataset, Assumptions, and Target Users: 

### Scope: 
Due to the time and computational constraints of this project, the current implementation focuses exclusively on analyzing and evaluating the quality of user‑generated free-text book reviews within the Goodreads platform.

The system is designed to detect and categorize quality issues, which are organized into two tiers: 
1. Tier One: Reviews containing what is likely malicious content, such as harmful links, spam, or self‑promotional material.
2. Tier Two: Reviews scored on substantiveness and appropriateness.

### Dataset: 
Raw data source: Julian McAuley’s Goodreads dataset (goodreads_reviews_.json.gz), which can be accessed via: https://cseweb.ucsd.edu/~jmcauley/datasets/goodreads.html#datasets

Key fields from raw dataset used:
- user_id 
- review_id
- review_text 
- rating 
- date_added 
- n_votes.

All non‑English reviews were removed prior to processing via langdetect.

### Assumptions: 
The following assumptions (as of now) were made in order to scope and implement this project within the given time and computational constraints:
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

The feature engineering process was broken down into two tiers to 
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

Model 1: Logistic regression, which was selected as the baseline model because of its  a which was necessary for the scope of this project.

- **Computational Efficiency**: Extremely important given the scope of this project and large datasets
- **Interpretability**: Feature coefficients
- **Robustness**: As a simpler baseline before more complex models (BERT)

Here, the model implementation was de
- Multinomial Logistic Regression with 5 quality levels (1–5)
- Train/test split: 80/20
- Metrics: Accuracy, Precision, Recall, F1 score, Confusion Matrix
- 



## Repository Structure: 
```plaintext

goodreads-detection-system/
├── datasets/                                   # All raw, cleaned, and processed datasets used and produced during this project. Details excluded as github cannot accomodate each dataset's size. 
│
├── scripts/
│   ├── load_data.py                            # Load raw JSON to CSV
│   ├── clean_data.py                           # Clean data (filter, dedupe, language)
│   ├── run_feature_engineering_tier1.py        # Adds link-flag feature
│   ├── run_eda.py                              # Exploratory data analysis
│   └── __init__.py
│
├── src/
│   ├── data_loading.py                         # Functions for loading data
│   ├── data_cleaning.py                        # Functions for cleaning data
│   ├── feature_engineering_tier1.py            # Link-detection feature
│   └── __init__.py
│
├── README.md                                   # Project documentation
├── requirements.txt                            # Dependencies required to install to replicate project
├── .gitignore                                  # Ignore rules for github maintanence (e.g., large raw data)
├── LICENSE                                     # Project license file
│
└── notebooks/                                  # Archived notebooks/scripts originally used in project design and testing, no longer used in current setup


```

## How to Run: 

### 1. Set Up the Environment
- First, activate a Conda environment and install the required dependencies:

```sh
conda create --name python=3.10 ? 
pip install -r requirements.txt
conda activate goodreads-nlp
