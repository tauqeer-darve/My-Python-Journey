import art

def add(n1, n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1 * n2

def div(n1,n2):
    return n1 / n2

calc_dict = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

def calculator():
    print(art.logo)
    carry_result = True
    num1 = float(input("Enter the 1st number: "))
    while carry_result:
        for keys in calc_dict:
            print(keys)
        select_op = input("Enter the operation you want to perform: ")
        num2 = float(input("Enter the second number: "))
        calc = calc_dict[select_op](num1,num2)
        result = round(calc,2)
        print(f"{num1} {select_op} {num2} = {result}")
        choice = input(f"Do you want to continue the calculation with {result} or restart a new calculation?\n('y' to continue, 'n' to restart): ")
        if choice == "y":
            num1 = result
        else:
            carry_result = False
            print("\n" * 20)
            calculator()

calculator()
