#Check if number is palindrome
Number ="123454321"
Number1 = Number
Number2 = Number1[::-1]
if Number1 == Number2 :
    print('Given number is a palindrome')
else:
    print('Given number is not a palindrome')