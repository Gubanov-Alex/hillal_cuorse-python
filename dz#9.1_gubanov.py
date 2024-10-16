import re

def popular_words (text:str, words:list)->dict:
    """
    Checking counts of words in text.

    :param text: text for checking.
    :type text: str.
    :param words: word for counting.
    :type words: list.
    :return: numbers  counts of words in dictionary.
    :rtype:  dict.
    """
    #1 - Simple:

    text_mod = text.lower().split()
    result ={}                                # Creating dictionary
    for word in words:
        result[word] = text_mod.count(word.lower())    # Counting words

    return result


    #2 - 2 Also not so difficult))):

    # text_mod = text.lower()
    # words_mod = [word.lower() for word in words]
    # word_counts = {word: 0 for word in words_mod}      # Creating dictionary
    # for word in words_mod:
    #     matches = re.findall(fr'\b{word}\b', text_mod)   # Counting words
    #     word_counts[word] = len(matches)       # Refreshing number of counts
    #
    # return word_counts


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')