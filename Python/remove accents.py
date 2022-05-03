import unicodedata


def remove_accents(text: str) -> str:
    """ Replace all ácçêntẽd characters from text with their non-accented counterparts by removing
    all "Nonspacing Mark (Mn)" unicode characters. Useful for making foreign names/words searchable """
    normalized_text = unicodedata.normalize('NFD', text)
    return ''.join(char for char in normalized_text if unicodedata.category(char) != 'Mn')


if __name__ == "__main__":
    assert remove_accents("façade") == "facade"
    assert remove_accents("́a ̀b c͜ d̥ ē") == "a b c d e"
