morse = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    " ": "/"
}
def encode(text):
    zdanie = ""
    for char in text:
        char = char.upper()
        if char in morse:
            zdanie += morse[char] + " "
        else:
            zdanie += "None"
    return zdanie
print(encode("Ala ma kota"))

#Odwrócenie słownika
morse_inv = {code: char for char, code in morse.items()}
def decode(text_morse):
    zdanie = ""
    text_morse = text_morse.strip().split(" ")
    for slowo in text_morse:
        zdanie += morse_inv[slowo]
    return zdanie
print(decode(encode("Ala ma kota")))


                