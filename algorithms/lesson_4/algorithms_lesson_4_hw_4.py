# Find and replace a substring in a string for another substring.
# User enter from a keyboard a string and both substrings.
# DON’T USE METHOD REPLACE


def string_find_replace(stringvalue, stringfind, stringreplace):

    stringresult = ''

    for i in stringvalue:
        if i == stringfind:
            i = stringreplace
        stringresult += i

    return stringresult


string_value = str(input('Enter a string: '))
string_find = str(input('Enter a string to find: '))
string_replace = str(input('Enter a string to replace: '))

string_find_replace(string_value, string_find, string_replace)

print("String value: " + string_value)
print("String find: " + string_find)
print("String replace: " + string_replace)
print("String result: " + string_find_replace(string_value, string_find, string_replace))
