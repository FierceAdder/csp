# Count.py

text = open("Mytext.txt", "r").read()

vowels = "aeiouAEIOU"
consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

vowel_count = 0
consonant_count = 0
upper_case_count = 0
lower_case_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1
    elif char in consonants:
        consonant_count += 1
    if char.isupper():
        upper_case_count += 1
    elif char.islower():
        lower_case_count += 1

print(f"Number of vowels: {vowel_count}")
print(f"Number of consonants: {consonant_count}")
print(f"Number of uppercase characters: {upper_case_count}")
print(f"Number of lowercase characters: {lower_case_count}")
