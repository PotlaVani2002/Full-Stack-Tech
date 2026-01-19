# #count the number of vowels in a given string
word = "hello"
count = 0

for i in word:
    if i in "aeiouAEIOU":
        print(i)
        count = count + 1

print('Number of vowels in', word, 'is', count)
