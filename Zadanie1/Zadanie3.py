def is_prime(n):
    if n >= 2:
        for y in range(2,n):
            if not ( n % y ):
                return "Ta liczba nie jest liczbą pierwszą"
    else:
	    return "Ta liczba nie jest liczbą pierwszą"
    return "Ta liczba jest liczbą pierwszą"

n = int(input("Wprowadź liczbę: "))
print(is_prime(n))

