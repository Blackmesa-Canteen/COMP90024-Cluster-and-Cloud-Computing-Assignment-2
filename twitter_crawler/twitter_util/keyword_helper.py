from fuzzywuzzy import fuzz
from loguru import logger

from common_util.config_handler import ConfigHandler

config = ConfigHandler()


def is_text_contains_a_keyword(keyword, input_text):
    lower_keyword = keyword.lower()
    lower_input_text = input_text.lower()

    return lower_keyword in lower_input_text


def is_text_match_keywords(input_text):
    """
    keywords are defined in config file.
    you can also define key-word-match-degree there

    :param input_text: text need to be judged
    :return: if text matches keywords or not

    author: xiaotian Li
    """
    key_word_sentence = config.get_lower_key_word_token_string()

    lower_input_text = input_text.lower()

    if len(key_word_sentence) != 0:

        match_degree = config.get_key_word_match_degree()
        if match_degree != 100:
            # fyzz matching
            ratio = fuzz.token_set_ratio(key_word_sentence, lower_input_text)
            # logger.debug("match score: " + str(ratio) + " in text: " + input_text)
            if ratio >= match_degree:
                # matched twitter into queue
                return True
            else:
                return False

        else:
            # Precise matching
            lower_key_word_list = config.get_lower_key_word_list()
            for keyword in lower_key_word_list:
                if keyword not in lower_input_text:
                    return False

    # no keywords defined at all, all text will match
    return True


if __name__ == '__main__':
    # test
    text = "Hey pal, you just blow in from stupid-town?"
    config.reset_config_file_name("app_history_tweet_config.yaml")
    print(is_text_match_keywords(text))

    print(is_text_contains_a_keyword(keyword='Melbou', input_text='Do you like melbourne, my friend'))
