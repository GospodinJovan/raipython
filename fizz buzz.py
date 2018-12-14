#fizz buzz at the beginning with 3 and 7, maybe variable

def fizz_buzz(n):

    if not (n) % 15:
        return "Fizz Buzz"
    elif not (n) % 5:
        return "Buzz"
    elif not (n) % 3:
        return "Fizz"
    else:
        return str(n)

x=(21)
print (fizz_buzz(x))
