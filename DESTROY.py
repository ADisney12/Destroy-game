import pygame
pygame.init()
import random

dis = pygame.display.set_mode((500, 500))
x = 225
y = 354
vel = 0
vel2 = 1.5
vel1 = 0
v1 = 0
v2 = 0
v3 = 0
laps = 0
a = 600
b = 600
ex = False
run = False
hit = False
point = 0
mawaf = False
mawaf2 = False
row = 0
ex1 = False
hit2 = False
l = 360
ga = False
isclicked = False
showpoints = False
showpoints2 = False
se = 0
le = 0
hit2 = False
se2 = 0
le2 = 0
cheat = False
z = 100000
velp = 1.7
pause = False
vel100 = 1
die = False
dx = 75
dy = 350
yes = False
mx = 25
my = 60
mex = 350
mey = 350
sx = 25
sy = 150
skin = False
mx1 = 40
my1 = 200
mx2 = 150
my2 = 200
mx3 = 260
my3 = 200
run5 = 0
choose = 1
#choose0 = False
#choose1 = False
player = False
game = False
lex = 400
ley = 40
# fonts, icons and backrounds
font = pygame.font.Font('freesansbold.ttf',37)
#score
textx = 165
texty = 10


def show_score(textx, texty):
    score = font.render("score:" + str(point), True, (255, 255, 255))
    dis.blit(score, (textx,texty))

textx2 = 10
texty2 = 465

#row
font2 = pygame.font.Font('freesansbold.ttf',50)
font4 = pygame.font.Font('freesansbold.ttf',30)

def show_score2(textx2, texty2):
    score2 = font4.render(str(row) + " in a row", True, (255, 255, 255))
    dis.blit(score2, (textx2,texty2))


#laps
font3 = pygame.font.Font('freesansbold.ttf',80)
textx3 = 250
texty3 = 465
def lap(textx3, texty3):
    score3 = font3.render(str(laps,), True, (255, 255, 255))
    dis.blit(score3, (textx3, texty3))

#player1
player1 = pygame.image.load('Python/destroy game/ClipartKey_146283.png')
ship = pygame.transform.scale(player1, (60, 60))
#player2
player2 = pygame.image.load('Python/destroy game/Pngitem_851274.png')
ship2 = pygame.transform.scale(player2, (60, 60))
#player3
player3 = pygame.image.load('Python/destroy game/Spaceship_tut.png')
ship3 = pygame.transform.scale(player3, (60, 60))

'''
if player == True:
    if choose == 2:
        dis.blit(ship, (x, y))
    if choose == 1:
        dis.blit(ship2, (x, y))
    '''
'''
ef playerec():
    pygame.draw.rect(dis, (255, 255, 255), (x, y, 80, 30))
'''
#backround
backround = pygame.image.load('Python/destroy game/space.jpg')
moon = pygame.transform.scale(backround, (500, 500))

#and the enemies
astroid = pygame.image.load('Python/destroy game/pngfind.com-asteroid-png-3213202.png')
vi = pygame.transform.scale(astroid, (55, 55))
def vil():
    dis.blit(vi, (loc1, v1))

astroid2 = pygame.image.load('Python/destroy game/pngfind.com-asteroid-png-3213202.png')
vi2 = pygame.transform.scale(astroid2, (55, 55))
def vil2():
    dis.blit(vi2, (loc2, v2))

run4 = 0
run3 = 0
count = 0
main = True
explode = False
exp = 200
while main == True:
    pygame.time.delay(2)
    if game == False:
        #basics
        back = pygame.image.load("Python/destroy game/screenshot 2021-03-02 074604.png")
        relback = pygame.transform.scale(back, (500, 500))
        dis.fill((0, 0, 0))
        #dis.blit(relback, (1, 1))
        dis.blit(moon, (1, 1))
        #pygame.draw.rect(dis, (255, 255, 255), (mx, my, 80, 30))
        play = font3.render("play", True, (255, 255, 255))
        fontop = pygame.font.Font('freesansbold.ttf',30)
        op = fontop.render("options", True, (255, 255, 255))
        ski = font2.render("skins", True, (255, 255, 255))
        dis.blit(ski, (25, 160))
        dis.blit(play, (25, 60))
        dis.blit(op, (25, 230))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
        #keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            main = False
            run = True
            lap = 0
            point = 0

        #button
        pygame.draw.rect(dis, (32, 99, 233,), (a, b, 20, 35))
        mo = pygame.mouse.get_pos()
        print(mo[0], mo[1])
        if mo[0] > mx:
            run3 = mo[0] - mx
        if mo[0] < mx:
            run3 = mx - mo[0] + 90
        if run3 < 150:
            if mo[1] > my:
                run3 = mo[1] - my 
            if mo[1] < my:
                run3 = my - mo[1] + 60 
            if run3 < 70:
                pygame.draw.rect(dis, (172, 188, 194), (mx, my, 160, 85))
                dis.blit(play, (25, 60))    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if skin == False:    
                            game = True
                            lap = 0
                            point = 0
                            x = 225
                            y = 354
                            v1 = 0
                            row = 0
                            vel2 = 1.5
                            vel100 = 1
                            velp = 1.7

        if mo[0] > sx:
            run4 = mo[0] - sx
        if mo[0] < sx:
            run4 = sx - mo[0] + 90
        if run4 < 130:
            if mo[1] > sy:
                run4 = mo[1] - sy 
            if mo[1] < sy:
                run4 = sy - mo[1] + 60
            if run4 < 50:
                pygame.draw.rect(dis, (172, 188, 194), (sx, sy, 140, 60))
                dis.blit(ski, (25, 160))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        skin = True
        
        
        if skin == True:
            dis.fill((0, 0, 0))
            player = False
            shipt = pygame.transform.scale(ship, (100, 100))
            ship2t = pygame.transform.scale(ship2, (100, 100))
            ship3t = pygame.transform.scale(ship3, (100, 100))
            font3.render("skins", True, (255, 255, 255))
            dis.blit(shipt, (mx1, my1))
            dis.blit(ship2t, (mx2, my2))
            dis.blit(ship3t, (mx3, my3))
            if mo[0] > mx1:
                run5 = mo[0] - mx1
            if mo[0] < mx1:
                run5 = mx1 - mo[0] + 100
            if run5 < 100:
                if mo[1] > my1:
                    run5 = mo[1] - my1
                if mo[1] < my1:
                    run5 = my1 - mo[1] + 100
                if run5 < 100:
                    pygame.draw.rect(dis, (172, 188, 194), (mx1, my1, 100, 100))
                    dis.blit(shipt, (mx1, my1))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            choose = 1
                print(choose)
            if choose == 1:
                pygame.draw.rect(dis, (172, 188, 194), (mx1, my1, 100, 100))
                dis.blit(shipt, (mx1, my1))
            
            if mo[0] > mx2:
                run5 = mo[0] - mx2
            if mo[0] < mx2:
                run5 = mx2 - mo[0] + 100
            if run5 < 100:
                if mo[1] > my2:
                    run5 = mo[1] - my2
                if mo[1] < my2:
                    run5 = my2 - mo[1] + 100
                if run5 < 100:
                    pygame.draw.rect(dis, (172, 188, 194), (mx2, my2, 100, 100))
                    dis.blit(ship2t, (mx2, my2))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            choose = 2
            if choose == 2:
                pygame.draw.rect(dis, (172, 188, 194), (mx2, my2, 100, 100))
                dis.blit(ship2t, (mx2, my2))

            if mo[0] > mx3:
                run5 = mo[0] - mx3
            if mo[0] < mx3:
                run5 = mx3 - mo[0] + 100
            if run5 < 100:
                if mo[1] > my3:
                    run5 = mo[1] - my3
                if mo[1] < my3:
                    run5 = my3 - mo[1] + 100
                if run5 < 100:
                    pygame.draw.rect(dis, (172, 188, 194), (mx3, my3, 100, 100))
                    dis.blit(ship3t, (mx3, my3))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            choose = 3
            if choose == 3:
                pygame.draw.rect(dis, (172, 188, 194), (mx3, my3, 100, 100))
                dis.blit(ship3t, (mx3, my3))
            
            if keys[pygame.K_e]:
                skin = False
                
            pygame.draw.rect(dis, (90, 91, 92), (lex, ley, 50, 50))
            if mo[0] > lex:
                run1 = mo[0] - lex
            if mo[0] < lex:
                run1 = lex - mo[0] + 30
            if run1 < 50:
                if mo[1] > ley:
                    run1 = mo[1] - ley
                if mo[1] < ley:
                    run1 = ley - mo[1] + 30
                if run1 < 50:
                    pygame.draw.rect(dis, (255, 255, 255), (lex, ley, 50, 50))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            skin = False
                            game = False
        
        
        #loc      
        if v1 == 0:
            loc1 = random.randint(0,450)
        loc2 = random.randint(0,450)
        
            
        
        if player == True:
            if choose == 1:
                dis.blit(ship, (x, y))
            if choose == 2:
                dis.blit(ship2, (x, y))
            if choose == 3:
                dis.blit(ship3, (x, y))
        
        if skin == False:    
            player = True
            vil()
        #vi2()
        
        #the ai
        shoot = False
        run2 = y - b
        v1 = v1 + 6
        #v2 = v2 - 1.5
        if run2 > 200:    
            if loc1 > x:
                run1 = loc1 - x
                x = x + 7
            if loc1 < x:
                run1 = x - loc1 
                x = x - 7
            if run1 < 40 and count == 0:
                shoot = True
                count = count + 1
                
        
        if v1 >= 500:
            v1 = v1 - 500
        pygame.display.update()
        
        
        if shoot == True:
            a = x + 16
            b = y
            shoot = False
        
        b = b - 7
        
        if run2 > 200:
            count = 0

        #if run2 > 50:
            #x = x - 8
        
        if count >= 1:
            shoot = False
        
        

        if v1 > b and v1 < 360:
            ex = True
            if ex == True: 
                if loc1 > a:
                    run1 = loc1 - a
                    run1 = run1 + 25
                if loc1 < a:
                    run1 = a - loc1
                if a == loc1:
                    run1 = 1
                if run1 < 45:
                    hit = True
                    se = loc1
                    le = v1
                    showpoints = True
                if hit == True:
                    d = v1
                    v1 = v1 - d
                    point = point + 100
                    row = row + 1
                    hit = False
                ex = False

        
    if game == True:
        dis.fill((0, 0, 0))
        dis.blit(moon, (0, 0))
        isclicked = False
        show_score(textx, texty)
        show_score2(textx2, texty2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
        



        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a] and x > 0:
            x = x - velp
        if keys[pygame.K_d] and x < 440:
            x = x + velp
        if keys[pygame.K_p]:
            row += 10000 
            point += 1000000

        if die == False or die == False:
            if keys[pygame.K_SPACE]:
                pause = True

            if pause == True:    
                vel2 = 0
                velp = 0
                vel1 = 0
                vel100 = 0
                mo = pygame.mouse.get_pos()
                fonthuge = pygame.font.Font('freesansbold.ttf',60)
                paused = fonthuge.render("paused", True, (255, 255, 255))
                dis.blit(paused, (140, 200))
                pygame.draw.rect(dis, (90, 91, 92), (mex, mey, 50, 50))
                if mo[0] > mex:
                    run1 = mo[0] - mex
                if mo[0] < mex:
                    run1 = mex - mo[0] + 50
                if run1 < 50:
                    if mo[1] > mey:
                        run1 = mo[1] - mey
                    if mo[1] < mey:
                        run1 = mey - mo[1] + 50
                    if run1 < 50:
                        pygame.draw.rect(dis, (255, 255, 255), (mex, mey, 50, 50))
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if event.button == 1:
                                game = False
                                pause = False
                                                   
                
            
            if keys[pygame.K_e]:
                velp = 1.7
                vel2 = 1.5
                vel1 = 2.5
                vel100 = 1
                pause = False

        
        
        
            
            
        #shoot ability
        if die == False:    
            if pause == False:    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        isclicked = True
                    if isclicked == True:
                        a = x + 19
                        b = y
                        vel1 = 2.5
            
        #laps
        if v1 >= 500:
            v1 = v1 - 501
            laps = laps + 1
            k = row
            row = row - k
        if ga == True:    
            if v2 >= 500:
                v2 = v2 - 500
                laps = laps + 1
                d = row
                row = row - d
            

        
        
        if laps > 15:
            ga = True

        if ga == False:
            loc2 = 700
        

        if laps > 45:
            vel2 = 1.8
        if laps > 75:
            vel2 = 2.5

        
        #locations
        if v1 == 0:
            loc1 = random.randint(0,450)
        if ga == True:   
            if v2 == 0:    
                loc2 = random.randint(0,450)
                vel = 1.5
            loc3 = random.randint(0,490)
            loc4 = random.randint(0,490)
            loc5 = random.randint(0,490)

        
        
            
        if showpoints == True:
            plus = font.render("+100", True, (255, 255, 255)) 
            dis.blit(plus, (se, le))
            le = le - vel100

        if showpoints2 == True:
            plus = font.render("+100", True, (255, 255, 255)) 
            dis.blit(plus, (se2, le2))
            le2 = le2 - vel100
        
        b = b - vel1
        

        #creates the object
        #pygame.draw.rect(dis, (255, 0, 0,), (x, y, 30, 30))
        pygame.draw.rect(dis, (32, 99, 233,), (a, b, 20, 35))
            

        vil()
        vil2()
        #pygame.draw.rect(dis, (255, 255, 255,), (loc1, v1, 30, 30))
        if player == True:
            if choose == 1:
                dis.blit(ship, (x, y))
            if choose == 2:
                dis.blit(ship2, (x, y))
            if choose == 3:
                dis.blit(ship3, (x, y))
        player = True
        #pygame.draw.rect(dis, (255, 255, 255,), (loc2, v2, 30, 30))A
        '''
        pygame.draw.rect(dis, (255, 255, 255,), (loc3, v3, 30, 30))
        pygame.draw.rect(dis, (255, 255, 255,), (loc4, v1, 30, 30))
        pygame.draw.rect(dis, (255, 255, 255,), (loc5, v1, 30, 30))

        '''
        #MAKES astroids move
        v1 = v1 + vel2
        v2 = v2 + vel2
        v3 = v3 + vel
        kill = True
        
        print(laps)
        if b > 0:    
            if v1 > b and v1 < 360:
                ex = True
                if ex == True: 
                    if loc1 > a:
                        run1 = loc1 - a
                        run1 = run1 + 25
                    if loc1 < a:
                        run1 = a - loc1
                    if a == loc1:
                        run1 = 1
                    if run1 < 45:
                        hit = True
                        se = loc1 
                        le = v1
                        showpoints = True
                    if hit == True:
                        d = v1
                        v1 = v1 - d
                        point = point + 100
                        row = row + 1
                        hit = False
                    ex = False

        
        if hit == False and v1 > 90:
            showpoints = False
            se = 0
            le = 0


        if hit2 == False and v2 > 75:
            showpoints2 = False
            se2 = 0
            le2 = 0
        
        if b > 0:    
            if v2 > b and v2 < 360:
                ex1 = True
                if ex1 == True:
                    if loc2 > a:
                        run1 = loc2 - a
                        run1 = run1 + 25
                    if loc2 < a:
                        run1 = a - loc2
                    if a == loc2:
                        hit2 = True
                    if run1 < 46:
                        hit2 = True
                        se2 = loc2
                        le2 = v2
                        showpoints2 = True
                    if hit2 == True:
                        d = v2
                        v2 = v2 - d
                        point = point + 100
                        row = row + 1
                        hit2 = False
                    ex1 = False
            
            
        

        print(str(row) + " " + "in a row")

    #how you die


        if v1 > y and v1 < 375:
            mawaf = True
            if mawaf == True:
                if loc1 > x:
                    fun = loc1 - x
                if x > loc1:
                    fun = x - loc1
                if x == loc1:
                    fun = 5
                if fun < 55:
                    print("you died")
                    die = True
            mawaf = False
        
        if v2 > y and v2 < 375:
            mawaf2 = True
            if mawaf2 == True:
                if loc2 > x:
                    fun = loc2 - x
                if x > loc2:
                    fun = x - loc2
                if x == loc2:
                    fun = 5
                if fun < 55:
                    print("you died")
                    die = True
            mawaf2 = False
        
        
        
        if die == True:
            vel = 0
            vel1 = 0
            vel2 = 0
            vel100 = 0
            velp = 0
            ga = False
            dis.fill((255, 255, 255))
            ded = font.render("you died", True, (0, 0, 0))
            fonts = pygame.font.Font('freesansbold.ttf',26)
            click = fonts.render("click here to restart", True, (0, 0, 0))
            dis.blit(ded, (150, 200))
            dis.blit(click, (30, 310))
            pygame.draw.rect(dis, (0, 0, 0), (dx, dy, 50, 50))
            pygame.draw.rect(dis, (0, 0, 0), (mex, mey, 50, 50))
            mo = pygame.mouse.get_pos()
            if mo[0] > dx:
                run1 = mo[0] - dx
            if mo[0] < dx:
                run1 = dx - mo[0] + 50
            if run1 < 50:
                if mo[1] > dy:
                    run1 = mo[1] - dy
                if mo[1] < dy:
                    run1 = dy - mo[1] + 30
                if run1 < 50:
                    pygame.draw.rect(dis, (90, 91, 92), (dx, dy, 50, 50))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            laps = 0
                            die = False
                            point = 0 
                            vel = 0
                            vel2 = 1.5
                            velp = 1.7
                            vel1 = 0
                            v1 = 0
                            v2 = 0
                            vel100 = 1
                            row = 0
                            
            
            if mo[0] > mex:
                run1 = mo[0] - mex
            if mo[0] < mex:
                run1 = mex - mo[0] + 50
            if run1 < 50:
                if mo[1] > mey:
                    run1 = mo[1] - mey
                if mo[1] < mey:
                    run1 = mey - mo[1] + 50
                if run1 < 50:
                    pygame.draw.rect(dis, (90, 91, 92), (mex, mey, 50, 50))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            game = False
                            die = False
                            
        
      
        pygame.display.update()
        