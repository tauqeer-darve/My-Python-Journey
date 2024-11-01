#Function with input(combination of positional and keyword attributes)
def display_user_profile(name, age, location, occupation="Not specified", hobbies=None):
    print("User Profile Summary")
    print("=====================")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Location: {location}")
    print(f"Occupation: {occupation}")

    if hobbies:
        print("Hobbies:")
        for hobby in hobbies:
            print(f" - {hobby}")
    else:
        print("Hobbies: Not specified")


display_user_profile(
    "Alice",
    28,
    "New York",
    occupation="Software Engineer",
    hobbies=["Reading", "Hiking", "Photography"]
)

display_user_profile(
    "Bob",
    34,
    "San Francisco"
)
