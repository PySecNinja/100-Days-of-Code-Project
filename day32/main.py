#To run and test the code you need to update 4 places:
# 1. Change GMAIL_USERNAME/GMAIL_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.

import smtplib
import random
import datetime as dt
import pandas as pd

GMAIL_USERNAME = "lulz.testing7878@gmail.com"
GMAIL_PASSWORD = "opawaglghwqtcytc"

# Check if today matches a birthday in the birthdays.csv
# Create a tuple from today's month and day using datetime. e.g.
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# Use pandas to read the birthdays.csv
birthdays_df = pd.read_csv("birthday.csv")

#Dictionary comprehension= for pandas DataFrame:
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in birthdays_df.iterrows()}

#Then we could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from templates and replace the [NAME] with the person's actual name from birthdays.csv
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

# Send the letter generated to that person's email address.
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(GMAIL_USERNAME, GMAIL_PASSWORD)
            connection.sendmail(from_addr=GMAIL_USERNAME, 
                                to_addrs=birthday_person["email"], 
                                msg=f"Subject: Happy Birthday!\n\n{contents}")
    except:
        print("Your Mail Has Failed To Send. Check the Firewall")