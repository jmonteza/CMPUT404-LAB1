import requests

print(requests.__version__)

print(requests.get("https://www.google.com").text)

GITHUB_URL = "https://raw.githubusercontent.com/jmonteza/CMPUT404-LAB1/master/find_version.py"

print(requests.get(GITHUB_URL).text)

