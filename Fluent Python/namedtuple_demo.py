from collections import namedtuple
City = namedtuple('City', 'name country population coordinates ')
tokyo = City(name = 'Tokyo', country = 'Japan', population = 36.933, coordinates = (1, 1))
print(tokyo.name)
print(tokyo.country)
print(tokyo.population)
print(tokyo.coordinates)