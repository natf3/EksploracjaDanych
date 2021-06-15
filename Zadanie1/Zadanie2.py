def isPalindrome(s):
    return s == s[::-1]
 
 
s = input("Wprowadz ciag znakow: ")
ans = isPalindrome(s)
 
if ans:
    print("Jest palindromem")
else:
    print("Nie jest palindromem")