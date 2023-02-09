# Student Grades Assignment by Ibrahim Ismayilov

# Importing the random module 
import random

# Intializing grades list
grades_list = []

# Generating 35 random grades
for i in range(35):
    grades_list.append(random.randint(1, 99))

# Menu Loop
loop = True
while loop:

    # Print Main Menu
    print("\nMAIN MENU")
    print("1. Display All Grades")
    print("2. Display Honours")
    print("3. Stats")
    print("4. Randomize Grades")
    print("5. Exit")

    # Get Menu Selection From The User
    selection = input("Enter Selection (1-5): ")

    # Action Based on Menu Selection
    if selection == "1":
        for grade in grades_list:
            print(f"\n{grade}")
    elif selection == "2":
        grades_count = 0
        for grades in grades_list:
            if grade > 80:
                grades_count += 1
                print(f"\n{grade}")
        print(f"\n{grades_count}")
    elif selection == "3":
        print("\nSTATS")
        highest_grade = max(grades_list)
        lowest_grade = min(grades_list)
        average_grade = sum(grades_list) / len(grades_list)
        print(f"Highest Grade: {highest_grade}%")
        print(f"Lowest Grade: {highest_grade}%")
        print(f"Average Grade: {average_grade}%")
    elif selection == "4":
        print(grades_list)
        for i in range(len(grades_list)):
            grades_list[i] = random.randint(1, 99)
        print(grades_list)
        print("GRADES HAVE BEEN RANDOMIZED")
    elif selection == "5":
        loop = False