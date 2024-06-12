from typing import Iterable

# from english_words import get_english_words_set

# web2lowerset = get_english_words_set(['gcide'], lower=True)
# read from google-10000-english-no-swears.txt
web2lowerset = set()
with open("google-10000-english-no-swears.txt", "r") as f:
    for line in f:
        word = line.strip().lower()
        web2lowerset.add(word)

while True:
    filter_ = input("Filter: ").strip().lower()

    if filter_ == "!exit":
        break

    containing: Iterable[str] = []
    if "&" in filter_:
        filter_, *containing = filter_.split("&")

    filter_new = ""
    for c in filter_:
        if c.isnumeric():
            filter_new += "_" * int(c)
        else:
            filter_new += c

    filter_ = filter_new

    # filter example: h__lo

    length = len(filter_)

    def filter_word(word):
        if len(word) != length:
            return False
        for a, x in zip(word, filter_):
            if x == '_':
                continue
            if a != x:
                return False
        for x in containing:
            for c in x:
                if c not in word:
                    return False
        return True

    filtered_words = [word for word in web2lowerset if filter_word(word)]

    for wd in filtered_words:
        print(wd)
