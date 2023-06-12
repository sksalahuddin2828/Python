import requests as req 

url: str = "https://checkip.amazonaws.com"

request = req.get(url)
ip: str = request.text

print("IP:", ip)

# Answer: IP: 27.88.12.100

#-----------------------------------------------------

import requests

def ip_address():
    url = "https://checkip.amazonaws.com"
    response = requests.get(url)
    ip = response.text
    print(f"Your IP Address is: {ip}")

ip_address()

# Answer: IP: 27.88.12.100

#-----------------------------------------------------

import requests

def ip_address():
    response = requests.get("https://api.ipify.org")
    ip_address = response.text
    print(f"Your IP Address is: {ip_address}")
    
ip_address()

# Answer: IP: 27.88.12.100
