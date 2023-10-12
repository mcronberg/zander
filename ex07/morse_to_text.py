def morse_to_text(morse_code, debug=None):
    morse_code_dict = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G',
        '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N',
        '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U',
        '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z'
    }

    # Split the morse code by double space to get individual words
    words_in_morse = morse_code.split('  ')
    if (debug):
        print(f"words_in_morse: {words_in_morse}")
    # List to hold the converted English words
    english_words = []

    # Iterate over each Morse word
    for word in words_in_morse:
        # Split the Morse word by single space to get individual Morse letters
        letters_in_morse = word.split(' ')
        if (debug):
            print(f"letters_in_morse: {letters_in_morse}")
        # Convert each Morse letter to English
        english_letters = []
        for letter in letters_in_morse:
            english_letter = morse_code_dict[letter]
            if (debug):
                print(f"  english_letter: {english_letter}")
            english_letters.append(english_letter)

        # Join the English letters to form a word and append to the list of words
        english_word = ''.join(english_letters)
        english_words.append(english_word)

    # Join the English words to form the final sentence
    english_sentence = ' '.join(english_words)

    return english_sentence


# Test the function with the provided example
print(morse_to_text("..  .- --  .-  ... --.- ..- .. .-. .-. . .-.."))
