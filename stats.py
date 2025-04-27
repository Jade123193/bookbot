# Removed unused import of get_book_text

def num_words(book_string: str) -> int:
    """
    Calculate the number of words in a given string.

    Args:
        book_string (str): The input string representing the book content.

    Returns:
        int: The total number of words in the string.
    """
    book_words = book_string.split()
    # Removed print statement to avoid side effects
    return len(book_words)


def sort_on(dict):
    """
    Extract the value associated with the key "num" from a dictionary.

    Args:
        d (dict): A dictionary containing a "num" key.

    Returns:
        Any: The value associated with the "num" key in the dictionary.
    """
    return dict["num"]


def charcter_dict_to_sorted_list(character_dict: dict) -> list:
    sorted_list = []
    for ch in character_dict:
        sorted_list.append({"character": ch, "num": character_dict[ch]})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list


def character_count(book_string: str) -> dict:
    """
Calculate the frequency of each alphabetic character in the given string.

Args:
    book_string (str): The input string representing the book content.

Returns:
    dict: A dictionary where keys are characters and values are their frequencies.
"""
    character_dict = {}

    # Iterate through each character in the string to count alphabetic characters
    for character in book_string:
        if character.isalpha():
            lower_case_character = character.lower()
            character_dict[lower_case_character] = character_dict.get(
                lower_case_character, 0) + 1
    return character_dict


def alphabetic_characters(book_string: str) -> dict:
    """
    Count the frequency of alphabetic characters in a given string.

    Args:
        book_string (str): The input string representing the book content.

    Returns:
        dict: A dictionary where keys are alphabetic characters and values are their frequencies.
    """
    from collections import defaultdict

    alpha_character_dict = defaultdict(int)
    for character in book_string:
        if character.isalpha():
            lower_case_character = character.lower()
            alpha_character_dict[lower_case_character] = alpha_character_dict.get(
                lower_case_character, 0) + 1
    return alpha_character_dict
