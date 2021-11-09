from typing import List


from stop_words import STOP_WORDS, LIST_PERSONALIZED, KEY_WORDS

def transform_to_upper(text):
    return {
        "text_original": text,
        "text_transformed" : text.upper()
    }




def text_parser(phrase):
    words = []
    message = phrase.lower()
    message = message.replace("'", " ")
    for word in message.split(" "):
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
