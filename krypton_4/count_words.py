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


def count_letters_vigenere(filenames):
    counters = [Counter() for _ in range(6)]
    
    for filename in filenames:
        with open(filename, 'r') as file:
            text = file.read()
            letters = re.findall(r'[a-zA-Z]', text)  
            
            for index, letter in enumerate(letters):
                letter = letter.upper()   
                group_index = index % 6   
                counters[group_index][letter] += 1
    
    # Print the frequency count for each group
    for i, counter in enumerate(counters, start=1):
        print(f"Group {i}: {counter}")

    
if __name__ == "__main__":
    filenames = sys.argv[1:]
    count_letters_vigenere(filenames)

