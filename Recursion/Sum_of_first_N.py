sum=0
def print_numbers(n):
    global sum
    if n > 0:
        print_numbers(n - 1)  # Recursive call
        sum+=n 
    return sum

# Example usage:
n = 5
res=print_numbers(n)
print(res)
