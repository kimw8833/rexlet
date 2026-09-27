from rexlet.normalization import normalize_merchant
from rexlet.categorization import categorize_transaction

def enrich_transaction(transaction):


    raw_description = transaction["description"]
    description = normalize_merchant(raw_description)
    category_data = categorize_transaction(description, rules=None)


    return {
            "date": transaction["date"],
            "description": raw_description,
            "amount": transaction["amount"],
            "currency": transaction["currency"],
            "merchant": description,
            "category": category_data["category"],
            "subcategory": category_data["subcategory"]
        }
