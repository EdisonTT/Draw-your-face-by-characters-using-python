# Draw your face by characters using Python
This is a simple python program which helps to draw your face using characters. 

Before starting, install python module ```pillow```. For guidelines visit [here](https://pillow.readthedocs.io/en/latest/installation.html).

The program is given below.
```python3
from PIL import Image as im
image = im.open('location of the image')
image = image.convert('L')
image.thumbnail((128,128))
width = image.width
height = image.height
total_pixle = width*height
#print(width)
#print(height)
pixel = list(image.getdata())
new_pixel = list(map(lambda a : round(a/255), pixle ))

for i in range(1,total_pixel):
    if new_pixel[i]==0:
        print('#',end='')
    if new_pixel[i]==1:
        print('.',end='')
    if i>2 and i%width==0:
        print()

```
The method ```im.open()``` will open the image and treat it as an object. The argument is the location of the image. If both the python program and the image file is in the same folder, the name of the image is enough. The method ```image.convert('L')``` will convert the image into grey style and ```image.thumbnail()``` will resize the image. It accepts a tuple containing two elements, one for width and the other for height.<br/>
A ```128 X 128``` image file has ```16384``` bytes of data (not that the image is in grey style). Each byte represents the intensity of white colour at a point. A zero represents a black colour and ```255``` represents white. ```image.data()``` collects these data of the image and stored in  ```pixel```, a list. Then, each byte is mapped to zero or one. It is stored in the list ```new_pixel```. Then for every zero in ```new_pixel```, a dotand for every ```1```, ```#``` is printed.<\br>
For example, consider the given input image file.
![abc](https://user-images.githubusercontent.com/62181643/113512623-19bcf380-9583-11eb-9f6a-dddfecc248aa.png)
The output is shown below.
![demo](https://user-images.githubusercontent.com/62181643/113512643-293c3c80-9583-11eb-8426-7cf1c71134f9.JPG)
