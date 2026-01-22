
# Given a list of email strings, filter out only valid emails(assume a valid email contains '@' and '.').
import re
emails=input("enter emails:").split()
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
valid_emails = [e for e in emails if re.match(pattern, e)]
print(valid_emails)

