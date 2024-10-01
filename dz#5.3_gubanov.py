import string
from dataclasses import replace
from string import punctuation

hashtag_user = input("Enter hashtag: ").title()
for letter in hashtag_user:
    if letter in string.punctuation or letter in " " :
        hashtag_user = hashtag_user.replace(letter, "")
hashtag_user = hashtag_user[:139]

print(f"#{hashtag_user}")


