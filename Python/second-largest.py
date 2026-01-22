
# Program to find the second largest array element.
arr = [10, 5, 20, 8, 15]
arr = list(set(arr)) 
arr.sort(reverse=True)
print("Second largest element:", arr[1])

