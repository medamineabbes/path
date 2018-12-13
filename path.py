import pygame
def distance(a,b,c,d):
     return math.sqrt((a-b)*(a-b)+(c-d)*(c-d))
red=(150,0,0)
green=(0,150,0)
t0=[5]
t1=[5]
ln0=[]
ln1=[]
xf=0
yf=0
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
                xf=mx
                yf=my
                pygame.draw.rect(Surface,(255,0,0),[mx,my,10,10],0)
            elif i==2 :
                pygame.draw.rect(Surface,(0,0,255),[mx,my,10,10],0)
                xa=mx
                ya=my
            else:
                t0.append(mx)
                t1.append(my)
                pygame.draw.rect(Surface,(0,0,0),[mx,my,10,10],0)
        if e.type==pygame.KEYDOWN:
            keys= pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                t=False
    pygame.display.update()
