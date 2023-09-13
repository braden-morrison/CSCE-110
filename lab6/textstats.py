# File: textstats.py
# Author: Student name
# Date: xx/xx/2022
# Section: Student section number
# E-mail: student_email@tamu.edu
# Description:
# e.g., This program asks for ...


def main():
    """Gets a block of text from the user and prints some statistics about the text."""
    text = input("Enter text: ").lower()
    print(f"Number of sentences: {get_sentences(text)}")
    print(f"Number of words: {get_words(text)}")
    print(f"Number of punctuations: {get_punctuations(text)}")
    print_letters(text)
    print_palindromes(text)


def get_sentences(text):
    sentences = text.split('.') + text.split('!') + text.split('?')
    sentences = [sentence.strip()
                 for sentence in sentences if sentence.strip()]
    return len(sentences)


def get_words(text):
    """Returns the number of words in the text."""
    words = text.split()
    return len(words)


def get_punctuations(text):
    """Returns the number of punctuations in the text."""
    punctuations = '.,;:!?'
    num = sum(text.count(p) for p in punctuations)
    return num


def print_letters(text):
    letter_counts = {}
    for char in text:
        if char.isalpha():
            char2 = char.lower()
            letter_counts[char2] = letter_counts.get(char2, 0) + 1

    sorted_letters = sorted(letter_counts.items(), key=lambda x: (-x[1], x[0]))

    prev_count = None
    for letter, count in sorted_letters:
        if prev_count is not None and count != prev_count:
            print()  # Print a blank line to separate groups of letters with the same count
        prev_count = count
        print(f"{letter}: {count}")
    pass


def print_palindromes(text):
    """Prints the number of occurrences of case-insensitive palindrome numbers and palindrome words and letters in
    the text. """
    pass


main()
