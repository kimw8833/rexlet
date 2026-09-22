from datetime import date
from decimal import Decimal

from pydantic import BaseModel, Field, field_validator


class TransactionInput(BaseModel):
    transaction_date:   date = Field(alias="Date")
    raw_description:    str = Field(alias="Description", min_length=1)
    amount:             Decimal = Field(alias="Amount")
    currency:           str = Field(alias="Currency", min_length=1)

    @field_validator("currency")
    @classmethod
    def normalize_currency(cls, value: str) -> str:
        return value.upper()
    