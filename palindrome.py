# first user must check python version, I am using python 3.8.3
def is_palindrome(s):
    for x in range(0, len(s)//2):
        if s[x] != s[-1 - x]:
            return False
    return True
str = input ('Enter any word to test whether it is a palindrome ')
if is_palindrome(str) == True:
    print (str, 'is a palindrome')
else:
    print(str, 'is not a palindrome')