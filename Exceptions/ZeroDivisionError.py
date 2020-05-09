
try:
    a = eval(input('Enter First number: '))
    b = eval(input('Enter Second number: '))
    print(a / b)
except ZeroDivisionError as e:
    print('Cant Divide By 0, ', e)
except NameError as e:
    print(e)
except ValueError as e:
    print('Invalid Input, ', e)
except Exception as e:
    print(e)
finally:
    print('Bye...')
