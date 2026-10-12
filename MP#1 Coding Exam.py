"""
<Croft, Malakai>
MP1_Exam
"""
input("C=(F-32)X 5/9")

def fahrenheit_to_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * 5 / 9
    return celcius


# example usage:
temp_f = 68
temp_c = fahrenheit_to_celcius(temp_f)
print(f"{temp_f}°F is equal to {temp_c:.2f}°C")

# Input temperature in Celsius
celsius = 25.567

# Convert to Fahrenheit: (C * 9/5) + 32
fahrenheit = (celsius * 9 / 5) + 32

# Print the result rounded to one decimal place
print(f"The temperature is {fahrenheit:.1f}°F")

# Input temperature in Fahrenheit
fahrenheit = 78.34

# Convert to Celsius: (F - 32) * 5/9
celsius = (fahrenheit - 32) * 5 / 9

# Print the result rounded to one decimal place
print(f"The temperature is {celsius:.1f}°C")

# Assuming 'temperature' is your converted temperature variable
if temperature < 0:
    print("Freezing Alert!")
elif temperature > 35:
    print("Heat Warning!")
else:
    print("Normal Temperature")


    def check_temperature(fahrenheit):
        celsius = (fahrenheit - 32) / 1.8
        rounded_celsius = round(celsius, 1)

        if rounded_celsius >= 37.8:
            print(f"{rounded_celsius} degrees - Heat Warning")
        else:
            print(f"{rounded_celsius} degrees - Normal")

