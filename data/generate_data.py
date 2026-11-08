"""
generate_data.py
================
Generates a synthetic dataset of ~2000 employees with burnout labels.
Columns:
    avg_daily_hours        : float  [6.0, 13.0]
    overtime_hours_week    : float  [0,  25]
    absence_days_month     : int    [0,   8]
    late_arrivals_month    : int    [0,  15]
    tasks_assigned         : int    [5,  40]
    vacation_days_last_year: int    [0,  25]
    burnout                : int    0 or 1  (target label)

Logic:
    A burnout score is computed from weighted features + noise.
    If score > threshold → burnout = 1, else 0.
    This ensures realistic class distribution (~35-40% burnout).
"""

import numpy as np
import pandas as pd
import random
import os

# ── Reproducibility ─────────────────────────────────────────────────────────
SEED = 42
np.random.seed(SEED)
random.seed(SEED)

N_EMPLOYEES = 1000

# ── Employee names pool (Arabic transliterated + common names) ───────────────
EMPLOYEE_NAMES = [
    "Ahmed Mohamed", "Mohamed Ali", "Omar Hassan", "Youssef Ibrahim",
    "Khaled Mahmoud", "Tariq Saeed", "Bilal Nasser", "Faris Amin",
    "Rami Younis", "Samir Fouad", "Nader Hamid", "Wael Karim",
    "Hassan Zaki", "Ayman Refaat", "Sherif Adel", "Bassam Tawfik",
    "Hossam Gamal", "Emad Saleh", "Ihab Mostafa", "Walid Nabil",
    "Layla Ahmed", "Nour Mohamed", "Sara Hassan", "Fatima Ibrahim",
    "Rania Khaled", "Dina Mahmoud", "Yasmine Saeed", "Mariam Nasser",
    "Hana Amin", "Salma Younis", "Amira Fouad", "Doaa Hamid",
    "Noha Wael", "Eman Karim", "Ghada Zaki", "Mona Refaat",
    "Heba Adel", "Nada Tawfik", "Reem Gamal", "Mai Saleh",
    "Adam Mostafa", "Ziad Nabil", "Karim Adly", "Mazen Fathy",
    "Sami Lotfy", "Tarek Wahid", "Ramzi Sobhy", "Galal Ezz",
    "Hazem Atef", "Shadi Raafat", "Nadine Hany", "Aya Sherif",
    "Rawan Essam", "Lina Ashraf", "Hoda Wafaa", "Rana Magdi",
    "Dalia Shawki", "Omnia Karam", "Engy Samir", "Rasha Ihab",
]

def generate_dataset(n: int = N_EMPLOYEES) -> pd.DataFrame:
    """Generate synthetic employee burnout dataset."""

    # ── Raw feature generation ───────────────────────────────────────────────
    avg_daily_hours = np.random.uniform(6.0, 13.0, n)
    overtime_hours_week = np.random.uniform(0, 25, n)
    absence_days_month = np.random.randint(0, 9, n)           # 0–8
    late_arrivals_month = np.random.randint(0, 16, n)         # 0–15
    tasks_assigned = np.random.randint(5, 41, n)              # 5–40
    vacation_days_last_year = np.random.randint(0, 26, n)     # 0–25

    # ── Burnout score formula (weights based on known risk factors) ──────────
    # Normalize each feature to 0-1 range first
    h_norm  = (avg_daily_hours - 6) / 7          # daily hours weight
    ot_norm = overtime_hours_week / 25            # overtime weight
    ab_norm = absence_days_month / 8             # absence weight
    la_norm = late_arrivals_month / 15           # late arrivals weight
    ta_norm = tasks_assigned / 40               # tasks weight
    vac_norm = vacation_days_last_year / 25      # vacation weight (INVERSE risk)

    # Weighted combination → burnout_score ∈ (0, 1)
    burnout_score_raw = (
        0.30 * h_norm
        + 0.25 * ot_norm
        + 0.15 * ab_norm
        + 0.10 * la_norm
        + 0.15 * ta_norm
        - 0.05 * vac_norm   # More vacation → less burnout risk
    )

    # Add noise to prevent overfitting
    noise = np.random.normal(0, 0.10, n)
    burnout_score_noisy = np.clip(burnout_score_raw + noise, 0, 1)

    # Binary label with threshold
    threshold = 0.50
    burnout_label = (burnout_score_noisy > threshold).astype(int)

    
    # ── Build name column (cycle through pool, add suffix to ensure uniqueness)
    names_col = []
    pool_size = len(EMPLOYEE_NAMES)
    for i in range(n):
        base = EMPLOYEE_NAMES[i % pool_size]
        if i >= pool_size:
            suffix = str(i // pool_size + 1)
            parts = base.split(" ")
            base = f"{parts[0]} {parts[1]} {suffix}" if len(parts) >= 2 else f"{base} {suffix}"
        names_col.append(base)

    # ── Assemble DataFrame ───────────────────────────────────────────────────
    df = pd.DataFrame({
        "employee_id":          [f"EMP{str(i+1).zfill(4)}" for i in range(n)],
        "name":                 names_col,
        "avg_daily_hours":      np.round(avg_daily_hours, 2),
        "overtime_hours_week":  np.round(overtime_hours_week, 2),
        "absence_days_month":   absence_days_month,
        "late_arrivals_month":  late_arrivals_month,
        "tasks_assigned":       tasks_assigned,
        "vacation_days_last_year": vacation_days_last_year,
        "burnout":              burnout_label,
    })

    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Basic data cleaning pipeline."""
    print(f"[Cleaning] Shape before: {df.shape}")

    # Drop duplicates (on feature columns only, ignore id)
    feature_cols = [
        "avg_daily_hours", "overtime_hours_week", "absence_days_month",
        "late_arrivals_month", "tasks_assigned", "vacation_days_last_year",
        "burnout"
    ]
    df = df.drop_duplicates(subset=feature_cols)

    # Drop rows with missing values (shouldn't exist for synthetic data)
    df = df.dropna()

    # Ensure correct dtypes
    df["absence_days_month"]     = df["absence_days_month"].astype(int)
    df["late_arrivals_month"]    = df["late_arrivals_month"].astype(int)
    df["tasks_assigned"]         = df["tasks_assigned"].astype(int)
    df["vacation_days_last_year"]= df["vacation_days_last_year"].astype(int)
    df["burnout"]                = df["burnout"].astype(int)

    # Clip numeric columns to expected ranges
    df["avg_daily_hours"]       = df["avg_daily_hours"].clip(6.0, 13.0)
    df["overtime_hours_week"]   = df["overtime_hours_week"].clip(0, 25)

    print(f"[Cleaning] Shape after:  {df.shape}")
    print(f"[Cleaning] Burnout distribution:\n{df['burnout'].value_counts()}")
    return df


if __name__ == "__main__":
    print("=" * 50)
    print("  Generating Synthetic Employee Burnout Dataset")
    print("=" * 50)

    # Generate
    df = generate_dataset(N_EMPLOYEES)
    print(f"\n[Generated] {len(df)} employee records")

    # Clean
    df = clean_data(df)

    # Save
    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(out_dir, "employees.csv")
    df.to_csv(out_path, index=False)
    print(f"\n[Saved] Dataset -> {out_path}")
    print("\nFirst 5 rows:")
    print(df.head().to_string())
    print("\nDone! All files saved.")
