
# Given a list of strings, return only those strings whose length is greater than a given number.
s=input("enter strings list: ")
n=int(input("enter number: "))
s2=s.split()
exist=False
for x in s2:
    if len(x)>n:
        print(x)
        exist=True
if not exist:
    print("No string have specified length")

