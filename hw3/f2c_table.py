# program that converts Fahrenheit to Celsius, 
# then prints a table with F in the first column and C in the second column

# for loop generates list of F vals from 0-100 in steps of 10
for temp_f in range(0, 101, 10):
    
    # below is the conversion equation from F to C
    temp_c = (temp_f - 32) * 5/9
    print(f"{temp_f} {temp_c}") 