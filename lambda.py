people = [
    {"name": "Jack", "house": "New Jersey"},
    {"name": "Jill", "house": "New York"},
    {"name": "Max", "house": "California"}
]

def f(person):
    return person["name"]

people.sort(key=f)

print(people)