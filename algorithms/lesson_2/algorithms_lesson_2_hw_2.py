# Zeros not for Heros
# Numbers ending with zeros are boring. They might be fun in your world, but not here.
# Get rid of them. Only the ending ones.
# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105
# Zero alone is fine, don't worry about it. Poor guy anyway


def removeEndingZeros(number):

    numberclean = number.rstrip("0")
    print(numberclean)


removeEndingZeros("1450")
removeEndingZeros("960000")
removeEndingZeros("1050")
removeEndingZeros("-1050")
removeEndingZeros("0")
