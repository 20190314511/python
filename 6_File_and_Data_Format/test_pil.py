from PIL import Image

im = Image.open( "resources/2.bmp","r" )
orgsize = im.size

im2 = im.resize((int(orgsize[0]/2), int(orgsize[1]/2)) )
im2.save( "resources/2.jpg")
