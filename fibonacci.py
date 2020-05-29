
#Program to print n number of terms of the fibonacci series
def fib(n):
    n1, n2 = 0, 1
    while n>0:
        print(n1, end=' ')
        n1, n2 = n2, n1+n2
        n-=1
    print()
n=int(input("enter the number of terms of fibonacci series"))
fib(n)