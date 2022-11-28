def countLetters():
    lotr_text = open("lotrTrilogy_text.txt", "r").read()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_count = dict.fromkeys(alphabet, 0)
    for letter in lotr_text:
        letter = letter.lower()
        if letter in alphabet:
            letter_count[letter] = (letter_count[letter] + 1)
    print(letter_count)
countLetters()
