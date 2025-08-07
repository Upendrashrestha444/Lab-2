#Write a program that reads a text and counts the frequency of each character (excluding spaces and special characters) using a dictionary.
text=input("Enter the text:\n")
new_text="".join(ch.lower() for ch in text if ch.isalnum())
d={}
frequncy=0
for item in new_text:
    if item in d:
        d[item]+=1
    else:
        d[item]=1

print("The frequncy of each character in the text are:\n")
print(d)            

