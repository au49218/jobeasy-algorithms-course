# Enter a string of words separated by spaces. Find the longest word.

def word_length(string):

    length = 0
    word_long = ""

    for word in string.split():
        if len(word) > length:
            length = len(word)
            word_long = word

    return length, word_long


sentence = "I am learning algorithms in python"
print(word_length(sentence))
