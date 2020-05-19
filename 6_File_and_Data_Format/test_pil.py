from PIL import Image
import os

orgpic = "resources/2.jpg"
im = Image.open( orgpic,"r" )
orgsize = im.size

im2 = im.resize((int(orgsize[0]/2), int(orgsize[1]/2)) )

cprpic = "resources/2 compress.jpg"
im2.save( cprpic )

print( os.stat(orgpic).st_size, os.stat(cprpic).st_size)