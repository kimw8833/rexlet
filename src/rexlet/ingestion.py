import csv
from pathlib import Path

from rexlet.transactions import TransactionInput


EXPECTED_HEADERS = {"Date", "Description", "Amount", "Currency"}


def load_transactions_from_csv(csv_path: Path) -> list[TransactionInput]:
    transactions = []

    with csv_path.open("r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        if reader.fieldnames is None:
            raise ValueError("CSV file is empty or missing a header.")

        if set(reader.fieldnames) != EXPECTED_HEADERS:
            raise ValueError("CSV file has invalid headers.")

        for row in reader:
            transaction = TransactionInput.model_validate(row)
            transactions.append(transaction)

    return transactions