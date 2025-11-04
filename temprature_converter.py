class TempratureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9
    
    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15
    
    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15
    
    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit):
        celsius = TempratureConverter.fahrenheit_to_celsius(fahrenheit)
        return TempratureConverter.celsius_to_kelvin(celsius)
    
if __name__ == "__main__":
    f= TempratureConverter.celsius_to_fahrenheit(100)
    c= TempratureConverter.fahrenheit_to_celsius(100)
    
    print(f"100 C to fahrenheit: {f:.2f}")
    print(f"100 F to Celsius: {c:.2f}")
    