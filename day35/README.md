### Create an environment variable to add another layer of protection for your API Keys its best not to hard code credentials    

API DOCS
https://openweathermap.org/api/one-call-3

WEATHER CONDITION CODES
https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2

To test the code - find a location with the desired weather alert
https://www.ventusky.com/

TWILIO
https://www.twilio.com/


# Use environmental variables
```bash
export TWILIO_ACCOUNT_SID=<TOKENID>
export TWILIO_AUTH_TOKEN=<TOKENID>

echo $TWILIO_ACCOUNT_SID
echo $TWILIO_AUTH_TOKEN
```

# Use a cron job to set the script to run at 5am everyday 
https://crontab.guru/

# Check current linux system time to ensure cronjob matches system
```bash
date
```

```bashcron
which python3
/usr/bin/python3
crontab -e
0 5 * * * /usr/bin/python3 /tmp/test/main.py
crontab -r 
```