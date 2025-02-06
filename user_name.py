def name_check(first_name, last_name):
    if len(first_name) < 2 or len(last_name) < 2:
        print("Please enter a first and last name with 2 characters or more.")
    else:
        print(len(first_name))
        print(len(last_name))
        print(f"Welcome user: {first_name} {last_name}!.")
name_check("Devon","Anderson")        