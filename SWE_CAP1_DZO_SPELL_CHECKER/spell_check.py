import re

def only_dzongkha_word(word):
    return re.match(r'^[\u0F00-\u0FFF]+$', word)

def load_dzongkha_dictionary(dictionary_file):
    dzongkha_words = set()
    with open(dictionary_file, 'r', encoding="utf-8") as file:
        for line in file:
            words = line.split()
            for word in words:
                if only_dzongkha_word(word):
                    dzongkha_words.add(word)
    return dzongkha_words

def check_incorrect_spellings(script_file, dictionary_file):
    dzongkha_words = load_dzongkha_dictionary(dictionary_file)

    with open(script_file, "r", encoding="utf-8") as file:
        lines = file.readlines()

    incorrect_spellings = []

    for line_num, line in enumerate(lines, start=1):
        words = line.split()

        for word_pos, word in enumerate(words, start=1):
            if only_dzongkha_word(word) and word not in dzongkha_words:
                incorrect_spellings.append((word, line_num, word_pos))

    return incorrect_spellings

script_file = "356.txt"
dictionary_file = "only_dzongkha.txt"

incorrect_spellings = check_incorrect_spellings(script_file, dictionary_file)

if incorrect_spellings:
    print("Incorrect Dzongkha words found:")
    for word, line_num, word_pos in incorrect_spellings:
        print(f"Word: '{word}' | Line: {line_num} | Position: {word_pos}")
else:
    print("No incorrect spellings found.")
