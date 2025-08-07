#Create a program that reads a sentence from the user and stores each word as an element of a list. Then count the frequency of each word using only lists.
s=input("Enter the sentence:\n")
words=s.split()
l=[]
for word in words:
    if word not in l:
        count=0
        for w in words:
            if w==word:
                count+=1
        print(f"The word {word} occurs {count} times. ")   
        l.append(word)