# #create a function that accepts a list & returns s new list with duplicates removed
def dup(l1):
    result = []
    for i in l1:
        if i not in result:
            result.append(i)
    return result

l1 = [10, 20, 10, 20, 40]
print(dup(l1))

