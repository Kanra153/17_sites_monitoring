# Sites Monitoring Utility

Script allows you to monitor sites health. It will show you days until domen's name exploration and if the site is responding with 200 code. To use this script you need to have a text file with urls. 

# How to Launch

Fist you should install missing libraries.
```
pip install -r requirements.txt
```
Then launch script.
```
$ python sites_health.py path/to/your/file
https://devman.org/
Is server respond with 200?: True
Days until expiration:  179

https://github.com/
Is server respond with 200?: True
Days until expiration:  952

https://www.twitch.tv
Is server respond with 200?: True
Days until expiration:  830
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
