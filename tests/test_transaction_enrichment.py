from rexlet.enrichment import enrich_transaction


def test_enrich_transaction_adds_merchant_and_category():

    transaction = {
        "date": "2026-09-20",
        "description": "MAX STHLM 018392",
        "amount": -129.00,
        "currency": "SEK",
    }

    result = enrich_transaction(transaction)

    assert result["merchant"] == "MAX Burgers"
    assert result["category"] == "Food"
    assert result["subcategory"] == "Restaurants"
    assert result["date"] == "2026-09-20"
    assert result["description"] == "MAX STHLM 018392"
    assert result["amount"] == -129.00
    assert result["currency"] == "SEK"
