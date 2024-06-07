# Mapping dictionary for Runes to Code
rune_to_code = {
    'ᚠ': 'ᚰ', 'ᚢ': '𝙖', 'ᚦ': '⁄', 'ᚩ': '∠', 'ᚱ': 'ᶓ', 'ᚳ': '₭', 'ᚷ': 'ᏻ', 
    'ᚹ': 'w', 'ᚻ': '𝗺', 'ᚾ': '⋺', 'ᛁ': 'Ȥ', 'ᛄ': 'ƶ', 'ᛇ': 'ℵ', 'ᛈ': 'Ω', 
    'ᛉ': 'Ᵽ', 'ᛋ': '7', 'ᛏ': '⁄', 'ᛒ': 'ⱱ', 'ᛖ': '⅂', 'ᛗ': '𝜺', 'ᛚ': '⋐', 
    'ᛝ': '⋺', 'ᛟ': 'אֹ', 'ᛞ': '𝙸', 'ᚪ': 'ℵ', 'ᚫ': 'אֵ', 'ᚣ': 'z', 'ᛡ': 'יָ', 
    'ᛠ': 'אֶ'
}

# Mapping dictionary for Code to Runes
code_to_rune = {v: k for k, v in rune_to_code.items()}

# Mapping dictionary for Runes to Letters
rune_to_letter = {
    'ᚠ': 'F', 'ᚢ': 'U', 'ᚦ': 'TH', 'ᚩ': 'O', 'ᚱ': 'R', 'ᚳ': 'C', 'ᚷ': 'G', 
    'ᚹ': 'W', 'ᚻ': 'H', 'ᚾ': 'N', 'ᛁ': 'I', 'ᛄ': 'J', 'ᛇ': 'EO', 'ᛈ': 'P', 
    'ᛉ': 'X', 'ᛋ': 'S', 'ᛏ': 'T', 'ᛒ': 'B', 'ᛖ': 'E', 'ᛗ': 'M', 'ᛚ': 'L', 
    'ᛝ': 'NG', 'ᛟ': 'OE', 'ᛞ': 'D', 'ᚪ': 'A', 'ᚫ': 'AE', 'ᚣ': 'Y', 'ᛡ': 'IA', 
    'ᛠ': 'EA'
}

# Mapping dictionary for Letters to Code
letter_to_code = {
    'F': 'ᚰ', 'U': '𝙖', 'TH': '⁄', 'O': '∠', 'R': 'ᶓ', 'C': '₭', 'G': 'ᏻ', 
    'W': 'w', 'H': '𝗺', 'N': '⋺', 'I': 'Ȥ', 'J': 'ƶ', 'EO': 'ℵ', 'P': 'Ω', 
    'X': 'Ᵽ', 'S': '7', 'Z': '7', 'T': '⁄', 'B': 'ⱱ', 'E': '⅂', 'M': '𝜺', 
    'L': '⋐', 'NG': '⋺', 'ING': '⋺', 'OE': 'אֹ', 'D': '𝙸', 'A': 'ℵ', 'AE': 'אֵ', 
    'Y': 'z', 'IA': 'יָ', 'IO': 'יָ', 'EA': 'אֶ'
}

def translate_rune_to_code(input_text):
    translated_text = ""
    for char in input_text:
        translated_text += rune_to_code.get(char, char)
    return translated_text

def translate_code_to_rune(input_text):
    translated_text = ""
    for char in input_text:
        translated_text += code_to_rune.get(char, char)
    return translated_text

def translate_rune_to_letter(input_text):
    translated_text = ""
    for char in input_text:
        translated_text += rune_to_letter.get(char, char)
    return translated_text

def translate_letter_to_code(input_text):
    translated_text = ""
    for char in input_text:
        translated_text += letter_to_code.get(char.upper(), char)
    return translated_text

def main():
    while True:
        print("\nMenu:")
        print("1. Rune to Code")
        print("2. Code to Rune")
        print("3. Rune to Letter")
        print("4. Letter to Code")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            input_text_rune = input("Enter text to translate from Rune to Code: ")
            print("Translation from Rune to Code:", translate_rune_to_code(input_text_rune))
        elif choice == '2':
            input_text_code = input("Enter text to translate from Code to Rune: ")
            print("Translation from Code to Rune:", translate_code_to_rune(input_text_code))
        elif choice == '3':
            input_text_rune = input("Enter text to translate from Rune to Letter: ")
            print("Translation from Rune to Letter:", translate_rune_to_letter(input_text_rune))
        elif choice == '4':
            input_text_letter = input("Enter text to translate from Letter to Code: ")
            print("Translation from Letter to Code:", translate_letter_to_code(input_text_letter))
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
