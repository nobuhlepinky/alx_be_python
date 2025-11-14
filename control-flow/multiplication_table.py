number_input = input("Enter a number to see its multiplication table: ")
number = int(number_input)

for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")