import re


def remove_url_from_text(text):
    """
    remove all url
    :param text:
    :return:
    """
    text = re.sub(r'(https|http)?:\/\/(\w|\.|\/|\?|\=|\&|\%)*\b', '', text, flags=re.MULTILINE)
    return text


def remove_special_char_from_text(text):
    a = re.findall(r'[^\*"@#:|<>]', text, re.S)
    a = "".join(a)
    print(a)


def get_eng_char_from_text(text):
    """
    only get english words from input text
    :param text: input text, like twitter content
    :return: text with english only
    """

    res = re.findall('[a-zA-Z0-9,.?!;:"\'()]+', text, re.S)
    res = "".join(res)

    return res


if __name__ == '__main__':
    pass
