inf = {"location":{"name":"Vilnius","region":"Vilniaus Apskritis","country":"Lithuania","lat":54.68,"lon":25.32,"tz_id":"Europe/Vilnius","localtime_epoch":1655654924,"localtime":"2022-06-19 19:08"},"current":{"last_updated_epoch":1655650800,"last_updated":"2022-06-19 18:00","temp_c":23.0,"temp_f":73.4,"is_day":1,"condition":{"text":"Sunny","icon":"//cdn.weatherapi.com/weather/64x64/day/113.png","code":1000},"wind_mph":5.6,"wind_kph":9.0,"wind_degree":40,"wind_dir":"NE","pressure_mb":1008.0,"pressure_in":29.77,"precip_mm":0.4,"precip_in":0.02,"humidity":53,"cloud":0,"feelslike_c":25.3,"feelslike_f":77.5,"vis_km":10.0,"vis_miles":6.0,"uv":5.0,"gust_mph":4.5,"gust_kph":7.2}}
vocab = inf["location"]
vocab2= inf["current"]

cityName = vocab["name"]
countryName = vocab["country"]
temperature = vocab2["temp_c"]
wind = vocab2["wind_kph"]

data = (cityName, countryName, temperature, wind)
print(data)
