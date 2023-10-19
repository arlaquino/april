"""
    Program to convert Celsius to Fahrenheit
"""
def cel_to_fah(celsius):
    """ convert value given to fahrenheit"""
    fah = celsius * 9/5 + 32
    return fah


celsius = 25
fah = cel_to_fah(celsius)
print(f"{celsius} degrees is {fah} Fahrenheit")