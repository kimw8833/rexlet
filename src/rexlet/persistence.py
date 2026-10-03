from sqlalchemy.orm import Session

from rexlet.models import Transaction

def save_transaction(session: Session, transaction: Transaction) -> Transaction:
    session.add(transaction)
    session.commit()
    session.refresh(transaction)

    return


def get_transactions(session: Session) -> list[Transaction]:
    return session.query(Transaction).all()