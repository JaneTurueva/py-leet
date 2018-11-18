import sys


LEET_MAP = {
    'a': '@',
    's': '5',
    'i': '1',
    'e': '3',
    'o': '0'
}


def leet(text: str) -> str:
    new_leet = ''
    for letter in text:
        lower_letter = letter.lower()
        if lower_letter in LEET_MAP:
            new_leet += LEET_MAP[lower_letter]
        else:
            new_leet += letter
    return new_leet


def main():
    text = ' '.join(sys.argv[1:])
    print(leet(text))
