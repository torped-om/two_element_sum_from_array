import string
import array
n=int(input("Enter no. of elements you want to put in array: "))
arr=[]
for x in range(n):
    elmt=int(input(f"Enter element {x+1}: "))
    arr.append(elmt)
trg=int(input("Enter a number to find that any two elements summed up make it or not: "))
sum=0
count=0
x=0
i=1
while True:
    for (i) in range(n):
        if i>x:
            sum=arr[x]+arr[i]
            if sum==trg:
                print(f"{x+1} and {i+1} terms summed up give {trg}")
                count+=1

    x+=1
    if not x!=n:
        break
if count==0:
    print(f"No Elemnents summed up give {trg}")