from rexlet.categorization import categorize_transaction


def test_max_burgers_is_categorized_as_restaurant():
    result = categorize_transaction("MAX Burgers")

    assert result == {
        "category": "Food",
        "subcategory": "Restaurants",
    }

def test_ica_is_categorized_as_groceries():
    result = categorize_transaction("ICA")

    assert result == {
        "category": "Food",
        "subcategory": "Groceries",
    }

def test_spotify_is_categorized_as_streaming():
    result = categorize_transaction("Spotify")

    assert result == {
        "category": "Entertainment",
        "subcategory": "Streaming",
    }

def test_vattenfall_is_categorized_as_electricity():
    result = categorize_transaction("Vattenfall")

    assert result == {
        "category": "Housing",
        "subcategory": "Electricity",
    }

def test_unknown_merchant_is_uncategorized():
    result = categorize_transaction("Unknown Shop")

    assert result is None
