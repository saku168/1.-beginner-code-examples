"""Check whether an integer is even or odd."""
try:
    number = int(input("Enter a whole number: "))
except ValueError:
    print("That was not a whole number.")
else:
    kind = "even" if number % 2 == 0 else "odd"
    print(f"{number} is {kind}.")
