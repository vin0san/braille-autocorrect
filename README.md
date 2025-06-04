# 🔠 Braille Auto-Correct System

A real-time auto-correct and word suggestion system for visually impaired users typing Braille using a QWERTY keyboard.

---

## 📌 Problem Statement

Typing Braille using a QWERTY keyboard can often result in input errors such as:
- Missing keys
- Extra or mistyped keys
- Incorrect dot combinations

This system corrects such inputs and suggests the most likely intended words from a given dictionary.

---

## 🧠 How It Works

### 🔹 QWERTY Braille Mapping

Each Braille dot (1–6) is mapped to a QWERTY key:

| Dot | QWERTY Key |
|-----|------------|
| 1   | D          |
| 2   | W          |
| 3   | Q          |
| 4   | K          |
| 5   | O          |
| 6   | P          |

Example:
- `'D'` = dot 1 → letter 'a'
- `'DW'` = dots 1 & 2 → letter 'b'
- `'DK'` = dots 1 & 4 → letter 'c'

### 🔹 Braille Word Formation
Each word is converted into a sequence of sorted key combinations.
Example: "cat" → [['D','K'], ['D'], ['W','Q','K','O']]

### 🔹 Auto-Correction Logic
We use **Levenshtein Distance** to compare the user’s Braille key input with dictionary word patterns and suggest the closest matches.

---

## 🧪 Example

**Input:**
DK,D,WQKO
**Output:**
Top Suggestions: ['cat', 'cap', 'car']

---

## 📁 Project Structure

```
braille-autocorrect/
├── main.py # Main script to run the system
├── braille_mapping.py # Key-to-dot and dot-to-letter mapping
├── dictionary_loader.py # Loads and converts the dictionary to Braille combos
├── autocorrect.py # Levenshtein-based suggestion engine
├── resources/
│ └── words.txt # English word dictionary
├── README.md # This file
```

---

## 🏃 How to Run

1. Clone the repo:
```bash
git clone https://github.com/vin0san/braille-autocorrect.git
cd braille-autocorrect
```
2. Run the program:
     python main.py
3. Type Braille key combos separated by commas (e.g., DK,D,WQKO)
   Type exit to quit.

## Dependencies
No external dependencies required. Works with Python 3.x.

## Future Improvements

- Support for Braille contractions

- Adaptive learning based on user history

- Multi-language support

- GUI for easier typing practice
