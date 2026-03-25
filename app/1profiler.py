import pandas as pd
import numpy as np
from datetime import datetime
"""
Module 1 — Data Profiler
Reads CSV or Excel files and produces a full column-level profile:
  - Data type classification
  - Missing value counts & percentages
  - Basic stats (mean, median, std, min, max, range) for numeric columns
  - Unique value counts and top values for categorical columns
"""

def detect_column_types(df: pd.DataFrame) -> dict:
    """
    Detect the semantic type of each column in a DataFrame.
    
    Returns a dict mapping column name -> detected type:
      'numeric', 'categorical', 'datetime', 'boolean', 'string', 'unknown'
    """
    results = {}

    for col in df.columns:
        series = df[col].dropna()

        if series.empty:
            results[col] = "unknown"
            continue

        # --- Boolean ---
        if pd.api.types.is_bool_dtype(series):
            results[col] = "boolean"

        # --- Numeric ---
        elif pd.api.types.is_numeric_dtype(series):
            results[col] = "numeric"

        # --- Datetime ---
        elif pd.api.types.is_datetime64_any_dtype(series):
            results[col] = "datetime"

        # --- Object / string columns — needs deeper inspection ---
        elif pd.api.types.is_object_dtype(series):
            # Try parsing as datetime
            try:
                pd.to_datetime(series.sample(min(50, len(series))), infer_datetime_format=True)
                results[col] = "datetime"
                continue
            except Exception:
                pass

            # Boolean-like strings
            bool_values = {"true", "false", "yes", "no", "1", "0", "t", "f", "y", "n"}
            if set(series.str.lower().unique()).issubset(bool_values):
                results[col] = "boolean"
                continue

            unique_ratio = series.nunique() / len(series)

            # Low cardinality → categorical, everything else → string
            if series.nunique() <= 20 or unique_ratio < 0.05:
                results[col] = "categorical"
            else:
                results[col] = "string"

        else:
            results[col] = "unknown"

    return results

def missing_data_percentage(df) -> dict:
    missing = {}
    
    for col in df.columns:
        total_rows = len(df)
        missing_count = df[col].isna().sum()
        
        if missing_count > 0:
            percentage = (missing_count / total_rows) * 100
            percentage = round(percentage, 2)
            missing[col] = percentage
    
    return missing