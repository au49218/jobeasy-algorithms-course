# Enter an irregular string (that means it may have space at the beginning
# of a string, at the end of the string, and words may be separated by several
# spaces). Make the string regular (delete all spaces at the beginning and end
# of the string, leave one space separating words).


def remove_spaces(string):

    strip_string = ' '.join(filter(None, string.split(' ')))

    return strip_string


sentence = "   I   am learning     algorithms  in      python"
print('Before:' + sentence)
print('After: ' + remove_spaces(sentence))
