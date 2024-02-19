n = int(input("Enter the size of the array"))
li = []
count = 1
for i in range(n):
    li.append(int(input("Enter the elements")))
print(li)
maxval = li[0]
for i in range(1,n):
    if li[i]>maxval:
        count += 1
        maxval=li[i]
print("Number of elements greater than their immediate next element:", count)

