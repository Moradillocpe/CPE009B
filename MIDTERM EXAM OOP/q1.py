def main():
    class TemperatureConversion:
        def __init__(self, temp=1):
            self._temp = temp

    class CelsiusToFahrenheit(TemperatureConversion):
        def conversion(self):
            return (self._temp * 9) / 5 + 32

    class CelsiusToKelvin(TemperatureConversion):
        def conversion(self):
            return self._temp + 273.15

    # Added conversion classes
    class FahrenheitToCelsius(TemperatureConversion):
        def conversion(self):
            return (self._temp - 32) * 5 / 9

    class KelvinToCelsius(TemperatureConversion):
        def conversion(self):
            return self._temp - 273.15

    # Original Celsius conversions
    tempInCelsius = float(input("Enter the temperature in Celsius: "))
    convert = CelsiusToKelvin(tempInCelsius)
    print(str(convert.conversion()) + " Kelvin")
    convert = CelsiusToFahrenheit(tempInCelsius)
    print(str(convert.conversion()) + " Fahrenheit")

    # Additional user inputs and conversions
    tempInFahrenheit = float(input("\nEnter the temperature in Fahrenheit: "))
    convert = FahrenheitToCelsius(tempInFahrenheit)
    print(str(convert.conversion()) + " Celsius")

    tempInKelvin = float(input("Enter the temperature in Kelvin: "))
    convert = KelvinToCelsius(tempInKelvin)
    print(str(convert.conversion()) + " Celsius")

main()