import sys


LEET_MAP = str.maketrans('AaSsIiEeOo', '@@55113300')


def leet(text: str):
    result = text.translate(LEET_MAP)
    return result


def main():
    text = ' '.join(sys.argv[1:])
    print(leet(text))
