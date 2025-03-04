#!/usr/bin/python3
import requests
import passwords

url = "https://httpbin.org/basic-auth/jtaylor125/test"

r = requests.get(url, auth=(passwords.USER,passwords.PASS))
print(r.text)
