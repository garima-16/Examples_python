#Program to check if a number is palindrome or not
import math
n=int(input("enter n"))
l = list(map(int, str(n)))
length=len(l)
for i in range(0, math.floor(length/2)):
    if (l[i]==l[length-i-1]):
        continue
    else:
        print ("not a palindrome")
        break
else:
    print ("palindrome")