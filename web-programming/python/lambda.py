people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"},
]


# If we only do sort then we get error message saying TypeError: < cannot be done
# To solve that error we can pass a function to sort function telling how to sort

# def my_function(person) :
#     return person["name"]

# Becuase this function is so small python provide a simple inline function called lambda function

people.sort(key=lambda people: people["name"])
print(people)