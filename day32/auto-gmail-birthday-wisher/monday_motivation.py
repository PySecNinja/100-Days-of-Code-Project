import smtplib
import random
import datetime as dt

GMAIL_USERNAME = "lulz.testing7878@gmail.com"
GMAIL_PASSWORD = "opawaglghwqtcytc"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(GMAIL_USERNAME, GMAIL_PASSWORD)
            connection.sendmail(
                from_addr=GMAIL_USERNAME,
                to_addrs=GMAIL_USERNAME,
                msg=f"Subject:Monday Motivation\n\n{quote}"
            )
    except:
        print("Your Mail Has Failed To Send. Check the Firewall")
