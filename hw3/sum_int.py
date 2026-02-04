# program compares two methods of summing from 1 to n (n=100) 
# using a python program and the formula n(n+1)/2

n = 100 
sum_py = 0

# loop metod 
for i in range(1, n+1):
    sum_py += i

# equation method 
sum_eq = n * (n + 1) / 2

print(sum_py)
print(sum_eq)

