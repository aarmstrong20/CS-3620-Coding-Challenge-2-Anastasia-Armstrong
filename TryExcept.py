try:
    a = 10
    b =0
    print(a/b)
except ZeroDivisionError:
    print("You can't divide by zero")
finally:
    print("Goodbye")