
# Input student name and marks.Return:total,average,grade(single function)
def grade(name, *args):
    total = 0
    count = 0

    for i in args:
        total += i
        count += 1

    if count != 0:
        avg = total / count
    else:
        avg = 0

    match avg:
        case _ if avg >= 80:
            result = 'Distinction'
        case _ if avg >= 70:
            result = 'First Class'
        case _ if avg >= 60:
            result = 'Second Class'
        case _ if avg >= 40:
            result = 'Third Class'
        case _ if avg >= 35:
            result = 'Pass'
        case _:
            result = 'Fail'

    return name, total, avg, result

print(grade("Vani",10,20,40,50))