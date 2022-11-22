try:
    a = int(input())

    if 1 <= a <= 100:
        if not a%3 and not a%5:
            print("Fizz Buzz")
        elif not a%3:
            print("Fizz")
        elif not a%5:
            print("Buzz")
        else:
            print(a)
    else:
        print("Error, type number 1-100")

except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')
