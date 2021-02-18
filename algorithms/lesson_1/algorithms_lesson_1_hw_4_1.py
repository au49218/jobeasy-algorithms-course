# CodeWars - Regex validate PIN code
# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything
# but exactly 4 digits or exactly 6 digits.
# If the function is passed a valid PIN string, return true, else return false.

def valid_code(code):

    if code.isnumeric():

        code_length = len(code)

        if code_length == 4 or code_length == 6:
            print("Pass: Exact Length >", code)
        else:
            print("Fail: Not Exact Length >", code)
    else:
        print("Fail: Non-Numeric Value >", code)


valid_code("4571")
valid_code("45715")
valid_code("457178")
valid_code("4571F")