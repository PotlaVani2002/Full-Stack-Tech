#write a function that takes a string and returns True if its a palindrome else false.
def palindrome(word):
    if word.lower() in word[::-1].lower():
       return True
    else:
        return False

word="Mam"
if palindrome(word):
    print("Palindrome")
else:
    print("Not Palindrome")
