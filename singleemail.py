import yagmail as email
import os 


sender = "sipuakk@gmail.com"
reciever = "exclusivebloh@gmail.com"

password = os.getenv("EMAIL_PASSWORD")

subject = "this is for  automation testing 2"

content = """
    hello there!
"""

yag = email.SMTP(user = sender , password = password)

yag.send(to = reciever, subject = subject, contents = content)
print("sent")