def drawbk( mygo):
    pg = mygo.pygame[0]
    screen = mygo.screen[0]
    x0 = mygo.grid_lefttop[0]
    y0 = mygo.grid_lefttop[1]
    width = mygo.grid_size[0]*mygo.grid_count

    for i in range(19):
        pg.draw.line(screen, mygo.line_color, 
            (x0+i*mygo.grid_size[0],y0), (x0+i*mygo.grid_size[0],y0+width), mygo.line_width)
        pg.draw.line(screen, mygo.line_color, 
            (x0,y0+i*mygo.grid_size[0]), (x0+width, y0+i*mygo.grid_size[0]), mygo.line_width)

    for j in range(5):
        for k in range(5):
            if (k==0 or j==0 or k==4 or j==4 or (k==2 and j==2) ):
                pg.draw.circle(screen, mygo.line_color, 
                    (x0+mygo.grid_size[0]*(j+1)*3, y0+mygo.grid_size[0]*3*(k+1)), mygo.spot_radious, 0)

def draw_piece( mygo, x, y, borw):
    pg = mygo.pygame[0]
    screen = mygo.screen[0]
    color = ((255,255,255),(0,0,0))
    x0 = mygo.grid_lefttop[0] + mygo.grid_size[0]* x
    y0 = mygo.grid_lefttop[1] + mygo.grid_size[1]* y
    pg.draw.circle(screen, color[borw], (x0,y0) , int(mygo.grid_size[0]/2-5), 0)

def drop_piece( mygo, x, y ):
    pg = mygo.pygame[0]
    screen = mygo.screen[0]
    x0 = mygo.grid_lefttop[0] + mygo.grid_size[0]* x
    y0 = mygo.grid_lefttop[1] + mygo.grid_size[1]* y
    bias = int(mygo.grid_size[0]/2)
    pg.draw.circle(screen, mygo.bkcolor, (x0,y0) , int(mygo.grid_size[0]/2-5), 0)
    pg.draw.line( screen, mygo.line_color, 
        (x0-bias, y0),(x0+bias, y0), mygo.line_width)
    pg.draw.line( screen, mygo.line_color, 
        (x0, y0-bias),(x0, y0+bias), mygo.line_width)

def set_windows_position(x, y):
    import os
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
    