import read
import math #import to get pi value

r = read.Read(float, 'Radius')

area = round(math.pi * r ** 2, 2) #calculating the area & rounding off to 2 decimal values
per = round(2 * math.pi * r, 2) #calculating the circumference

print('Area of the circle is', area)
print('Perimeter of the circle is', per)
