# This program multiplies and divides two numbers
# The program is accurate for INT (numbers) data Types entered by user
# The program has an exception to handle other inputs (alphabets) than than numbers.
# Also, The program has an exception to handle division by zero error. 
# The main function requests user for inputs
# After that it calls the multiply and divide functions
def main():
    while True:
        try:
            x =int(input("Enter the first Number: "))
            y =int(input("Enter the Second Number: "))
        except ValueError:
            print("Input Error: Please Enter a Valid Number!!")
            continue
        else:
            product = multiply(x, y)
            print(f"{x} multiplied by {y} is: {product}")
            try:
                quotient = divide(x, y)
                print(f"{x} divided by {y} is: {quotient:.2f}")  #the float result is rounded to 2dp
            except ZeroDivisionError:
                print("Cannot divide by zero..!")
            break
# The function takes two parameters and multiples them  
def multiply(a, b):
    return (a * b)
# The function takes two parameters and divides them 
def divide(a, b):
        return (a / b)  
#The main function is invoked/called at this point
main ()