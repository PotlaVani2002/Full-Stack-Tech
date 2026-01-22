
# Remove duplicates from a list while preserving order using filter().
l1=[10,20,30,20,10,40]
sets=set()
orderl=list(filter(lambda x: x not in sets and not sets.add(x),l1))
print(orderl)

