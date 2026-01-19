#write a function that takes a string and returns True if its a palindrome else false.
word="Mam"
if word.lower() in word[::-1].lower():
    print("Palindrome")
else:
    print("Not Palindrome")