def correct_sentence(text):
    text = text[0].upper() + text[1:]
    if not text.endswith('.'):
        text += '.'

    print(text)


correct_sentence("greetings frineds")
