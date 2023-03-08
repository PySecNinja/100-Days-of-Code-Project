## HTTP Response Codes
```plain text
Informational responses (100 – 199)
Successful responses (200 – 299)
Redirection(Maybe permissions) messages (300 – 399)
Client error responses (400 – 499)
Server error responses (500 – 599)
```
https://www.webfx.com/web-development/glossary/http-status-codes/

### To run this script in linode or on your own linux box
```plain text
sudo yum install git -y               #Install Git
sudo yum install python-pip -y        #Install PIP
pip3 install -r requirements.txt      #Install python modules
```

### run the script in the background 
```bash
nohup python3 main.py &
```

#### to see the running scripts on the box please note the number to the left 

```plain text
[root@192-46-218-170 day33]#jobs
[1]+  Running                 python3 main.py &
```

### to stop the script use the number to the left ie:
```bash 
kill %1
```

##Kayne west quote API
https://kanye.rest/

## To get current coordinates of your location:
https://www.latlong.net/

## SunRise-SunSet API
https://sunrisesunset.io/api/
