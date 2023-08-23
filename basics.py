# code to convert degrees to radians
import math
from datetime import datetime
from time import time, ctime, gmtime

degrees = input("input degrees to convert: ")

a = int(degrees)

output= a * math.pi/180

print(f"{degrees} degrees is equal to {output} radians")

code to calculate surface area and volume

radius = input("input radius to calculate: ")

r = int(radius)
pi = math.pi

surface_area = 4* pi* r * r
volume = 4/ 3*pi*r*r*r 
print(f'A sphere with the radius, {radius} meters has a surface area of {surface_area} meters squared and a volume of {volume} meters cubed')
 

# to tell the time
now= ctime()

x = now.split(" ")
y = x[3].split(":")

print(f'The time is {y[0]} hours, {y[1]} minutes and {y[2]} seconds UCT')

 # to split a sentence into words

 
sentence = input('Type a sentence here:')
output = sentence.split() 
print(output)
join words into a sentence1

words = ['That', 'is', 'a', 'good', 'thing']

output1 = ' '.join(words)
output2 = ""

for i in words:
    output2 += i
    output2 += " "

print(output1)
print(output2)











