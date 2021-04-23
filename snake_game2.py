import pygame as pg
import random
pg.init()
win_w,win_h=900,600
win=pg.display.set_mode((win_w,win_h))
pg.display.set_caption('snake Game')
x,y,s_h,s_w=win_w/2,win_h/2,20,10
apx,apy=random.randint(0,win_w-10),random.randint(0,win_h-10)
ap_w,ap_h=10,10
run=True
esc_condition=True
ap_ct=0
direction,temp_direction='',''
red,green,blue=(255,0,0),(0,255,0),(0,0,255)
font=pg.font.SysFont(None,25)
snake_list=[1,0,1]   #defines the structure of the snake
bend_x,bend_y=0,0

##    =================================================================

'''def esc_msg(text,color):
    msg=font.render(text,True,color)
    win.blit(msg,(win_w/2,win_h/2))
    pg.display.update()'''





##    =================================================================

while run:
    pg.time.delay(5)
    for event in pg.event.get():
       # print(event)
        if event.type==pg.QUIT:
            run=False
            
    key=pg.key.get_pressed()
    ''' while not esc_condition:
        key=pg.key.get_pressed()
        win.fill((255,255,0))
        esc_msg('press e to exit',(0,0,0))
        print('##')
        if key[pg.K_UP]:
            #run=False
            esc_condition=True'''
        
    
    if key[pg.K_LEFT]:
        x-=1
        direction='left'
        
        #s_h,s_w=10,20
    elif key[pg.K_UP]:
        y-=1
        direction='up'
       # s_h,s_w=20,10
    elif key[pg.K_DOWN]:
        y+=1
        direction='down'
        #s_h,s_w=20,10        
    elif key[pg.K_RIGHT]:
        x+=1
        direction='right'
        #s_h,s_w=10,20

    ''' elif key[pg.K_ESCAPE]:
        esc_condition=False
        
        pg.display.update()
        '''
   
        

    if x<0:
        x=win_w
    elif x>win_w:
        x=0
    elif y<0:
        y=win_h
    elif y>win_h:
        y=0

    if (apx<=x<apx+ap_w or apx<x+s_w<apx+ap_w) and (apy<=y<apy+ap_h or apy<y+s_h/2<apy+ap_h):
        
        ap_ct+=1
        
       # snake_list.insert(-1,0)
        apx,apy=random.randint(0,win_w-10),random.randint(0,win_h-10)
    s_h=s_h*(1+ap_ct)


    win.fill((255,255,255))

    if direction!=temp_direction:
        bend_x,bend_y=x,y
        temp_direction=direction

        
    if bend_y-y==0 :
        horizontal_length=x-bend_x
        if horizontal_length!=s_h:
            pg.draw.rect(win,(0,255,0),(x,y,horizontal_length,s_w))
            pg.draw.rect(win,(0,255,0),(bend_x,bend_y,s_w,s_h-(x-bend_x)))
        else:
            pg.draw.rect(win,(0,255,0),(x,y,s_h,s_w))
    elif bend_x-x==0 :
        pg.draw.rect(win,(0,255,0),(x,y,s_h,s_w))
        ''' pg.draw.rect(win,(0,255,0),(x,y,s_w,y-bend_y))
       pg.draw.rect(win,(0,255,0),(bend_x,bend_y,s_w-(y-bend_y),s_h))
       '''
    ''' for i in range(len(snake_list)):
        if snake_list[i]==1:
            color=blue
        else:
            color=green
        pg.draw.rect(win,color,(x,y+(i*s_h),s_w,s_h))
        pg.draw.rect(win,(0,0,0),(x-1,y+(i*s_h)-1,s_w+1,s_h+1),1)'''
#    pg.draw.rect(win,(0,255,0),(x,y,s_w,s_h*(ap_ct+1)))  
    pg.draw.rect(win,(255,0,0),(apx,apy,ap_w,ap_h))
    pg.display.update()


pg.quit()
