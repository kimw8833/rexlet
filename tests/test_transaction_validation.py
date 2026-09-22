import csv
from datetime import date
from decimal import Decimal
from pathlib import Path

import pytest
from pydantic import ValidationError

from rexlet.transactions import TransactionInput


# Valid transaction
def test_valid_transaction_is_parsed():
    transaction = TransactionInput.model_validate(
        {
            "Date": "2026-09-01",
            "Description": "MAX STHLM 018392",
            "Amount": "-149.00",
            "Currency": "SEK",
        }
    )

    assert transaction.transaction_date == date(2026, 9, 1)
    assert transaction.raw_description == "MAX STHLM 018392"
    assert transaction.amount == Decimal("-149.00")
    assert transaction.currency == "SEK"

# Missing Date
def test_missing_date_fails_validation():
    with pytest.raises(ValidationError):
        TransactionInput.model_validate(
            {
                "Description": "MAX STHLM 018392",
                "Amount": "-149.00",
                "Currency": "SEK",
            }
        )

# Invalid date
def test_invalid_calendar_date_fails_validation():
    with pytest.raises(ValidationError):
        TransactionInput.model_validate(
            {
                "Date": "2026-13-40",
                "Description": "MAX STHLM 018392",
                "Amount": "-149.00",
                "Currency": "SEK",
            }
        )

# Invalid amount
def test_invalid_amount_fails_validation():
    with pytest.raises(ValidationError):
        TransactionInput.model_validate(
            {
                "Date": "2026-09-02",
                "Description": "ICA KVANTUM UPPSALA",
                "Amount": "not-a-number",
                "Currency": "SEK",
            }
        )

# Missing Description
def test_missing_description_fails_validation():
    with pytest.raises(ValidationError):
        TransactionInput.model_validate(
            {
                "Date": "2026-09-03",
                "Amount": "-119.00",
                "Currency": "SEK",
            }
        )

# Empty Description
def test_empty_description_fails_validation():
    with pytest.raises(ValidationError):
        TransactionInput.model_validate(
            {
                "Date": "2026-09-03",
                "Description": "",
                "Amount": "-119.00",
                "Currency": "SEK",
            }
        )

# Missing Currency
def test_missing_currency_fails_validation():
    with pytest.raises(ValidationError):
        TransactionInput.model_validate(
            {
                "Date": "2026-09-04",
                "Description": "VATTENFALL AB",
                "Amount": "-840.00",
            }
        )

# Empty Currency
def test_empty_currency_fails_validation():
    with pytest.raises(ValidationError):
        TransactionInput.model_validate(
            {
                "Date": "2026-09-04",
                "Description": "VATTENFALL AB",
                "Amount": "-840.00",
                "Currency": "",
            }
        )

# Currency normalization
def test_currency_is_normalized_to_uppercase():
    transaction = TransactionInput.model_validate(
        {
            "Date": "2026-09-05",
            "Description": "SL ACCESS",
            "Amount": "-970.00",
            "Currency": "sek",
        }
    )

    assert transaction.currency == "SEK"

# Unknown merchant description
def test_transaction_without_known_merchant_is_valid():
    transaction = TransactionInput.model_validate(
        {
            "Date": "2026-09-07",
            "Description": "UNKNOWN SHOP 48291",
            "Amount": "-87.50",
            "Currency": "SEK",
        }
    )

    assert transaction.raw_description == "UNKNOWN SHOP 48291"



# Valid sample CSV - CSV Positive test data - accepted
def test_valid_sample_csv_records_pass_validation():
    csv_path = Path("data/sample/transactions.csv")

    with csv_path.open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        transactions = [
            TransactionInput.model_validate(row)
            for row in reader
        ]

    assert len(transactions) == 8

# Invalid sample CSV - CSV Negative test data - rejected
def test_invalid_sample_csv_records_fail_validation():
    csv_path = Path("data/sample/transactions_invalid.csv")

    invalid_count = 0

    with csv_path.open(newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            try:
                TransactionInput.model_validate(row)
            except ValidationError:
                invalid_count += 1

    assert invalid_count == 4
    