#For reading from the .bmp file I will be using a lot of the code from hw2
a = open("Base.bmp","rb")
print(a.read(2)==b'BM')#is a bitmap
print(int.from_bytes(a.read(4),byteorder='little'))#file size is correct
a.read(8)#empty + mostly arbitrary
header_size = int.from_bytes(a.read(4),byteorder='little')
print(header_size)#this is a bmp3 file, so no alterations necessary from og hw code
width = int.from_bytes(a.read(4), byteorder = 'little')
height = int.from_bytes(a.read(4), byteorder = 'little')
print(width)
print(height)#checks out
a.read(2)#always equals 1
#copied from hw. gives how many bytes are read per pixel
bytesperpixel = int((int.from_bytes(a.read(2),byteorder='little'))/8)#=3
#changes from here on out: My idea is to do the following
#1- convert the bmp to grayscale (makes it a lot easier to work with
#1.5- if 3 struggles, create an image based on this grayscale to better understand issues
#2- create a 2d array giving the values of the grayscale
#3- use the simple filtering method as explained in the dynamsoft article
#4- if possible, learn about and apply the more complex methods
a.close()
a = open("Base.bmp", "rb")
f2 = open("GS_Color.bmp","wb")
f2.write(a.read(54))
image_grayscale = []
for i in range(height):
    curr_grayscale = []
    for j in range(width):
        gray_value =  .299*  int.from_bytes(a.read(1),byteorder='little')+.587* int.from_bytes(a.read(1),byteorder='little')+.114* int.from_bytes(a.read(1),byteorder='little')
        for k in range (bytesperpixel):
            f2.write(int(gray_value).to_bytes(1, byteorder= 'little'))
        curr_grayscale.append(int(gray_value))
    image_grayscale.append(curr_grayscale)
#le pain: doing spatial filtering
#note from past: have completed simple filtration, will move on to gaussian (alters weighting of image)
f2.close()
a.close()
f2 = open("GS_Color.bmp","rb")
final = open("Simple_Smooth.bmp", "wb")
final2 = open("Gaussian_Smooth.bmp", "wb")
header = f2.read(54)
final.write(header)
final2.write(header)
for i in range (height):
    for j in range (width):
        sum = 0
        G_sum = 0
        objs = 0
        G_objs = 0
        left = (j==0)
        right = (j== width-1)
        top = (i==height-1)
        bot = (i== 0)
        #kinda monotonous but it should work in theory
        sum = sum + (image_grayscale[i][j])*1
        objs = objs + 1
        G_sum = G_sum + (image_grayscale[i][j])*4
        G_objs = G_objs + 4
        if left != True:
            sum = sum + (image_grayscale[i][j-1])*1
            objs = objs + 1
            G_sum = G_sum + (image_grayscale[i][j-1])*2
            G_objs = G_objs + 2
            if top != True:
                sum = sum + image_grayscale[i + 1][j - 1]
                objs = objs + 1
                G_sum = G_sum + (image_grayscale[i+1][j-1])*1
                G_objs = G_objs + 1
            if bot != True:
                sum = sum + image_grayscale[i - 1][j - 1]
                objs = objs + 1
                G_sum = G_sum + (image_grayscale[i-1][j-1])*1
                G_objs = G_objs + 1
        if right != True:
            sum = sum + (image_grayscale[i][j+1])*1
            objs = objs + 1
            G_sum = G_sum + (image_grayscale[i][j+1])*2
            G_objs = G_objs + 2
            if top != True:
                sum = sum + image_grayscale[i + 1][j + 1]
                objs = objs + 1
                G_sum = G_sum + (image_grayscale[i+1][j+1])*1
                G_objs = G_objs + 1
            if bot != True:
                sum = sum + image_grayscale[i - 1][j + 1]
                objs = objs + 1
                G_sum = G_sum + (image_grayscale[i-1][j+1])*1
                G_objs = G_objs + 1
        if top != True:
            sum = sum + (image_grayscale[i + 1][j])*1
            objs = objs + 1
            G_sum = G_sum + (image_grayscale[i+1][j])*2
            G_objs = G_objs + 2
        if bot != True:
            sum = sum + (image_grayscale[i - 1][j])*1
            objs = objs + 1
            G_sum = G_sum + (image_grayscale[i-1][j])*2
            G_objs = G_objs + 2
        average = (int)(sum/objs)
        G_av = (int)(G_sum/G_objs)
        for a in range (3):
            final.write(average.to_bytes(1,byteorder='little'))
            final2.write(G_av.to_bytes(1,byteorder='little'))



