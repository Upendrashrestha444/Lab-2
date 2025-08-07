#Write a program that receives a list of tuples representing (x, y) coordinates. Determine whether the points form a straight line.
n=int(input("How many co-ordinates do you want to enter:\n ")) 
points=[]
for num in range(n):
    x=int(input(f"Enter the x co-ordinates for point {num+1}:  "))
    y=int(input(f"Enter the y co-ordinates for point {num+1}:  "))
    points.append((x,y))
co_ordinates=tuple(points)
print("The co-ordinates you entered is:", co_ordinates) 
straight_line=True
x0,y0=co_ordinates[0]
x1,y1=co_ordinates[1]
for i in range(2,n):
    xi,yi=points[i]
    if (y1-y0)*(xi-x0)!=(yi-y0)*(x1-x0):
        straight_line=False
        break

if straight_line:
    print("The points form a straight line.")
else:
    print("The points do not form a straight line.")



    
                   
    
     