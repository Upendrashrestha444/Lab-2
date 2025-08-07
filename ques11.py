#Given a list of numbers with duplicates, use a set to remove the duplicates. Then,convert it back to a sorted list and display the result.
l=[900,500,600,200,100,100,100,600,500,1000,700,700]
s=set(l)
new_list=sorted(s)
print(new_list)