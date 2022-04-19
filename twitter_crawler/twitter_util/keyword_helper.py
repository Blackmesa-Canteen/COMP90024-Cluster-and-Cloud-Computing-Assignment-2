from fuzzywuzzy import fuzz
from loguru import logger

from common_util.config_handler import ConfigHandler

config = ConfigHandler()


def is_text_match_keywords(input_text):
    """
    keywords are defined in config file.
    you can also define key-word-match-degree there

    :param input_text: text need to be judged
    :return: if text matches keywords or not

    author: xiaotian Li
    """
    key_word_sentence = config.get_lower_key_word_token_string()

    if len(key_word_sentence) != 0:
        ratio = fuzz.token_set_ratio(key_word_sentence, input_text)
        # logger.debug("match score: " + str(ratio) + " in text: " + input_text)
        if ratio >= config.get_key_word_match_degree():
            # matched twitter into queue
            return True
        else:
            return False
    # no keywords defined at all, all text will match
    return True

if __name__ == '__main__':
    text = "7 away WTF?!"
    print(is_text_match_keywords(text))