travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above 
#First *fork* your copy. Then copy-paste your code below this line 👇
#Finally click "Run" to execute the tests

# def add_new_country(country, no_of_visits, city):
#     travel_log.append({
#         "country":country,
#         "visits":no_of_visits,
#         "cities":city})

# *********************************

def add_new_country(country, no_of_visits, city):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = no_of_visits
    new_country["cities"] = city
    travel_log.append(new_country)


#🚨 Do NOT change the code below
add_new_country("India", 2, ["Bangalore", "Kerala"])
print(travel_log)