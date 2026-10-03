from datetime import date

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from rexlet.models import Transaction, Base
from rexlet.persistence import get_transactions, save_transaction

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

    save_transaction(session, transaction)
    assert transaction.id is not None

    saved_transaction = session.query(Transaction).first()

    assert saved_transaction.merchant == "MAX Burgers"
    assert saved_transaction.description == "MAX STHLM 018392"
    assert saved_transaction.amount == -129.0
    assert saved_transaction.currency == "SEK"
    assert saved_transaction.category == "Food"
    assert saved_transaction.subcategory == "Restaurants"

    session.close()


def test_save_multiple_transactions():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)

    TestSession = sessionmaker(bind=engine)
    session = TestSession()

    first_transaction = Transaction(
        date=date(2026, 10, 2),
        description="MAX STHLM 018392",
        amount=-129.0,
        currency="SEK",
        merchant="MAX Burgers",
        category="Food",
        subcategory="Restaurants",

    )

    second_transaction = Transaction(
        date=date(2026, 10, 3),
        description="SPOTIFY",
        amount=-119.0,
        currency="SEK",
        merchant="Spotify",
        category="Entertainment",
        subcategory="Streaming",
    )

    session.add(first_transaction)
    session.add(second_transaction)
    session.commit()

    saved_transactions = get_transactions(session)

    assert len(saved_transactions) == 2

    session.close()
