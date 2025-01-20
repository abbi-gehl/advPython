# Abigail Gehlbach 1/16/25
# Lab 01 List Comprehensions

def div_seven(l):
    # return nums divisible by 7
    return [i for i in l if i % 7 == 0]


def three_digit(l):
    # return nums if they have the digit 3 in them
    return [i for i in l if '3' in str(i)]


def remove_vowels(s):
    # used string comprehension, syntax from:
    # https://blog.finxter.com/python-string-comprehension-a-comprehensive-guide/
    lookup = ['a', 'e', 'i', 'o', 'u']
    return ''.join(i for i in s if i not in lookup)


def find_short_words(s):
    # using split to separate string
    return [i for i in s.split() if len(i) < 4]


def str_len_dict(l):
    # doc from: https://peps.python.org/pep-0274/
    return {k: len(k) for k in l}


# Testing functions

l1 = div_seven([i for i in range(1, 1001)])
print("Q1. " + str(l1))

l2 = three_digit([i for i in range(1, 1001)])
print("Q2. " + str(l2))

# remove vowels from str
s1 = remove_vowels("The Quick Brown Fox Jumps over The Lazy Dog")
print("Q3. " + s1)

# find all words less than 4 chars
s2 = find_short_words("I think list comprehensions are pretty cool and fun")
print("Q4. " + str(s2))

# dict comp to map str to len
d1 = str_len_dict(["testing", "one", "two", "three", "blastoff"])
print("Q5. " + str(d1))
