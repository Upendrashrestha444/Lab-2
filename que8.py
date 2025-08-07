#8. Write a program to input two sets of student roll numbers: one who play cricket and another who play football. Find:
#a. Students who play both sports
#b. Students who play only one sport
#c. Students who play neither (given a master list of all students)
master_list=set(map(int,input("Enter the roll number of all students with spaces:\n").split()))
c=set(map(int,input("Enter the roll no. of students who play cricket separated by spaces:\n").split()))
f=set(map(int,input("Enter the roll no. of students who play football separated by spaces:\n").split()))
both=c & f
only_one= c ^ f
neither= master_list-(c|f)
print("\n{:<30}{:<30}".format("Category", "Roll Numbers"))
print("-"*60)
print("{:<30}{:<30}".format("Both Sports", str(sorted(both))))
print("{:<30}{:<30}".format("Only One Sport", str(sorted(only_one))))
print("{:<30}{:<30}".format("Neither Sport", str(sorted(neither))))

