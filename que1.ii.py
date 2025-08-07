# ii) without using built-in functions:
#a. Find the maximum and minimum number
#b. Sort the list in ascending order
#c. Remove duplicate elements

n=int(input("How many numbers you want to enter?\n"))
l=[]
for i in range(1,n+1):
    x=int(input(f"Enter number {i}: "))
    l.append(x)

print("The list you entered is:", l)
print()
print("#without using built-in functions:\n")
print()
maximum=l[0]
minimum=l[0]

for i in range(len(l)):
    if l[i]>= maximum:
        maximum=l[i]
    if l[i]<=minimum:
        minimum=l[i]          
print("The maximum number is:", maximum)
print("The minimum number is:", minimum)  

n=len(l)
for j in range(n):
   for i in range(0,n-j-1):
     if l[i]>l[i+1]:
      l[i],l[i+1]=l[i+1],l[i]
 
    
print("The ascending sorted list is:", l)

unique_list=[]
for item in l:
   if item not in unique_list:
      unique_list.append(item)
print("Unique list is:",unique_list)
   

                                             
   
      

   



      






