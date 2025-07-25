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
├── datasets/                                   # Raw, cleaned, and processed data (large files excluded from GitHub)
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
├── notebooks/                                  # Archived notebooks used in early design/testing
│
├── README.md                                   # Project documentation
├── requirements.txt                            # Dependencies required to install to replicate project
├── .gitignore                                  # Ignore rules for github maintanence (e.g., large raw data)
└── LICENSE                                     # Project license file



```

## How to Run: 

### 1. Set Up the Environment
- First, activate a Conda environment and install the required dependencies:

```sh
conda create --name python=3.10 ? 
pip install -r requirements.txt
conda activate goodreads-nlp
```

---

### References 

- Wan, et al. (2018), Monotonic Attention Networks for Contextual Word Representations.
- Wan, et al. (2019), Spoiler Detection in Movie Reviews.
- Julian McAuley’s Goodreads dataset: Dataset Portal

---
### Author:
Lauren Rutledge    
July 2025