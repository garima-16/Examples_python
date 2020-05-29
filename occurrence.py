#Program to find the occurrences of a character in a string
string1=input("enter any string ")
ch=input("enter a character ")
count=0
for i in string1:
    if ch==i:
        count+=1
print("number of occurrences of character in string ",count)
        