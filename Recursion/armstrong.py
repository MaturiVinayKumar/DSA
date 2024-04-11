def is_armstrong(n):
    num_str = str(n)
    num_len = len(num_str)
    return n == sum(int(digit) ** num_len for digit in num_str)

# Test the function
print(is_armstrong(153))
print(is_armstrong(370))
print(is_armstrong(371))
print(is_armstrong(407))
