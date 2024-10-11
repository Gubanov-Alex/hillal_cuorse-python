import string
import re


def is_palindrome(text:string)->bool:
    result = False

    # """Simple formula:"""

    # for letter in text:
    #     if letter in string.punctuation or letter in " ":
    #         text = text.replace(letter, "")
    #
    # if text.lower() == text[::-1].lower():
    #     result = True

    # """Using regular expressions:"""
    new_text = re.sub(r'[^a-zA-Z0-9]', '', text)

    if new_text.lower() == new_text[::-1].lower():
        result = True

    return result

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")