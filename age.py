def my_input(prompt: str):
    while True:
        age = input(prompt)

        try:
            int(age)
        except ValueError:
            print("That is not a valid age.")
            continue
        
        return age

age = my_input("Age: ")
a = int(age)
if a <= 0 or a >= 100:
    print("No way")
elif a > 50:
    print("You are older than 50 years old")
elif a < 50:
    print("You are younger than 50 years old")
else:
    print("You are 50 years old")
