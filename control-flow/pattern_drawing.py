size_input = input("Enter the size of the pattern: ")
size = int(size_input)

row_counter = 0

while row_counter < size:
    for column_counter in range(size):
        print("*", end="")

    print()  
    row_counter += 1