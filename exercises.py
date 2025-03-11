# Exercise 0: Example

def example_list_function():
  example_list = ['element1', 'element2', 'element3']
  for element in example_list:
      print(element)

example_list_function()

# Exercise 1: List and Indexing
#
# Create a list named students containing at least three student names (strings).
# Assign the second student’s name to a variable named first_student.
# Assign the last student’s name to a variable named last_student.

def manage_students():
    students = ['Zaid', 'Ali', 'Ahmed']
    first_student = students[1]
    last_student = students[2]
    return f'{first_student} {last_student}'

print('Exercise 1:', manage_students())

print('========================')

# Exercise 2: Loop and String Concatenation

def combine_foods():
    foods = ("Pizza", "Burger", "Sushi")
    meal = ""

    for food in foods:
        meal += food + ' '
    
    return meal
    
print('Exercise 2:', combine_foods())

print('========================')

# Exercise 3: Slicing Tuples
#
# Using the slice operator, assign a new tuple containing only the last two food strings in the foods to a variable named last_two_foods.

def slice_foods():
    foods = ("Pizza", "Burger", "Sushi", "Salad")
    last_two_foods = foods[2:4]
    return last_two_foods

print('Exercise 3:', slice_foods())

print('========================')

# Exercise 4: Dictionaries and String Formatting

def hometown_info():
    home_town = {
        "city": "Hamad Town",
        "state": "Bahrain",
        "population": 6500
    }

    home_town_message = f'I was born in {home_town["city"]}, {home_town["state"]} - population of {home_town["population"]}'

    return home_town_message

print('Exercise 4:', hometown_info())

print('========================')

# Exercise 5: Iterating Over Dictionary Items

def list_home_town_items():
    home_town = {
        "city": "Hamad Town",
        "state": "Bahrain",
        "population": 6500
    }
    home_town_items = []

    for key, val in home_town.items():
        home_town_items.append(f'{key} = {val}')
    
    return home_town_items

print('Exercise 5:', list_home_town_items())