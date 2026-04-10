import requests

API_KEY = "AIzaSyAzrYhIFWlLxv08iuSCuKbZ4h5XE1SK62g"

url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"

response = requests.get(url)

print(response.json())