l= float(input('Please enter the length of wall in meter'))
w = float(input('Please enter the width of wall in meter'))
c = 5
import math

def Area_of_wall(length,width,cover):
    Area = length * width
    num_of_cans = math.ceil(Area / cover)
    print(f'you will required {num_of_cans} to paint' )
Area_of_wall(l,w,c)
