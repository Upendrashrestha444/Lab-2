#1. Write a program to input n numbers and store them in a list. Then perform the following operations:

#  i) Using built in functions                          # ii) without using built-in functions:
#a. Find the maximum and minimum number                 #a. Find the maximum and minimum number 
#b. Sort the list in ascending order                    #b. Sort the list in ascending order
#c. Remove duplicate elements                           #c. Remove duplicate elements

n=int(input("How many number do you want to enter? \n"))
print()
l=[]
for i in range(1,n+1):
    x=int(input(f"Enter Number {i}: "))
    l.append(x)
print("The list you entered is:", l)
print("---> USING BUILT-IN FUNCTION:\n")
maximum=max(l)
minimum=min(l)
print("The maximum number is:", maximum)
print("The minimum number is:", minimum)
sorted_list=sorted(l)
print("The sorted list is:", sorted_list)
unique_list=list(set(l))
y=sorted(unique_list)
print("The list with duplicates removed is:", y)

      


