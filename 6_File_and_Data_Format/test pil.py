from PIL import Image

im = Image.open( "resources/2.bmp","r" )
orgsize = im.size

# 演示resize
im2 = im.resize((int(orgsize[0]/2), int(orgsize[1]/2)), 3 )
im2.save( "resources/2_resize.jpg")

# 演示旋转
im3 = im2.rotate(45)
im3.save("resources/2_rotate.jpg")