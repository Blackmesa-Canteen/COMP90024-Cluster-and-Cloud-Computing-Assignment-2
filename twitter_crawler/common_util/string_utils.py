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
    print(remove_retweet_from_twitter_text('RT @zamancomtr: Meslekten ihraç edilen polis müdürü Murat Çetiner: Bana takdir belgesi veren     BM de mi paralel? http://t.co/sd5N6yaZzv'))
