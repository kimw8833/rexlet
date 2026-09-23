import pytest
from pydantic import ValidationError
from datetime import date
from decimal import Decimal
from pathlib import Path

from rexlet.ingestion import load_transactions_from_csv
from rexlet.transactions import TransactionInput


def test_load_transaction_from_valid_csv():
    csv_path = Path("data/sample/transactions.csv")

    transactions = load_transactions_from_csv(csv_path)

    assert len(transactions) == 8
    assert all(
        isinstance(transaction, TransactionInput)
        for transaction in transactions
    )

    first_transaction = transactions[0]

    assert first_transaction.transaction_date == date(2026, 9, 1)
    assert first_transaction.raw_description == "MAX STHLM 018392"
    assert first_transaction.amount == Decimal("-149.00")
    assert first_transaction.currency == "SEK"

def test_invalid_transaction_in_csv_fails_validation(tmp_path):

    csv_path = tmp_path / "invalid_transactions.csv"

    csv_path.write_text(

        "Date,Description,Amount,Currency\n"
        "2026-09-20,,129.00,SEK\n",
        encoding="utf-8"
    )

    with pytest.raises(ValidationError):
        load_transactions_from_csv(csv_path)

def test_csv_missing_required_column_raises_error(tmp_path):

    csv_path = tmp_path / "missing_column.csv"

    csv_path.write_text(
        "Date,Description,Currency\n"
        "2026-09-20,MAX STHLM 018392,SEK\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        load_transactions_from_csv(csv_path)

def test_csv_with_header_only_returns_empty_list(tmp_path):

    csv_path = tmp_path / "empty_transactions.csv"

    csv_path.write_text(
        "Date,Description,Amount,Currency\n",
        encoding="utf-8",
    )

    transactions = load_transactions_from_csv(csv_path)

    assert transactions == []

def test_completely_empty_csv_raises_error(tmp_path):
    csv_path = tmp_path / "empty.csv"

    csv_path.write_text(
        "",
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        load_transactions_from_csv(csv_path)

def test_csv_with_invalid_headers_raises_error(tmp_path):

    csv_path = tmp_path / "invalid_headers.csv"

    csv_path.write_text(
        "Foo,Bar,Baz\n",
        encoding="utf-8"
    )

    with pytest.raises(ValueError):
        load_transactions_from_csv(csv_path)

def test_csv_with_extra_comlumn_raises_error(tmp_path):

    csv_path = tmp_path / "extra_column.csv"

    csv_path.write_text(
        "Date,Description,Amount,Currency,Account\n"
        "2026-09-20,MAX STHLM 018392,-129.00,SEK,Checking\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError):
        load_transactions_from_csv(csv_path)
