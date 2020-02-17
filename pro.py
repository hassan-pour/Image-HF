from PIL import Image
img = Image.open('1.jpg')
print('Welcome to PES v.2.2 ----enter---- blur or black and withe or out of color or sym!')
fi=input('HI.please enter the job you want! or enter mod1 or mod2:')
weight = img.size[0]
height = img.size[1]
red=0
green=0
blue=0
#AI system put pix;
def ai (x,y):
    for x2 in range(x-2,x+3):
        for y2 in range(x-2,x+3):
            r,g,b=tr+tb+tg
            if tr==mo and tg==mo and tb==mo:
                a=0
    if a==0:
        return(tr+tb+tg)
#v.1.0
if fi=='blur':
    x1=int(input())
    y1=int(input())
    x2=int(input())
    y2=int(input())
    for x in range(1,weight-1):
        for y in range(1,height-1):
            if x<x1 or x>x2 and y<y1 or y<y2:
                r, g, b = img.getpixel((x+1, y+1))
                red=red+r
                blue=blue+b
                green=green+g
                r, g, b = img.getpixel((x-1, y-1))
                red=red+r
                blue=blue+b
                green=green+g
                r, g, b = img.getpixel((x+1, y-1))
                red=red+r
                blue=blue+b
                green=green+g
                r, g, b = img.getpixel((x-1, y+1))
                red=red+r
                blue=blue+b
                green=green+g
                r, g, b = img.getpixel((x, y+1))
                red=red+r
                blue=blue+b
                green=green+g
                r, g, b = img.getpixel((x, y-1))
                red=red+r
                blue=blue+b
                green=green+g
                r, g, b = img.getpixel((x-1, y))
                red=red+r
                blue=blue+b
                green=green+g
                r, g, b = img.getpixel((x+1, y))
                red=red+r
                blue=blue+b
                green=green+g
                img.putpixel((x, y), (red//8, green//8, blue//8))
                red=0
                green=0
                blue=0
#v.2.0
if fi=='black and withe':
    for x in range(weight):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            a=r+g+b//3
            if a>125:
                img.putpixel((x, y), (255, 255, 255))
            elif a<=125:
                img.putpixel((x, y), (0, 0, 0))
if fi=='out of color':
    for x in range(weight):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            a=r+g+b//3
            img.putpixel((x, y), (a, a, a))
if fi=='sym':
    for x in range(weight):
        l = []
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            l.append((r, g, b))
        img_pixels.append(l)
    for x in range(weight-1,-1,-1):
        for y in range(height):
            img.putpixel((x*-1, y), (img_pixels[x][y][0],img_pixels[x][y][1] ,img_pixels[x][y][2] ))
if fi=='mod1':
    x52=int(input('x:'))
    y52=int(input('y:'))
    r, g, b = img.getpixel((x52, y52))
    red=r
    blue=b
    green=g
    for x in range(weight):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            if r-10<red<r+10 and g-10<green<g+10 and b-10<blue<b+10:
                img.putpixel((x, y), (255, 0, 0))
if fi=='mod2':
    red=int(input('r:'))
    green=int(input('g:'))
    blue=int(input('b:'))
    for x in range(weight):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            if red-50<red<red+50 and green-50<g<green+50 and blue-50<b<blue+50:
                img.putpixel((x, y), (255, 255, 255))

#v.2.1
if fi=='new1':
    for x in range(weight):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            if 210>r<=230:
                img.putpixel((x, y), (0, 0, 255))
if fi=='new2':
    for x in range(weight):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            if 210>r<=230:
                img.putpixel((x, y), (0, 255, 0))
if fi=='new3':
    for x in range(weight):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            if 210>r<=230:
                img.putpixel((x, y), (255, 0, 0))
if fi=='new4':
    for x in range(weight):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            if 210>g<=230:
                img.putpixel((x, y), (0, 0, 255))
if fi=='new5':
    for x in range(weight):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            if 210>g<=230:
                img.putpixel((x, y), (0, 255, 0))
if fi=='new6':
    for x in range(weight):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            if 210>g<=230:
                img.putpixel((x, y), (255, 0, 0))
if fi=='new7':
    for x in range(weight):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            if 210>b<=230:
                img.putpixel((x, y), (0, 0, 255))
if fi=='new8':
    for x in range(weight):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            if 210>b<=230:
                img.putpixel((x, y), (0, 255, 0))
if fi=='new9':
    for x in range(weight):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            if 210>b<=230:
                img.putpixel((x, y), (255, 0, 0))
#v.2.2
if fi=='new10':
    for x in range(weight):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            if 210>r<=230:
                img.putpixel((x, y), (0, 0, 0))
if fi=='new11':
    for x in range(weight):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            if 210>g<=230:
                img.putpixel((x, y), (0, 0, 0))
if fi=='new12':
    for x in range(weight):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            if 210>b<=230:
                img.putpixel((x, y), (0, 0, 0))
#v.2.5
#new filters
if fi=='negative':
    from PIL import ImageFilter
    for i in range(weight):
        for j in range(height):
            r,g,b = img.getpixel((i,j))
            redPixel    = 255 - r
            greenPixel  = 255 - g
            bluePixel   = 255 - b
            img.putpixel((i,j),(redPixel, greenPixel, bluePixel))

# v.2.6
if fi == "Red&Black":
    for x in range(weight):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            a=r+g+b//3
            if r > g and r > b and (r * 2) - (g + b) > 150:
                img.putpixel((x, y), (255, 0, 0))
            else :
                if a > 125:
                    img.putpixel((x, y), (255, 255, 255))

                else :
                    img.putpixel((x, y), (0, 0, 0))
#crop v.1.5
if fi=='crop':
    x1=int(input())
    y1=int(input())
    x2=int(input())
    y2=int(input())
    cropped=img.crop((x1,y1,x2,y2))
#AI system v.1.1
if fi=='use face ID':
    for x in range(weight):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            a=r+g+b//3
            if a-20<220<a+20:
                img.putpixel((x, y), (255, 255, 0))
            if r-20<180<r+20:
                img.putpixel((x, y), (0, 255, 255))
            if g-20<180<g+20:
                img.putpixel((x, y), (255, 0, 255))
            if r>g and r>b and r>220:
                img.putpixel((x, y), (255, 0, 255))
            if r > g and r > b and (r * 2) - (g + b) > 150:
                img.putpixel((x, y), (255, 0, 0))
#!در حال تعمير
'''if fi=='use face ID2':
    imgg = Image.open('3.jpg')
    for x in range(weight):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            if r==255 and b=255:
                g1=g1+1
    for x in range(weight):
        for y in range(height):
            r, g, b = imgg.getpixel((x, y))
            if r==255 and b=255:
                a=a+1'''
img.save('2.jpg')
