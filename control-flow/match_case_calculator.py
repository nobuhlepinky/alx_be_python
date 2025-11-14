num1_text = input("Enter the first number: ")
num1 = float(num1_text)

num2_text = input("Enter the second number: ")
num2 = float(num2_text)

operation = input("Choose the operation (+, -, *, /): ")

result = None

match operation:
    case '+':
        
        result = num1 + num2
        print(f"The result of addition is: {result}")

    case '-':
        
        result = num1 - num2
        print(f"The result of subtraction is: {result}")

    case '*':
        
        result = num1 * num2
        print(f"The result of multiplication is: {result}")

    case '/':
        
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result of division is: {result}")

   

