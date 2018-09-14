from string import ascii_letters

ascii_letters += " "

def longestWord(sen):
    sen = list(sen)
    for l in sen:
        if l not in ascii_letters:
            sen.remove(l)

    words = ""
    words = words.join(sen).split(" ")

    longest_word = words[0]
    for i in range(0, len(words)):
        if len(words[i]) > len(longest_word):
            longest_word = words[i]

    return longest_word
