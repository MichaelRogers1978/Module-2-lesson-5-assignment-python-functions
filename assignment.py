# task1

def addition(number_one, number_two):
    return number_one + number_two
def subtraction(number_one, number_two):
    return number_one - number_two
def multiplication(number_one, number_two):
    return number_one * number_two
def division(number_one, number_two):
    if number_two == 0:
        print("division by zero is not allowed.")
    else:
        return number_one / number_two

user_operation = input("What operation are you going to perform? (+, -, *, /)")
user_number_one = int (input("what is the first number? "))
user_number_two = int (input("what is the second number? "))

if user_operation == "+":
    print(addition(user_number_one, user_number_two))
elif user_operation == "-":
    print(subtraction(user_number_one, user_number_two))
elif user_operation == "*":
    print(multiplication(user_number_one, user_number_two))
elif user_operation == "/":
     print(division(user_number_one, user_number_two))
else:
    print("invalid operation, try again.")



#task2mber 

#Write a function that lets the user add items to a list.
#Include a function to remove items from the list.
#Add a function that prints out the entire list in a formatted way.

def list(item_one, item_two, item_three):
    return item_one, item_two, item_three
def remove(item_one, item_two, item_three):
    return item_one, item_two, item_three




user_item_one = input("what is your first item? ")
user_item_two = input("what is your second item? ")
user_item_three = input("What is your third item?") 

# This is an empty list, where we will store the items once we get it
grocery_list = [] 

# Start by asking users to build their grocery list 

if user_item_one and user_number_two and user_item_three:
    grocery_list.append(user_item_one)
    grocery_list.append(user_item_two)
    grocery_list.append(user_item_three)
    print(grocery_list)

else:
    print("Go home, you forgot your list.")

user_input = str(input("Oops, you added items, which one would you like to remove?"))
if user_input == ("check if your grocery_list has the item to remove in it."):
    if grocery_list.remove():
        print(grocery_list)
else: 
    print("Sorry, that item isn't in your list")
    
    

