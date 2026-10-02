from datetime import date

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from rexlet.models import Transaction, Base


def test_save_and_read_transaction():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)

    TestSession = sessionmaker(bind=engine)
    session = TestSession()

    transaction = Transaction(
        date=date(2026, 10, 2),
        description="MAX STHLM 018392",
        amount=-129.0,
        currency="SEK",
        merchant="MAX Burgers",
        category="Food",
        subcategory="Restaurants",
    )

    session.add(transaction)
    session.commit()

    saved_transaction = session.query(Transaction).first()

    assert saved_transaction.merchant == "MAX Burgers"
    assert saved_transaction.description == "MAX STHLM 018392"
    assert saved_transaction.amount == -129.0
    assert saved_transaction.currency == "SEK"
    assert saved_transaction.category == "Food"
    assert saved_transaction.subcategory == "Restaurants"

    session.close()