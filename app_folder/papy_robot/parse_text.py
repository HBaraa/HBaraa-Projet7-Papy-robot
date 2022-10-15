import random

from .stop_words import STOP_WORDS, LIST_PERSONALIZED, KEY_WORDS
from .random_quotes import FIRST_RANDOM_QUOTES


def text_parser(phrase):
    words = []
    message = phrase.lower()
    message = message.replace("'", " ")
    for word in message.split():
        words.append(word)
        if (
            word in STOP_WORDS
            or word in LIST_PERSONALIZED
        ):
            words.remove(word)
        elif word in KEY_WORDS:
            words.remove(word)
            word = word
            words.append(word)
        else:
            pass
    return words


GREETING_LIST = ["salut", "bonjour", "bonjours",
                          "coucou", "hey", "ahoy"]


def detect_salutation(message):
    # 0 : No greetings / 1 : Greeting detected
    salutations = 0
    saluer_word = ""

    for salutation in GREETING_LIST:
        if salutation in message:
            saluer_word = salutation
            message = message.replace(salutation, "")
            salutations = 1

    return {
        "msg": message,
        "greeting_word": saluer_word,
        "greeting": salutations
        }


def add_random_quotes(searched_title, sentence):
    first_quotes_list = FIRST_RANDOM_QUOTES
    nbr = len(first_quotes_list)
    n = random.randint(0, nbr-1)
    added_sentence = first_quotes_list[n]
    text_final = added_sentence + " " + searched_title.capitalize()+" 🧐 " + " ;   " + sentence   # noqa
    return text_final
