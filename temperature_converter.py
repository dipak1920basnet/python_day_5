def main():
    temperature = 32
    celsius_to_fahrenheits = celsius_to_fahrenheit(temperature)
    fahrenheit_to_celsiuss = fahrenheit_to_celsius(temperature)
    print(f"{temperature}°C -> {celsius_to_fahrenheits}°F")
    print(f"{temperature}°F -> {fahrenheit_to_celsiuss}°F")
    
def celsius_to_fahrenheit(temp):
    return ( temp * (9/5) ) + 32

def fahrenheit_to_celsius(temp):
    return ( temp - 32) * (5/9)

if __name__ == "__main__":
    main()