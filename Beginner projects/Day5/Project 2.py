
# Area Calc
import math

def point_calc(height,width,cover):
    calc_1 = height * width 
    cans = math.ceil(calc_1/cover)
    print(f"You will need {cans} in paint cans.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
point_calc(height = test_h,width = test_w,cover = coverage)
