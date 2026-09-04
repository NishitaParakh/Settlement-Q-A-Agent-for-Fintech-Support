from flask import Blueprint, request, jsonify

search_bp = Blueprint("search", __name__)


# Mock transaction database
TRANSACTIONS = [
    {
        "transaction_id": "TXN1025",
        "date": "2026-09-04",
        "status": "DELAYED",
        "amount": 1500,
        "gateway": "SUCCESS",
        "bank": "SUCCESS",
        "ledger": "PENDING"
    },
    {
        "transaction_id": "TXN1026",
        "date": "2026-09-04",
        "status": "COMPLETED",
        "amount": 2500,
        "gateway": "SUCCESS",
        "bank": "SUCCESS",
        "ledger": "SUCCESS"
    },
    {
        "transaction_id": "TXN1027",
        "date": "2026-09-03",
        "status": "FAILED",
        "amount": 800,
        "gateway": "FAILED",
        "bank": "PENDING",
        "ledger": "PENDING"
    }
]


@search_bp.route("/search", methods=["GET"])
def search_transactions():

    transaction_id = request.args.get("transaction_id")
    date = request.args.get("date")
    month = request.args.get("month")
    status = request.args.get("status")

    results = TRANSACTIONS

    # Search by transaction ID
    if transaction_id:
        results = [
            transaction for transaction in results
            if transaction["transaction_id"].lower()
            == transaction_id.lower()
        ]

    # Search by date
    if date:
        results = [
            transaction for transaction in results
            if transaction["date"] == date
        ]

    # Search by month
    if month:
        results = [
            transaction for transaction in results
            if transaction["date"].startswith(month)
        ]

    # Search by status
    if status:
        results = [
            transaction for transaction in results
            if transaction["status"].lower()
            == status.lower()
        ]

    return jsonify({
        "count": len(results),
        "transactions": results
    })