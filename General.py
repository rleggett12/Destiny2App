print("Welcome to my Destiny 2 app")
print("designed by: Rian Leggett - 2017")


choice = input("Please select your class: Hunter, Titan or Warlock")
choice = choice.lower()

while choice != " ":
    
    if choice == "hunter":
        open("hunter.py", r)
        choice = " "
        break while

    elif choice == "titan":
        open("titan.py", r)
        choice = " "
        break while

    elif choice == "warlock":
        open("warlock.py", r)
        choice = " "
        break while

    else:
        print("please enter one of the three prompted classes")
        choice = "a"

    choice = input.lower("Please select your class: Hunter, Titan or Warlock")
    choice = choice.lower()

print("success!")


