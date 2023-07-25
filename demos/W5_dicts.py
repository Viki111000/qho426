#Initialise empty dictionary
d = {}
d2 = dict()
# print(type(d2))
#Initialise no-empty dictionary
phonebook = {"Thomas":7743434310, "Ruud": 73434343431, "July": 7746591029}
# print(phonebook)
#Print individual elements
name = input("Who you gonna call?")
if name in phonebook:
    print(f"Calling...{phonebook[name]}")
else:
    print(f"No number for {name}")
#Zipping two lists together into a dictionary
names = ["Marius", "Nazaret", "Michaela"]
ages = [23, 22, 21]
people = dict(zip(names, ages))
print(people)
#Values could be anything, but KEYS must beimmutable

#Traversing Dictionaries - accesing keys/values
for thing in people:
    print(thing)
for thing in people.values():
    print(thing)
for v, k in people.items():
    print(f"Person{k} is {v} years old")
