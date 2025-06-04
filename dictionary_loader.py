from braille_mapping import dot_to_key, key_to_dot, braille_letters

def word_to_braille_keys(word):
    keys_seq = []
    for letter in word.lower():
        if letter not in braille_letters:
            continue
        dots= braille_letters[letter]
        keys = [dot_to_key[dot] for dot in dots]
        keys_seq.append(sorted(keys)) # normalize combo order
    return keys_seq

def load_dictionary(file_path="resources/dictionary.txt"):
    braille_dict = {}
    with open(file_path, "r") as file:
        for line in file:
            word = line.strip()
            if not word.isalpha():
                continue
            braille_dict[word.lower()] = word_to_braille_keys(word)
    return braille_dict