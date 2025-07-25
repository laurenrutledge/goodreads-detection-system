"""
data_loading.py
---------------
This module is responsible for loading raw Goodreads data from JSON Lines files
and performing initial lightweight processing such as selecting required columns
and extracting metadata (e.g., genre from the filename).

Most functions in this file are accessed by scripts/load_data.py, which also contains
variables for the json files and the required columns that are being pulled.

Author: Lauren Rutledge
Created: July 2025
"""

import os
import pandas as pd

# ---------------------------------------------------------------------------
# Function: extract_genre
# ---------------------------------------------------------------------------
def extract_genre(file_path: str) -> str:
    """
    Extract the genre keyword from a Goodreads reviews filename.

    Parameters
    ----------
    file_path : str
        Full path to the raw JSON file, e.g.
        "datasets/raw/goodreads_reviews_mystery_thriller_crime.json".

    Returns
    -------
    str
        The genre string extracted from the filename,
        e.g. "mystery_thriller_crime".
    """
    base_name = os.path.basename(file_path)
    return os.path.splitext(base_name)[0].replace('goodreads_reviews_', '')

# ---------------------------------------------------------------------------
# Function: load_raw_json
# ---------------------------------------------------------------------------
def load_raw_json(file_path: str, required_columns: list[str] | None = None) -> pd.DataFrame:
    """
    This function loads a Goodreads reviews JSON Lines file into a pandas DataFrame.

    Parameters
    ----------
    file_path : str
        Path to the JSON Lines file (each line is a JSON object).
    required_columns : list of str, optional
        List of columns to keep from the raw file. If None, all columns are kept.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing either all raw columns or only the selected columns.
    """
    df = pd.read_json(file_path, lines=True)
    if required_columns:
        df = df[required_columns]
    return df
