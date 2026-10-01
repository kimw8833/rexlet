from datetime import date
from decimal import Decimal

from rexlet.models import Transaction


def test_create_transaction_model():
    transaction = Transaction(
        date=date(2026, 9, 30),
        description="MAX STHLM 018392",
        amount=Decimal("-129.00"),
        currency="SEK",
        merchant="MAX Burgers",
        category="Food",
        subcategory="Restaurants",
    )

    assert transaction.description == "MAX STHLM 018392"
    assert transaction.amount == Decimal("-129.00")
    assert transaction.merchant == "MAX Burgers"
    assert transaction.category == "Food"
    assert transaction.subcategory == "Restaurants"


def test_transaction_table_columns():
    columns = Transaction.__table__.columns

    assert "id" in columns
    assert "date" in columns
    assert "description" in columns
    assert "amount" in columns
    assert "currency" in columns
    assert "merchant" in columns
    assert "category" in columns
    assert "subcategory" in columns


def test_enrichment_fields_are_nullable():
    columns = Transaction.__table__.columns

    assert columns["merchant"].nullable is True
    assert columns["category"].nullable is True
    assert columns["subcategory"].nullable is True


def test_required_transaction_fields_are_not_nullable():
    columns = Transaction.__table__.columns

    assert columns["date"].nullable is False
    assert columns["description"].nullable is False
    assert columns["amount"].nullable is False
    assert columns["currency"].nullable is False