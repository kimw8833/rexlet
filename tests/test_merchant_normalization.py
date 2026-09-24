from rexlet.normalization import normalize_merchant

def test_normalize_max_merchant():

    result = normalize_merchant("MAX STHLM 018392")

    assert result == "MAX Burgers"

def test_normalize_max_merchant_ignores_case_and_whitespace():

    result = normalize_merchant("  max sthl 018382  ")

    assert result == "MAX Burgers"

def test_normalize_ica_merchant():

    result = normalize_merchant("ICA KVANTUM UPPSALA 48392")

    assert result == "ICA"

def test_normalize_spotify_merchant():

    result = normalize_merchant("spotify p12345")

    assert result == "Spotify"

def test_normalize_vattenfall_merchant():

    result = normalize_merchant("VATTENFALL AB 839201")

    assert result == "Vattenfall"

def test_unknown_merchant_returns_cleaned_description():

    result = normalize_merchant("  LOCAL COFFEE SHOP 12345  ")

    assert result == "LOCAL COFFEE SHOP 12345"

def test_max_does_not_match_inside_another_word():

    result = normalize_merchant("MAXIMUM FITNESS UPPSALA")

    assert result == "MAXIMUM FITNESS UPPSALA"