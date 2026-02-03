# program to generate a list of odd numbers from 1 to n, where n = 30 

for num in range(1, 31):
    print(num/2, int(num/2))
    # checks if dividing the number by 2 leaves a remainder, if it does the number is odd
    if num / 2 != int(num / 2):
        print(num)



