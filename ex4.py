try:
    a = int(input('Enter sales of 1 manager: '))
    b = int(input('Enter sales of 2 manager: '))
    c = int(input('Enter sales of 3 manager: '))

    Salary = 200

    if a > 1000:
        zp1 = Salary + a * 0.08
    else:
        if a < 500:
            zp1 = Salary + a * 0.03
        else:
            zp1 = Salary + a * 0.05
    if b > 1000:
            zp2 = Salary + b * 0.08
    else:
        if b < 500:
            zp2 = Salary + b * 0.03
        else:
            zp2 = Salary + b * 0.05
    if c > 1000:
            zp3 = Salary + c * 0.08
    else:
        if c < 500:
            zp3 = Salary + c * 0.03
        else:
            zp3 = Salary + c * 0.05
    if zp1 > zp2 and zp1 > zp3:
            print('The best in sales - 1 manager!!')
            zp1 += 200
    elif zp2 > zp1 and zp2 > zp3:
            print('The best in sales - 2 manager!')
            zp2 += 200
    elif zp3 > zp1 and zp3 > zp2:
                print('The best in sales - 3 manager!')
                zp3 +=200

    print('Salary of 1 manager ',zp1)
    print('Salary of 2 manager ',zp2)
    print('Salary of 3 manager ',zp3)

except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}') 