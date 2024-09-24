# List and Tuples

food = ["Bread","Carrots","Celery"]   # Array
#   index 0         1         2
print(food)
print(food[1])
print(food[0], food[1], food[2])

print("")

# How to replace array variable
food[0]="Ribeye"
print(food)
print(food[0], food[1], food[2])

print("")

# How to know the size of my list
print("The size of my list is", len(food))

print("")

# How to append an array variable
len(food)    # length of array
food.append("Cheese")
print(food)

print("")
# How to insert an array variable
food.insert(1,"ORANGE")
print(food)

print("")

# How to delete an array variable
food.pop(2)
print(food)

print("")

food.remove("Cheese")    # Code does not work as cheese does not exist but Cheese does
print(food)

food.append("Orange")
print(food)
food.remove("Orange")
print(food)

print("")

# Empty the list
food.clear()
print(food)

print("")

# A tuple, almost like a lit but you change the variables
cars = ("Ford", "Toyota", "Bentley")
print(cars)
print(cars[2])
#cars[2] = "Rolls Royce"     # Can't change the variables in tupils.    Take out the first comment to see
print(len(cars))
cars = cars + ("Mercedes",)
print(cars)

print("")

# Convert from list to tuple
temp = list(cars)
temp.remove("Mercedes")
cars = tuple(temp)
print(cars)