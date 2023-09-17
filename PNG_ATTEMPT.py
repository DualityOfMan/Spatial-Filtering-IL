


Opng = open("pngwing.com.png","rb")
for i in range (8):
    print(int.from_bytes(Opng.read(1),'little'),end=" ")#header is correct
#this code is dependent on information from the 'PNG Chunk File Reader' linked in the Log, and online converters
Opng.read(8)#includes four seemingly unimportant bytes and the header name IHDR
pWidth = int.from_bytes(Opng.read(4),'big')
pHeight = int.from_bytes(Opng.read(4),'big')
