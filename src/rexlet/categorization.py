MERCHANT_CATEGORIES = {
    "MAX Burgers": {
        "category": "Food",
        "subcategory": "Restaurants",
    },
    "ICA": {
        "category": "Food",
        "subcategory": "Groceries",
    },
    "Spotify": {
        "category": "Entertainment",
        "subcategory": "Streaming",
    },
    "Vattenfall": {
        "category": "Housing",
        "subcategory": "Electricity",
    },
}


def categorize_transaction(merchant, rules=None):
    if rules is None:
        rules = MERCHANT_CATEGORIES

    normalized_merchant = merchant.strip().lower()

    for rule_merchant, category_data in rules.items():
        if normalized_merchant == rule_merchant.strip().lower():
            return category_data

    return None
