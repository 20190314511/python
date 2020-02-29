#Drawing lines project
import sys
import pygame
from pygame.locals import *
import go_funcs

# python 使用类创建结构体
class GoClass(object):
    class Struct(object):
        def __init__(self):
            self.win_lefttop = 20,30
            self.grid_lefttop = 50,50
            self.grid_size = 36,36
            self.spot_radious = 3
            self.line_color = 0,0,0
            self.line_width = 1
            self.bkcolor = 192,192,160
            self.grid_count = 18
            self.win_title = "五子棋"
            self.turn = 1
            self.curpos = (9,9)
            self.pieces = {}
            self.histroy = []
            self.pygame = []
            self.screen = []
    def make_struct(self):
        return self.Struct()
 
go = GoClass()
mygo = go.make_struct()
go_funcs.set_windows_position(mygo.win_lefttop[0],mygo.win_lefttop[1])
pygame.init()

screen = pygame.display.set_mode( ( mygo.grid_size[0]*mygo.grid_count + mygo.grid_lefttop[0]*2,
mygo.grid_size[0]*mygo.grid_count + mygo.grid_lefttop[1]*2) )
mygo.pygame.append(pygame)
mygo.screen.append(screen)

screen.fill(mygo.bkcolor)
pygame.display.set_caption(mygo.win_title)

go_funcs.drawbk(mygo)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN, MOUSEBUTTONDOWN):
            if (event.type==QUIT):
                pygame.quit()
            else:
                if event.type==MOUSEBUTTONDOWN:
                    if event.button==1:
                        cpos = pygame.mouse.get_pos()
                        x = round((cpos[0] - mygo.grid_lefttop[0])/mygo.grid_size[0])
                        y = round((cpos[1] - mygo.grid_lefttop[1])/mygo.grid_size[1])
                        key = str((x,y))
                        if (x in range(19) and y in range(19)):
                            if mygo.pieces.get( key, -1 )< 0:
                                mygo.histroy.append((x,y, mygo.turn))
                                mygo.pieces[key]=mygo.turn
                                go_funcs.draw_piece( mygo, x, y, mygo.turn)
                                mygo.curpos = (x,y)
                                mygo.turn = (mygo.turn+1)%2
                                pygame.display.update()
                    else:
                        if len(mygo.histroy)>0:
                            last_step = mygo.histroy.pop()
                            x = last_step[0]
                            y = last_step[1]
                            mygo.turn = last_step[2]
                            go_funcs.drop_piece( mygo, x, y)
                            mygo.pieces[str((x,y))]=-2
                            pygame.display.update()
                            if (len(mygo.histroy)>0):
                                last_step = mygo.histroy[-1]
                                mygo.curpos = ( last_step[0], last_step[1])
    #draw the line


