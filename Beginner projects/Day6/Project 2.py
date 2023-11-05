
travel_log = [
   {
   "country": "Morocco",
    "visits":  ["Rabat", "Marrakech", "Fes"], 
    "visits": 20
    },
]

def add_new_country(country_visited, cities_visited, times_visits):
    new_country = {}
    new_country["country"] = country_visited 
    new_country["cities"] = cities_visited 
    new_country["visits"] = times_visits
    travel_log.append(new_country)
    

add_new_country("Russia", 2 , ["Moscow"])
print(travel_log)
