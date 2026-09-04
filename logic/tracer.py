import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"


def load_data():
    gateway = pd.read_csv(DATA_DIR / "gateway.csv")
    bank = pd.read_csv(DATA_DIR / "bank.csv")
    ledger = pd.read_csv(DATA_DIR / "ledger.csv")
    settlements = pd.read_csv(DATA_DIR / "settlements.csv")

    return gateway, bank, ledger, settlements


def clean_records(df):
    # Convert NaN values to None so they can be returned as JSON
    df = df.astype(object).where(pd.notna(df), None)
    return df.to_dict("records")


def find_transaction(transaction_id):
    gateway, bank, ledger, settlements = load_data()

    gateway_record = gateway[
        gateway["transaction_id"] == transaction_id
    ]

    bank_record = bank[
        bank["transaction_id"] == transaction_id
    ]

    ledger_record = ledger[
        ledger["transaction_id"] == transaction_id
    ]

    settlement_record = settlements[
        settlements["transaction_id"] == transaction_id
    ]

    return {
        "transaction_id": transaction_id,
        "gateway": clean_records(gateway_record),
        "bank": clean_records(bank_record),
        "ledger": clean_records(ledger_record),
        "settlement": clean_records(settlement_record)
    }
