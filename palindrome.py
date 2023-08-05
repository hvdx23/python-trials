def pal(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return pal(s[1:-1])


string = input("Enter the string: ")
result = pal(string)
if result:
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")
