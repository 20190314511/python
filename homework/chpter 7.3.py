from PIL import Image

unicode_char = list("")
ascii_char = list('"$%_&WM#*oahkbdpqwmZO0QEESDLCJUYXzcvunxrjft/\|()1{}[]?-/+@<>i!;:,\^`.')
def get_char( r,b,g,alpha = 256 ):
    if alpha == 0:
        return ' '
    gray = int( 0.2126*r + 0.7152*g+ 0.0722*b)
    unit = 256/len(ascii_char)

    return ascii_char[int(gray//unit)]

def main( filename ):
    im = Image.open( filename )
    W,H = 100,60
    im = im.resize((W,H))

    txt = ''
    for i in range(H):
        for j in range(W):
            txt += get_char( *im.getpixel((j,i)) )
        txt += "\n"
    fo = open(filename+".txt", "w")
    fo.write(txt)
    fo.close()

main( "resources/2.bmp")

