def normalize_merchant(description: str) -> str:

    cleaned_description = description.lower().strip().split()

    if "max" in cleaned_description:
        return "MAX Burgers"
    elif "ica" in cleaned_description:
        return "ICA"
    elif "spotify" in cleaned_description:
        return "Spotify"
    elif "vattenfall" in cleaned_description:
        return "Vattenfall"

    return description.strip()
