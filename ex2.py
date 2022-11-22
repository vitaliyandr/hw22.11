try:
    num = int(input("Number: "))
    st = int(input("Degree of: "))

    if st > 7 or st < 0:
        print("Degree of number must be 1-7")
    else:
        print(num**st)
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')
