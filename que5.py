#5. Write a Python function that accepts a list and returns a new list containing only the elements at even indexes and those that are prime numbers.

def is_prime(n):
    if n==0 or n==1:
        return False
    for i in range (2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

z=input("Enter the numbers with spaces:\n")
x=list(map(int,z.split()))
print("The list you entered is:", x)

result=[]
for j in range(len(x)):
    if j%2==0 and is_prime (x[j]):
        result.append(x[j])
print(f"The new list is: {result}")






 



