import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"


def load_data():
    gateway = pd.read_csv(DATA_DIR / "gateway.csv")
    bank = pd.read_csv(DATA_DIR / "bank.csv")
    ledger = pd.read_csv(DATA_DIR / "ledger.csv")
    settlements = pd.read_csv(DATA_DIR / "settlements.csv")

    return gateway, bank, ledger, settlements


def find_transaction(transaction_id):
    gateway, bank, ledger, settlements = load_data()

    gateway_record = gateway[gateway["transaction_id"] == transaction_id]
    bank_record = bank[bank["transaction_id"] == transaction_id]
    ledger_record = ledger[ledger["transaction_id"] == transaction_id]
    settlement_record = settlements[
        settlements["transaction_id"] == transaction_id
    ]

    return {
        "transaction_id": transaction_id,
        "gateway": gateway_record.to_dict("records"),
        "bank": bank_record.to_dict("records"),
        "ledger": ledger_record.to_dict("records"),
        "settlement": settlement_record.to_dict("records")
    }


if __name__ == "__main__":
    result = find_transaction("TXN1001")
    print(result)