n = input("Please enter a number for your fib series: ")
n = int(n)
x = [0,1]
for i in range(2,n):
    if i <= n:
        x.append(x[i-1]+x[i-2])
print(x)


    