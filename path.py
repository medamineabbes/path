import pygame
def puis(a):
    b=-1
    for i in range(a):
        b*=b
    return b;
pygame.init()
Surface=pygame.display.set_mode((300,300))
Surface.fill((255,255,255))
run=True
for i in range(1,30):
    pygame.draw.rect(Surface,(0,0,0),[i*10,0,1,300],0)
    pygame.draw.rect(Surface,(0,0,0),[0,i*10,300,1],0)
i=0
t=True
while run:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            run=False
        if e.type == pygame.MOUSEBUTTONDOWN and t:
            (mx,my)=pygame.mouse.get_pos()
            mx=mx-mx%10
            my=my-my%10
            i+=1
            if i==1:
                xd=mx
                yd=my
                color=(200,0,0)
            else :
                color=(0,0,200)
                xa=mx
                ya=my
            if i==2:
                t=False
            pygame.draw.rect(Surface,color,[mx,my,10,10],0)
    pygame.display.update()
