#map
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'SanFrancisco',
    'MI': 'Detroit', 
    'FL': 'Jacksonville'
}

#增加一些城市
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print cities
print('-' * 10)
print("NY State has:", cities['NY'])
print("OR State has:", cities['OR'])

#print states
print('-' * 10)
print("Michigan's abbreviation is:", states['Michigan'])
print("Florida's abbreviation is", states['Florida'])

#use the state then cities dict
print('-' * 10)
print("Michigan's has:", cities[states['Michigan']])
print("Florida's has", cities[states['Florida']])

#print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#now do both at the same time 
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
#safely get a abbreviation by state that might not be there
state = states.get('Texas')
if not state:
    print("Sorry, no Texas")

#get a city with a default value
city = cities.get("TX", "Does No Exitst")
print(f"the city for the state 'Tx' is : {city}")