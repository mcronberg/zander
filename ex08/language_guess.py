def frequency_letter(filepath, letter):

    with open(filepath, 'r') as file:
        text = file.read().lower()  
        
    unwanted_chars = [' ', '.', ',', '?', '!']
    for char in unwanted_chars:
        text = text.replace(char, '')
    
    letter_count = text.count(letter)
    total_letters = len(text)
    
    percentage = (letter_count / total_letters) * 100
    
    return percentage

def language_guess(filepath):
    frequency_a = frequency_letter(filepath, 'a')
    frequency_e = frequency_letter(filepath, 'e')
    
    if 7.2 <= frequency_a <= 9.2 and 11.7 <= frequency_e <= 13.7:
        return "English"
    elif 5.5 <= frequency_a <= 7.5 and 15.3 <= frequency_e <= 17.3:
        return "German"
    elif 6.6 <= frequency_a <= 8.6 and 13.7 <= frequency_e <= 15.7:
        return "French"
    else:
        return "Unknown"

if __name__ == "__main__":
    path = 'files/hamlet.txt'
    print('The text is in', language_guess(path))

if __name__ == "__main__":
    path = 'files/hamlet.txt'
    frequency_a = frequency_letter(path, 'a')
    frequency_e = frequency_letter(path, 'e')
    print('The letter a appears', frequency_a, '% of the time in the text')
    print('The letter e appears', frequency_e, '% of the time in the text')
