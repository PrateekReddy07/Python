x=[0,0,0,0,0]
E=[7,0,5,1,3]
L=[1,2,1,3,4]
T=int(input("T="))
for i in range(0,T):
       x[i]=(x[i-1]+E[i])-L[i]
print("The maximum members in the crusie ship at the time is",max(x))

T = int(input("Enter the number of time steps (T): "))
x = [0] * T
E = []
L = []
for i in range(T):
    entry = int(input(f"Enter the entry value for time step {i + 1}: "))
    exit = int(input(f"Enter the exit value for time step {i + 1}: "))
    E.append(entry)
    L.append(exit)
for i in range(T):
    if i == 0:
        x[i] = E[i] - L[i]
    else:
        x[i] = x[i - 1] + E[i] - L[i]
print("The maximum members in the cruise ship at any given time is", max(x))


          
