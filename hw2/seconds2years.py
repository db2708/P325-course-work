min = 60 # sec
hour = 60 # min
day = 24 # hour
year = 365.25 # day

sec_per_year = min * hour * day * year

def seconds_to_years(time):
    n_years = time / sec_per_year
    return print(f"{time} seconds is equivalent to {n_years} years.")
 
seconds_to_years(1*10**9)
