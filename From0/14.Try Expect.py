try:
    #value = 10 / 0
    number = int(input("Please enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except:
    print("Invalid Input")