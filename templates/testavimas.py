import requests


url = "https://weatherapi-com.p.rapidapi.com/current.json"

querystring = {"q":"vilnius"}

headers = {
	"X-RapidAPI-Key": "7dc783f7c0msh74790f20df568edp13e418jsn7a470f461168",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

print(response)
