#4. Write a program to simulate a basic stack and queue using a list. Provide options to push, pop (stack), enqueue, and dequeue (queue).



stack=[]
queue=[]


print("╔══════════════════════════════════════╗")
print("║       STACK AND QUEUE OPERATION      ║")
print("╠══════════════════════════════════════╣")
print("║ 1. Stack push                        ║")
print("║ 2. Stack pop                         ║")
print("║ 3. Queue enqueue                     ║")
print("║ 4. Queue dequeue                     ║")
print("║ 5. Display                           ║")
print("║ 6. Exit                              ║")
print("╚══════════════════════════════════════╝")
for n in range(1000):   
  choice=int(input("Enter the choice (1/2/3/4/5/6):\n"))

  if choice==6:
        print("Exiting the program. Goodbye!")
        break
 
  if choice==1:
            x= input("Enter data to push onto the stack:\n ")
            stack.append(x)
            print(f"{x} pushed onto the stack.\n")

  elif choice==2:
            if len(stack)==0:
                print("Can't pop,The stack is empty.\n ")   
            else:
                m=stack.pop()
                print(f"Popped {m} from the stack.")
  elif choice==3:
            y=input("Enter the data to enqueue into the queue:\n")           
            queue.append(y)
            print(f"{y} enqueued into the queue.\n")
  elif choice==4:
            n=queue.pop(0)
            print(f"{n} is dequeued from the queue.")
  elif choice==5:
            print(f"stack(bottom to top): {stack} ")   
            print(f"Queue(Front to rear): {queue}") 
  else:
         print("Enter valid input.")           

