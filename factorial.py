#Program to find the factorial of a number
def fact(n):
    fac=1
    while n>0:
        fac=fac *n
        n-=1
    print("factorial is ",fac)
fact(4)