def perform_operation(num1, num2, operation):
    op = operation.lower()

    if op == 'add':
        return num1 + num2
    
    elif op == 'subtract':
        return num1 - num2
    
    elif op == 'multiply':
        return num1 * num2
    elif op == 'divide':
        
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2