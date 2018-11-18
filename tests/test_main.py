from leet import leet


def test_lowercase():
    assert leet('hello world!') == 'h3ll0 w0rld!'


def test_uppercase():
    assert leet('HELLO WORLD!') == 'H3LL0 W0RLD!'