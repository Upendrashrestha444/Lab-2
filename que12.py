#Create a dictionary to store student names as keys and their scores in three subjects as values (in a list). Write functions to:
#a. Display the average marks of each student
#b. Find the topper
#c. Update the marks of a student

d={}
n=int(input("Enter the no. of students:\n"))
for i in range(1,n+1):
    name=input(f"Enter the name of student ({i}):")
    marks=list(map(int,input("Enter the marks in 3 subjects with spaces:\n").split()))
    d[name]=marks
def average_marks(marks):
    return sum(marks)/len(marks)

def topper(score):
    highest_percentage = 0
    topper_name = ""
    for name, marks in score.items():
        total_marks = sum(marks)
        percentage = total_marks / (len(marks)) 
        if percentage > highest_percentage:
            highest_percentage = percentage
            topper_name = name
    return topper_name, highest_percentage

def update_marks(score, name):
    if name in score:
        new_marks = list(map(int, input(f"Enter new marks for {name} (3 subjects): ").split()))
        score[name] = new_marks
        return f"Marks updated for {name}: {score[name]}"
    else:
        return f"Student not found."


print("1.AVERAGE MARKS:")
print("2.FIND TOPPER")
print("3.UPDATE THE NAME OF STUDENT")
while True:
 choice=int(input("Enter the choice:\n"))
 if choice==1:
    a=input("Enter the name of student to know average marks:\n")
    if a in d:
        avg=average_marks(d[a])
        print(f"Average marks of {a} is {avg:.2f}")
    else:
        print("Student not found.")
        
 elif choice==2:
    topper_name,highest_percentage=topper(d) 
    print(f"The topper is {topper_name} with {highest_percentage:.2f} percentage.\n")
 elif choice==3:
     b=input("Enter the name of student to update its data.\n")
     if b in d:
        print(update_marks(d,b))
     else:
        print("Student not found.")  
 else:
    print("Please Enter the valid choice.")        




     