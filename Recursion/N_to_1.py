def print_numbers(n):
    if n > 0:
        print(n)
        print_numbers(n - 1)  # Recursive call
        

# Example usage:
n = 5
print_numbers(n)
