# Creating a dictionary
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("Creating Dictionary: ")
print(Dict)

# Accessing a element using key
print("Accessing a element using keys: ")
print(Dict['Name'])

# Accessing a element using get() method
print('Accessing a element using get:')
print(Dict.get(1))

# creation using Dictioanry comprehension
myDict = {x: x**2 for x in [1, 2, 3, 4, 5]}
print(myDict)