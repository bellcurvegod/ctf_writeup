from collections import Counter
import re
import sys

def count_words(filenames):
    word_count = Counter()
    for filename in filenames: 
        with open(filename, 'r') as file:
            text = file.read()
            words = re.findall(r'\b\w+\b', text)
            word_count.update(words)
    return word_count

def count_letters(filenames):
    letter_count = Counter()
    for filename in filenames: 
        with open(filename, 'r') as file:
            text = file.read()
            letters = re.findall(r'[a-zA-Z]', text)
            letter_count.update(letters)
    return letter_count

if __name__ == "__main__":
    filenames = sys.argv[1:]
    word_count = count_words(filenames)
    letter_count = count_letters(filenames)
    for letter, count in letter_count.most_common():
        print(f"{letter}: {count}")

