import requests

url = "https://api.thecatapi.com/v1/images/search"

# sending get request and saving the response as response object
r = requests.get(url=url)

# extracting data in json format
data = r.json()

cat_picture = data[0]["url"]
