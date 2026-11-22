"""Convert Celsius to Fahrenheit."""
try:
    celsius = float(input("Temperature in Celsius: "))
except ValueError:
    print("Please enter a valid number.")
else:
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius:g}°C = {fahrenheit:.1f}°F")
