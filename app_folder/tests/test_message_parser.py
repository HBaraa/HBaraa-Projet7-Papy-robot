import json
import pytest
from app_folder.static.scripts.py_codes.stop_words import STOP_WORDS
from app_folder.static.scripts.py_codes.utils import text_parser, detect_salutation, remove_special_char, filtred_text


def test_if_parser_detect_greetings():
    mock_message = 'bonjour'
    tester = detect_salutation(mock_message)
    assert tester["msg"] == ""
    assert tester["greeting"] == 1

def test_if_special_char_are_removed():
    mock_message = 'je ()cherche l\'adresse d\'openclassrooms{[:!]}'
    msg = remove_special_char(mock_message)
    assert msg == "je cherche l adresse d openclassrooms"

def test_clean_message():
    mock_message = "je cherche l adresse d openclassrooms"
    words_list = text_parser(mock_message)
    mock_another_message = "je cherche l adresse de la tour effel"
    second_words_list = text_parser(mock_another_message)
    mock_text = filtred_text(second_words_list)
    print(mock_text)
    assert words_list == ["openclassrooms"]
    assert second_words_list == ["tour", "effel"]
    assert mock_text == "tour effel"
