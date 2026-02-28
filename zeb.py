name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

current_year = 2026
age = current_year - birth_year

if age >= 18:
    print(name, "is eligible to vote ✅")
else:
    print(name, "is not eligible to vote ❌")