import math
def calculate_distance(x1,y1,x2,y2):
    distance= math.sqrt((x2-x1)**2+(y2-y1)**2)
    return distance
x_ram=int(input('Enter the x corrdinate of ram:'))
y_ram=int(input('Enter the y coordinate of ram:'))
x_sita=int(input('Enter the x coordinate of sita:'))
y_sita=int(input('Enter the y coordinate of sita:'))
distance=calculate_distance(x_ram,y_ram,x_sita,y_sita)
print('The distance between ram and sita',distance)
