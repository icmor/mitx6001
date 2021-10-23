# Problem Set 1

## Question 1
def count_vowels(word):
    vowels = 0
    for letter in word:
        if letter in "aeiou":
            vowels += 1
    return vowels


## Question 2
def count_bobs(word):
    bobs = 0
    for i in range(0, len(word)-2):
        if word[i:i+3] == "bob":
            bobs += 1
    return bobs


## Question 3
def count_longest_alphabetical(word):
    longest = ''
    current = ''
    for letter in word:
        if not current or letter < current[-1]:
            current = letter
        else:
            current += letter
        if len(current) > len(longest):
            longest = current
    return longest
