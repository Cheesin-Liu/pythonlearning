#!/usr/bin/env python3
fahrenheit = 0
print("celsius_from_fahrenheit")
while fahrenheit <=250:
    celsius = (fahrenheit - 32) / 1.8
    print("Fahrenheit {:5d} --- Celsius  {:7.2f}".format(fahrenheit , celsius))
    fahrenheit = fahrenheit + 25
