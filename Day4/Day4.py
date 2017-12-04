#!python

valid_count=0
def anagram(word):
    letters = list(word)
    letters.sort()
    return ''.join(letters)

with open('input.txt') as f:
    for line in f:
        invalid=0
        words={}
        for word in line.split():
            word=anagram(word)  # Comment out for Day4.1
            invalid = words.get(word, 0)
            if invalid == 0:
                words[word]=1
            else:
                break;
        if invalid == 0:
            valid_count += 1

print(valid_count)