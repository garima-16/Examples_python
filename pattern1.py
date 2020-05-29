#Program to create a pattern
n=int(input("print n"))
for i in range(1,n,2):
    for j in range( 1,n-i ):
        print (end=' ')
    for j in range(1,i+1):
        print (i,end=' ')
    print()
