def celsius_to_fahrenheit(c):
    return [c * (9/5) + 32 if isinstance(c, int) else [i * (9/5) + 32 for i in c]]
    
print("Wartość w F: ", celsius_to_fahrenheit([1, 2, 54, 21]))

