# minutes as input to hours and remaining minutes - take min as 135

min = int(input())

hours = min//60
rmin = min%60

print(f"Hours: {hours} and remaining minutes: {rmin}")