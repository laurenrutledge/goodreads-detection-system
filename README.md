# A Quality Detection System for Book Reviews Posted on Goodreads

-----

## Overview: 
This project presents the foundation of an automated system for assessing the quality of free‑text book reviews collected from Goodreads.

Leveraging a large, publicly available dataset of free-text reviews written by Goodreads' end-users, interpretable linguistic and metadata features were extracted to first train a multinomial logistic regression model that classifies reviews into “quality levels.”

A metadata‑driven baseline model was selected initially due to practical time and compute constraints, offering a fast, interpretable, and resource‑efficient method to begin exploring review quality at scale.

Current and ongoing work is focused on integrating transformer‑based models (starting with BERT) to directly analyze raw text for semantic depth, coherence, and contextual richness. Thereafter, future directions will include incorporating human‑labeled data to further refine model performance and experimenting with additional NLP architectures.


### Background: 
Goodreads — a widely used online book review platform — hosts millions of user-created free-text book reviews that shape book discovery and reading trends today. While online free‑form book review platforms like Goodreads have become highly influential, it is increasingly clear that the sheer volume of content does not guarantee meaningful insight. Buried within millions of entries are countless reviews that contribute little value or even include spam, self‑promotion, or malicious links.  

This project confronts this challenge by analyzing Goodreads’ free‑text review data to detect and categorize review quality issues including text-rating inconsistencies, text informalities, and noisy helpless text reviews. To do so, the current iteration of this project uses a combination: 
- Rule‑based heuristics, 
- Feature engineering, and 
- Natural language processing (NLP) 

The result is a system that (1) automatically flags malicious or overtly problematic reviews and (2) distinguishes and elevates more informative, substantive reviews over low‑quality content. By filtering out noise and prioritizing meaningful contributions, this system strengthens the reliability of Goodreads data and lays a foundation for cleaner, more trustworthy free-text review ecosystems. 

### Problem Statement: 
The goal is to design and implement a system that can effectively analyze free-text book reviews, and: 
1. Identify and flag malicious or inappropriate reviews, and
2. Highlight and prioritize high‑quality, informative contributions over lower-quality reviews

While this project currently focuses on Goodreads, the system is designed to be scalable and adaptable for other review platforms in the future.


### Project Scope, Dataset, & Assumptions: 

#### Scope: 
Due to the time and computational constraints of this project, the current implementation focuses exclusively on analyzing and evaluating the quality of user‑generated free-text book reviews within the Goodreads platform.

The system is designed to detect and categorize quality issues, which are organized into two tiers: 
1. Tier One: Reviews containing what is likely malicious content, such as harmful links, spam, or self‑promotional material.
2. Tier Two: Reviews scored on substantiveness and appropriateness.

### Methods 

## Repository Structure: 
```plaintext

goodreads-detection-system/
├── datasets/
│   ├── raw/                                    # Raw Goodreads JSON files
│   ├── loaded_and_cleaned/                     # Loaded snapshots before cleaning
│   ├── cleaned/                                # Post-cleaning CSVs
│   └── processed/                              # Feature-engineered CSVs
│   ├── processed_and_labeled_for_training      # Post-cleaning CSVs
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
