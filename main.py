"""
This module processes a book text file to calculate word count and character frequency.
"""
import sys
from stats import character_count, num_words  # type: ignorepa


def get_book_text(book_path: str):
    """
    Reads the text of a book from a file, calculates word count and character frequency,
    and prints the results.
    """
    with open(book_path) as f:
        file_contents = f.read()
        word_count = num_words(file_contents)

        # Corrected variable name
        print(f"--- Begin report of the {book_path} ---")
        print(f"'Found {word_count} total words'")
        for character, count in sorted(character_count(file_contents).items(), key=lambda item: item[1], reverse=True):
            if count > 100:
                print(f"'{character}: {count}'")
            else:
                print(f"'{character}: {count}'")
        print(f"--- End Report ---")


if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
else:
    input_path = sys.argv[1]
    get_book_text(input_path)
