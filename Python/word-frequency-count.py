# # Count word frequency and display results in descending order(string).
text = input("Enter a string: ").lower()
words = text.split()
freq = {}
# for word in words:
#     freq[word] = freq.get(word, 0) + 1
# # Sort by word (string), not by count
# sorted_freq = sorted(freq.items(), key=lambda x: x[0], reverse=True)
# for word, count in sorted_freq:
#     print(word, ":", count)
 
for word in words:
    freq[word] = freq.get(word, 0) + 1
# Sort by frequency (descending)
sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_freq:
    print(word, ":", count)

