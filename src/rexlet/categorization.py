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


def categorize_transaction(merchant):
    return MERCHANT_CATEGORIES.get(merchant)
