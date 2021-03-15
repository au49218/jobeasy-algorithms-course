# Write a Python function, which will count how many times a character
# (substring) is included in a string. DON’T USE METHOD COUNT


def count_chars(count_str):

    char_count = 0

    for i in count_str:
        if i == 'a':
            char_count = char_count + 1

    return str(char_count)


sentence = "   I   am learning     algorithms  in      python"
print('Count: ' + count_chars(sentence))
