import pandas as pd
import numpy as np

def clean_agent_data(txns, agents):
    """
    Cleans transaction data and returns a cleaned
    dataframe together with a cleaning log.
    """

    log = []

    before = len(txns)

    txns = txns.drop_duplicates(subset="txn_id")

    log.append(
        f"Removed {before - len(txns)} duplicate rows."
    )

    txns["txn_type"] = (
        txns["txn_type"]
        .str.strip()
        .str.title()
    )

    txns["amount"] = pd.to_numeric(
        txns["amount"],
        errors="coerce"
    )

    txns["txn_date"] = pd.to_datetime(
        txns["txn_date"],
        errors="coerce"
    )

    median_amount = txns["amount"].median()

    txns["amount_imputed"] = txns["amount"].isna()

    txns["amount"] = txns["amount"].fillna(
        median_amount
    )

    q1 = txns["amount"].quantile(0.25)
    q3 = txns["amount"].quantile(0.75)

    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    txns["is_outlier"] = (
        (txns["amount"] < lower)
        |
        (txns["amount"] > upper)
    )

    clean_df = txns.merge(
        agents,
        on="agent_id",
        how="left"
    )

    return clean_df, log