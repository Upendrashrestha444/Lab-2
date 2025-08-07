#Create a set of random numbers. Add more numbers until the set has 10 unique elements. Also, remove the smallest and largest element.
import random
s=set()
while(len(s)<10):
    ran=random.randint(0,999)
    s.add(ran)
n=sorted(s)    
print("The set of numbers is: ",n)   
largest=max(n)
smallest=min(n)
n.remove(largest)
n.remove(smallest)
print(f"The new list with greatest and smallest number removed is: {n}")