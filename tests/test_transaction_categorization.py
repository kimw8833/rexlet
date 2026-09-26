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


def test_categorization_is_case_insensitive():
    result = categorize_transaction("max burgers")

    assert result == {
        "category": "Food",
        "subcategory": "Restaurants",
    }


def test_transaction_can_be_categorized_with_custom_rules():
    rules = {
        "Pressbyran": {
            "category": "Food",
            "subcategory": "Convenience Store",
        }
    }

    result = categorize_transaction("Pressbyran", rules)

    assert result == {
        "category": "Food",
        "subcategory": "Convenience Store",
    }


def test_rule_can_have_category_without_subcategory():
    rules = {
        "SJ": {
            "category": "Transport",
        }
    }

    result = categorize_transaction("SJ", rules)

    assert result == {
        "category": "Transport",
    }


def test_unknown_merchant_with_custom_rules_is_uncategorized():
    rules = {
        "SJ": {
            "category": "Transport",
        }
    }

    result = categorize_transaction("Unknown Shop", rules)

    assert result is None
