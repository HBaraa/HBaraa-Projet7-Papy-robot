from app_folder.papy_robot.parse_text import text_parser, detect_salutation, remove_special_char   # noqa


def test_detect_greetings():
    mock_message = 'bonjour'
    tester = detect_salutation(mock_message)
    assert tester["msg"] == ""
    assert tester["greeting"] == 1


def remove_special_char(msg):
    for i in msg:
        if i in "['\"/\\:?!-}><(){,]":
            if i in ",-'\"":
                msg = msg.replace(i, " ")
            else:
                msg = msg.replace(i, "")


def test_clean_message():
    mock_message = "Ou se trouve le jet d'eau de Genève "
    words_list = text_parser(mock_message)
    assert words_list == ["jet", "eau", "de", "genève"]
