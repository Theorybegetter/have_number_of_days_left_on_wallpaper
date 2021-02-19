import datetime
import ctypes
from PIL import Image, ImageDraw, ImageFont

x = str(datetime.datetime.now())
x=x[:10]
g=int(x[8:10]) #current day
h=int(x[5:7])  #current month
i=int(x[:4])    #current year

j=23  #any targeted day 
k=5    #any targeted month 
l=2028   #any targeted year 

class Date:
    def __init__(self, d, m, y):
        self.d = d
        self.m = m
        self.y = y
 
 

monthDays = [31, 28, 31, 30, 31, 30,
             31, 31, 30, 31, 30, 31]
  
def countLeapYears(d):
 
    years = d.y
 
    
    if (d.m <= 2):
        years -= 1
 
    
    ans = int(years / 4)
    ans -= int(years / 100)
    ans += int(years / 400)
    return ans
 

 
def getDifference(dt1, dt2):
 

    n1 = dt1.y * 365 + dt1.d
 

    for i in range(0, dt1.m - 1):
        n1 += monthDays[i]
 

    n1 += countLeapYears(dt1)
 

    n2 = dt2.y * 365 + dt2.d
    for i in range(0, dt2.m - 1):
        n2 += monthDays[i]
    n2 += countLeapYears(dt2)
 

    return (n2 - n1)
 
 
dt1 = Date(g, h, i)
dt2 = Date(j, k ,l)
 

img = Image.new('RGB', (1000, 700), color = (255, 255, 255))
d = ImageDraw.Draw(img)
d.text((500,350), str(getDifference(dt1, dt2))+"days to go", fill=(0,0,0),)
 
img.save('days_left.png')

#the image will be saved in the directory this file is on

ctypes.windll.user32.SystemParametersInfoW(20,0,"Absolute Path of The image",0)
#make sure there's a extra '\' after u enter the respective directory for python to read ur code
#example 
#wrong "C:\Users\Frail\Desktop\Days left\day_left.png"
#correct "C:\\Users\Frail\Desktop\Days left\day_left.png"