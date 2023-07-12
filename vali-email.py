import re 
def valid_email(email) : 
    regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+$"
    match = re.match(regex, email )
    return bool(match)
email1 = "sha@gmail.com"
email2 = "sha12@harvard.edu"
email3 = "sha@gmail.com1"
print(valid_email(email1))
print(valid_email(email2))
print(valid_email(email3))
