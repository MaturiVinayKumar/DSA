def print_numbers(n):
    if n > 0:
        print_numbers(n - 1)  # Recursive call
        print(n)

# Example usage:
n = 5
print_numbers(n)
