string=input("Enter the string")
star=string.count("*")
hash=string.count("#")
if star>hash:
    print("Positive")
elif star<hash:
    print("Negative")
elif star==hash:
    print("Equal")
else:
    print("0")

s1=input("Enter the string")
star=0
hash=0
for i in s1:
    if i=="*":
        star=star+1
    elif i=="#":
        hash=hash+1
    else:
        print("0")

if(star>hash):
    print("Positive")
elif(hash>star):
    print("Negative")
else:
    print("0")

x=[0]*4
print(x)
