# Calculator

# Add
def add(n1,n2):
    return n1 + n2
# subtract
def sub(n1,n2):
    return n1 - n2
# multiply

def multiply(n1,n2):
    return n1 * n2

# division

def divide(n1,n2):
    return n1/n2

operations = {
"+" : add,
"-" : sub,
"*" : multiply,
"/" : divide
}

num1 = int(input("what is the first number?: "))

for symbol in operations:
    print(symbol)


operations_symbol = input("pick an operation from the line above")
num2 = int(input("what is the second number?: "))
calculation_function = operations[operations_symbol]
answer = calculation_function(num1,num2)

print(f"{num1} {operations_symbol} {num2} = {answer}")