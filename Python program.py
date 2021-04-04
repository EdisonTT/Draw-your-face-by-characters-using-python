from PIL import Image as im
image = im.open('jerry.png')
image = image.convert('L')
image.thumbnail((128,128))
width = image.width
height = image.height
total_pixel = width*height
#print(width)
#print(height)
pixel = list(image.getdata())
new_pixel = list(map(lambda a : round(a/255), pixel ))

for i in range(1,total_pixel):
    if new_pixel[i]==0:
        print('#',end='')
    if new_pixel[i]==1:
        print('.',end='')
    if i>2 and i%width==0:
        print()
