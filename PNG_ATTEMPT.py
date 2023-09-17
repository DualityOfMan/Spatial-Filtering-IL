


Opng = open("pngwing.com.png","rb")
Opng.read(8)#header
#this code is dependent on information from the 'PNG Chunk File Reader' linked in the Log, and online converters
#the following values are known:
#Color type: RGBA with 8 bits per channel (theoretically 32 bits per pixel)
Opng.read(8)#includes four seemingly unimportant bytes and the header name IHDR
pWidth = int.from_bytes(Opng.read(4),'big')
print(pWidth)
pHeight = int.from_bytes(Opng.read(4),'big')

