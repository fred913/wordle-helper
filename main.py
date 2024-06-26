from typing import Iterable

from english_words import get_english_words_set

bigwl = get_english_words_set(['gcide'], lower=True)
# read from google-10000-english-no-swears.txt
tinywl = list()
with open("google-10000-english-no-swears.txt", "r") as f:
    for line in f:
        word = line.strip().lower()
        tinywl.append(word)

while True:
    filter_ = input("Filter: ").strip().lower()

    if filter_ == "!exit":
        break

    containing: Iterable[str] = []

    allow_big_wl = False
    if "*" in filter_:
        allow_big_wl = True
        filter_ = filter_.replace("*", "")

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

    filtered_words = [word for word in tinywl if filter_word(word)]

    for wd in filtered_words:
        print(wd)

    if allow_big_wl:
        print("Retrying with big word list...")
        filtered_words = [word for word in bigwl if filter_word(word)]
        for wd in filtered_words:
            print(wd)
