print("Celsius | Fahrenheit")
print("--------------------")

for celsius in range(0, 41):
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius:7} | {fahrenheit:.2f}")