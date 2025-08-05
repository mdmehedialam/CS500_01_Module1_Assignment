# This program adds and subtracts two numbers
# The program is accurate for INT (numbers) data Types entered by user
# The program has an exception to handle other inputs (alphabets) than than numbers.
# The main function requests user for inputs
# After that it calls the add and subtract functions

def main():
    while True:
        try:
            x =int(input("Enter the first Number: "))
            y =int(input("Enter the Second Number: "))
        except ValueError:
            print("Input Error: Please Enter a Valid Number!!")
            continue
        else:
            sum = add(x, y)
            print(f"{x} add {y} is: {sum}")
            diff = subtract(x, y)
            print(f"{x} minus {y} is: {diff}")
            break
 
# The function takes two parameters and adds them  
def add(a, b):
    return (a + b)

# The function takes two parameters and subtracts the first from the second 
def subtract(a, b):
    return (a - b)

#The main function is invoked/called at this point
main ()