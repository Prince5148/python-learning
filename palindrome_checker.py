num=int(input("Enter Number:"))
original=num
reverse=0

while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10

if original==reverse:
    print("this is the palindrome number")
else:
    print("this is not palindrome number")

#string palindrome checker

text=input("enter any string:")
if text==text[::-1]:
    print("the string is palidrome ")
else:
    print("the string is not palindrome")