from braille_mapping import combo_to_letter
from dictionary_loader import load_dictionary
from autocorrect import suggest_word

# Load the dictionary once
braille_dict = load_dictionary()

print("Braille Auto-Correct System Initialized")
print("Type comma-separated key combos (e.g., DK,D,WQKO) or type 'exit' to quit.")

while True:
    user_input = input("\nEnter Braille Key Combinations: ").strip()
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    # Convert user input into sorted key combos (e.g., 'DK' → ['D','K'])
    key_combos = [sorted(list(combo.upper())) for combo in user_input.split(',') if combo]

    # Get suggestions
    suggestions = suggest_word(key_combos, braille_dict)

    # Show results
    print("Top Suggestions:", suggestions if suggestions else "No close matches found.")
