# Recursion for fibonacci

fn_series = [0, 1]


def fibonacci_recursion(fnumber):

    if len(fn_series) >= fnumber > 0:
        return fn_series[fnumber - 1]
    else:
        fn = fibonacci_recursion(fnumber - 1) + fibonacci_recursion(fnumber - 2)
        if fnumber > len(fn_series):
            fn_series.append(fn)
        return fn


number = int(input('Enter a number, N, N>=2 : '))

fibonacci_recursion(number)

print(fn_series)
