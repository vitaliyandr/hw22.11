try:
    operators = {
        'MTS': 2.3,
        'Kyivstar': 1.5,
        'Lifecell': 4.5, 
        }

    cost = int(input("Enter the cost of the conversation: "))
    operator1 = input("Select the operator: ") 
    operator2 = input("Select the second operator: ")
    if operator1 == operator2:
        print("The cost of the conversation: ", cost)
    else:
        print("The cost of the conversation: ", cost * operators[operator1] + cost * operators[operator2])

except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')