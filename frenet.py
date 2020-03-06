from string import ascii_letters
from operator import itemgetter
from nltk.corpus import words


def letters(text):
    letter_dict = {}
    total = 0
    p = "%"
    for letter in text:
        if letter in ascii_letters:
            try:
                letter_dict[letter] += 1
            except KeyError:
                letter_dict[letter] = 1

    print("=" * 5, 'Letters', "=" * 5)
    for x in letter_dict.values():
        total += x
    for letter in sorted(letter_dict.items(), key=itemgetter(1), reverse=True):
        x = ((letter[1] / total) * 100)
        print("the %s %.2f%s " % (letter, x, p))


def bigrams(text):
    bigram_dict = {}
    bigram_holder = []
    total = 0
    p = "%"
    for letter in text:
        if letter not in ascii_letters:
            bigram_holder = []
            continue
        else:
            bigram_holder.append(letter)

        if len(bigram_holder) == 2:
            bigram = bigram_holder[0] + bigram_holder[1]
            try:
                bigram_dict[bigram] += 1
            except KeyError:
                bigram_dict[bigram] = 1

            last = bigram_holder.pop()
            bigram_holder = []
            bigram_holder.append(last)

    print("=" * 5, 'Bigrams', "=" * 5)
    for x in bigram_dict.values():
        total += x
    for bigram in sorted(bigram_dict.items(), key=itemgetter(1), reverse=True):
        x = ((bigram[1] / total) * 100)
        print("the %s %.2f%s " % (bigram, x, p))


def trigrams(text):
    trigram_dict = {}
    trigram_holder = []
    total = 0
    p = "%"
    for letter in text:
        if letter not in ascii_letters:
            trigram_holder = []
            continue
        else:
            trigram_holder.append(letter)

        if len(trigram_holder) == 3:
            trigram = trigram_holder[0] + trigram_holder[1] + trigram_holder[2]
            try:
                trigram_dict[trigram] += 1
            except KeyError:
                trigram_dict[trigram] = 1

            l1 = trigram_holder.pop()
            l2 = trigram_holder.pop()
            trigram_holder = []
            trigram_holder.append(l2)
            trigram_holder.append(l1)

    print("=" * 5, 'Trigrams', "=" * 5)
    for x in trigram_dict.values():
        total += x
    for trigram in sorted(trigram_dict.items(), key=itemgetter(1), reverse=True):
        x = ((trigram[1] / total) * 100)
        print("the %s %.2f%s " % (trigram, x, p))


def is_english_word(word):
    setofwords = set(words.words())
    if word in setofwords:
        print("yes")


is_english_word("the")
