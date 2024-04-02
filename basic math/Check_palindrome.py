#check palindrome
n= int(input())
m=n
reversed_number=0
while(m!=0):
    last_digit=m%10
    reversed_number = reversed_number*10+last_digit
    m=m//10
if(reversed_number==n):
    print('Palindrome')
else:
    print('Not a Palindrome')
