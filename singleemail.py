import yagmail as email
import os 
import pandas as pd


sender = "sipuakk@gmail.com"
reciever = "exclusivebloh@gmail.com"

password = os.getenv("EMAIL_PASSWORD")
subject = "this is for  automation testing 2"

# create an SMTP object with the gmail credentials
yag = email.SMTP(user = sender , password = password)

# read the csv file and convert it to a pandas dataframe

data = pd.read_csv("details.csv")

# convert the data to a dataframe for easy handling and iteration over rows
df = pd.DataFrame(data)


for index, row in df.iterrows():
    content = [f"""
        hello {row["name"]}! You have to pay
        {row["amount"]}
    """, row["filepath"]]
    yag.send(to = row["email"], subject = subject, contents = content)
    print(f"sent email to {row["email"]}")





