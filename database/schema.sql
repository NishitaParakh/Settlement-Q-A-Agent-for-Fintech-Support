CREATE TABLE IF NOT EXISTS transactions (
    transaction_id TEXT PRIMARY KEY,
    date_t TEXT,
    amount REAL,
    currency TEXT,
    gateway_status TEXT,
    bank_status TEXT,
    ledger_status TEXT,
    settlement_status TEXT,
    created_at TEXT
)

CREATE TABLE IF NOT EXISTS investigations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaction_id TEXT,
    diagnosis TEXT,
    reason TEXT,
    confidence TEXT,
    recommended_action TEXT,
)

CREATE TABLE IF NOT EXISTS investigations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    transaction_id TEXT,
    exception_type TEXT,
    description_t TEXT
)