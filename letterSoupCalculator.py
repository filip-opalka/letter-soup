def countLetters():
    lotr_text = open("lotrTrilogy_text.txt", "r").read()
    letter_count = {"a": 0,
                    "b": 0,
                    "c": 0,
                    "d": 0,
                    "e": 0,
                    "f": 0,
                    "g": 0,
                    "h": 0,
                    "i": 0,
                    "j": 0,
                    "l": 0,
                    "k": 0,
                    "m": 0,
                    "n": 0,
                    "o": 0,
                    "p": 0,
                    "q": 0,
                    "r": 0,
                    "s": 0,
                    "t": 0,
                    "u": 0,
                    "v": 0,
                    "w": 0,
                    "x": 0,
                    "y": 0,
                    "z": 0}
    for letter in lotr_text:
        letter = letter.lower()
        if letter in "abcdefghijklmnopqrstuvwxyz":
            letter_count[letter] = (letter_count[letter] + 1)
    print(letter_count)
countLetters()
