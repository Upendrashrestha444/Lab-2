 #2.Given two lists of integers, write a program to merge them into a single list and then remove the elements that are common in both.

l1=[2,4,6,8,10,12,14,16]
l2=[4,8,12,16]
common=set(l1)&set(l2)
new_l1=[x for x in l1 if x not in common]
new_l2=[x for x in l2 if x not in common]
print(f"The merged list with no common elements is:{new_l1+new_l2}")





                        
