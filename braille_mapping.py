#Braille mapping logic goes here

dot_to_key = {
    1: 'D',
    2: 'W',
    3: 'Q',
    4: 'K',
    5: 'O',
    6: 'P'
}

key_to_dot = {
    v: k for k, v in dot_to_key.items()
}

braille_letters = {
    'a': [1],
    'b': [1, 2],
    'c': [1, 4],
    'd': [1, 4, 5],
    'e': [1, 5],
    'f': [1, 2, 4],
    'g': [1, 2, 4, 5],
    'h': [1, 2, 5],
    'i': [2, 4],
    'j': [2, 4, 5],
    'k': [1, 3],
    'l': [1, 2, 3],
    'm': [1, 3, 4],
    'n': [1, 3, 4, 5],
    'o': [1, 3, 5],
    'p': [1, 2, 3, 4],
    'q': [1, 2, 3, 4, 5],
    'r': [1, 2, 3, 5],
    's': [2, 3, 4],
    't': [2, 3, 4, 5],
    'u': [1, 3, 6],
    'v': [1, 2, 3, 6],
    'w': [2, 4, 5, 6],
    'x': [1, 3, 4, 6],
    'y': [1, 3, 4, 5, 6],
    'z': [1, 3, 5, 6],

    # Add more mappings as needed
}

def combo_to_letter(combo):
    try:
        dots = sorted([key_to_dot[dot.upper()] for dot in combo])
    except KeyError:
        return None
    for letter, pattern in braille_letters.items():
        if sorted(pattern) == dots:
            return letter
    return None