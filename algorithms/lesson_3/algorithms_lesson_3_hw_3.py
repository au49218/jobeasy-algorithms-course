# Recursion for digital root

def digital_root(dnumber):
    if (dnumber < 10):
        return dnumber
    dnumber = dnumber % 10 + digital_root(dnumber // 10)
    return digital_root(dnumber)


number = int(input('Enter a number: '))

print((digital_root(number)))
