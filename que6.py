#6.Write a program to create a tuple of n numbers, then find:
#a. The average of the numbers
#b. The median
#c. The mode (without using libraries)

x=list(map(int,input("Enter the numbers separated by spaces:\n").split()))

for i in range(len(x)):
    for j in range(i+1,len(x)):
        if x[i]>x[j]:
            x[i],x[j]=x[j],x[i]

print("The sorted list is:",x)
t=tuple(x)
print(f"The tuple is: {t}")
sum=0
for i in range(len(t)):
    sum+=t[i]
average=(sum)/len(t)
print(f"The average of the numbers is : {average}")

n=len(t)
if n%2!=0:
    median=t[n//2]
else:
    median=t[((n//2 -1)+n//2)//2]    

print("The median of the numbers is:",median) 


frequency={}
for num in t:
    if num in frequency:
        frequency[num]+=1
    else:
        frequency[num]=1  

max_frequency=max(frequency.values() )

modes=[]
for num in frequency:
    if frequency[num]==max_frequency:
        modes.append(num)
print(f"The mode of the numbers is:{modes}")        



       


    




