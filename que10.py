#Write a Python function that accepts a sentence and returns a set of all unique vowels used.
def unique_vowels(sentence):
    vowels={"a","e","i","o","u"}
    sentence= sentence.lower()
    unique={ch for ch in sentence if ch in vowels}
    return unique

x=input("Enter a sentence:\n")
u=unique_vowels(x)
print(f"The set of all the unique vowels used in the snetence are: {u}")
