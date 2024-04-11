res=1
def fact(n):
    global res
    if n>1:
        res = n*fact(n-1) 
    return res

n = 10
factorial=fact(n)
print(factorial)
