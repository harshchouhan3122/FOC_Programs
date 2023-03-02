# try and except

# Celcius to Fahrenheit
cel = float(input("Enter the Temperature in Degree Celcius : "))
try:
    fht = (cel*(9/5)) + 32
    print("Temperature in Fahrenheit is : ", fht)
except:
    print("Enter the numbers only!")
