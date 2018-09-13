import random
import time
import pygame, sys
from pygame.locals import *

class cuadro :
    des = False
    mina = False
    num = 0
    highlight = False
    flag = 0


def GenMatriz(x,y,m) :
    assert( m + 1 < x*y )
    A = [ [ cuadro() for j in range(y) ] for i in range(x) ]
    B = []
    for i in range(x) :
        for j in range(y) :
            B.append( (i,j) )
    minas = random.sample(B, m)
    for i in range(x) :
        for j in range(y) :
            if (i,j) in minas :
                A[i][j].mina = True
                A[i][j].num = -1
    for i in range(x) :
        for j in range(y) :
            n = 0
            if (i,j) in minas :
                for a in range(-1,2) :
                    for b in range(-1,2) :
                        if 0 <= i+a < x and 0 <= j+b < y :
                            A[i+a][j+b].num += 1
    return A

def GenMatrizChida(x,y,m,a,b) :
    assert( m + 1 < x*y )
    A = [ [ cuadro() for j in range(y) ] for i in range(x) ]
    B = []
    for i in range(x) :
        for j in range(y) :
            if (a,b) != (i,j) :
                B.append( (i,j) )
    minas = random.sample(B, m)
    for i in range(x) :
        for j in range(y) :
            if (i,j) in minas :
                A[i][j].mina = True
                A[i][j].num = -1
    for i in range(x) :
        for j in range(y) :
            n = 0
            if (i,j) in minas :
                for a in range(-1,2) :
                    for b in range(-1,2) :
                        if 0 <= i+a < x and 0 <= j+b < y :
                            A[i+a][j+b].num += 1
    return A

def revelar(A,x,y) :
    B = [(x,y)]
    for C in B :
        i,j = C[0],C[1]
        for a in range(-1,2) :
            for b in range(-1,2) :
                if 0 <= i+a < len(A) and 0 <= j+b < len(A[0]) :
                    if not A[i+a][j+b].mina :
                        A[i+a][j+b].des = True
                        if A[i+a][j+b].num == 0 and not( (i+a,j+b) in B ) :
                            B.append((i+a,j+b))

def destapar(A,x,y) :
    if A[x][y].mina == True :
        A[x][y].num = -1
    else :
        A[x][y].des = True
        if A[x][y].num == 0 :
            revelar(A,x,y)

def ms(b) :
    c = int(round(b))
    m = c // 60
    s = c % 60
    a = ''
    if m >= 10 :
        a+= str(m)+':'
    elif m < 10 :
        a+= '0'+str(m)+':'
    if s >= 10 :
        a += str(s)
    elif s < 10 :
        a += '0'+str(s)
    return a

def getconfig() :
    open('buscaminastragavenao.cfg', 'a').close()
    sav = open('buscaminastragavenao.cfg', 'r+')
    s = sav.read()
    sav.close()
    s = s.split('\n')
    with open('buscaminastragavenao.cfg', 'r+') as sav :
        if s == [''] :
            sav.write('9,9,10')
            return (9,9,10)
        try :
            s = s[0].split(',')
            s = (int(s[0]),int(s[1]),int(s[2]))
            assert( 75 >= s[0] > 1 and 40 >= s[1] > 1 and (s[0]*s[1])-1 > s[2] >= 1 )
            return s
        except:
            sav.write('9,9,10,0,0,255\n'+'Gary estuvo aqui, joseandres es un perdedor\n')
            return (9,9,10)

def getcolor() :
    open('buscaminastragavenao.cfg', 'a').close()
    sav = open('buscaminastragavenao.cfg', 'r+')
    s = sav.read()
    sav.close()
    s = s.split('\n')
    with open('buscaminastragavenao.cfg', 'r+') as sav :
        if s == [''] :
            sav.write('9,9,10')
            return (9,9,10)
        try :
            s = s[0].split(',')
            s = (int(s[3]),int(s[4]),int(s[5]))
            assert( all( 255 >= i >= 0 for i in s) )
            return s
        except:
            sav.write('9,9,10,0,0,255\n'+'Gary estuvo aqui, joseandres es un perdedor\n')
            return (0,0,255)

def geths() :
    open('highscores', 'a').close()
    sav = open('highscores', 'r+')
    s = sav.read()
    sav.close()
    s = s.split('\n')
    with open('highscores', 'r+') as sav :
        if s == [''] :
            return []
        try :
            for i in range(len(s)) :
                s[i] = s[i].split(' ')
                s[i][1] = int(s[i][1])
                assert( len(s[i][0]) <= 10 and s[i][1] > 0 )
            return s[:10]
        except:
            sav.write('')
            return []

def savehs(hs) :
    sav = open('highscores', 'r+')
    sav.read()
    sav.close()
    for i in range(len(hs)) :
        for j in range(i+1,len(hs)) :
            if hs[i][1] > hs[j][1] :
                hs[i],hs[j] = hs[j],hs[i]
    for i in range(len(hs)) :
        hs[i][1] = str(hs[i][1])
        hs[i] = ' '.join(hs[i])
    hs = '\n'.join(hs)
    sav = open('highscores', 'w')
    sav.write(hs)
    sav.close()

def blankconfig() :
    sav = open('buscaminastragavenao.cfg', 'r+')
    sav.read()
    sav.close()

def saveconfig(x,y,m,RGB) :
    blankconfig()
    sav = open('buscaminastragavenao.cfg', 'w')
    sav.write(str(x)+','+str(y)+','+str(m)+','+str(RGB[0])+','+str(RGB[1])+','+str(RGB[2]))
    sav.close()

def menusito(surf,n,font) :
    surf.fill((255,255,255))
    pygame.draw.polygon(surf, (100,100,255), ((0, 80*n), (0, 80+80*n), (400, 80+80*n), (400, 80*n)))
    texto = font.render('Juego Normal', True, (0,0,0))
    rect = texto.get_rect()
    rect.center = (200, 40)
    surf.blit(texto, rect)
    texto = font.render('Juego Personalizado', True, (0,0,0))
    rect = texto.get_rect()
    rect.center = (200, 120)
    surf.blit(texto, rect)
    texto = font.render('Opciones', True, (0,0,0))
    rect = texto.get_rect()
    rect.center = (200, 200)
    surf.blit(texto, rect)
    texto = font.render('Highscores', True, (0,0,0))
    rect = texto.get_rect()
    rect.center = (200, 280)
    surf.blit(texto, rect)
    texto = font.render('Creditos', True, (0,0,0))
    rect = texto.get_rect()
    rect.center = (200, 360)
    surf.blit(texto, rect)

def opcionsitas(surf,n,x,y,m,font,color) :
    surf.fill((255,255,255))
    pygame.draw.polygon(surf, (100,100,255), ((0, 80*n), (0, 80+80*n), (400, 80+80*n), (400, 80*n)))
    texto = font.render('Numero de filas: '+str(x), True, (0,0,0))
    rect = texto.get_rect()
    rect.center = (200, 40)
    surf.blit(texto, rect)
    texto = font.render('Numero de columnas: '+str(y), True, (0,0,0))
    rect = texto.get_rect()
    rect.center = (200, 120)
    surf.blit(texto, rect)
    texto = font.render('Numero de minas: '+str(m), True, (0,0,0))
    rect = texto.get_rect()
    rect.center = (200, 200)
    surf.blit(texto, rect)
    texto = font.render('Color de bandera', True, color)
    rect = texto.get_rect()
    rect.center = (200, 280)
    surf.blit(texto, rect)
    texto = font.render('Volver', True, (0,0,0))
    rect = texto.get_rect()
    rect.center = (200, 360)
    surf.blit(texto, rect)

def highscores(surf,hs,font) :
        surf.fill((255,255,255))
        for i in range(len(hs)) :
            texto = font.render(str(i+1)+'. '+hs[i][0], True, (0,0,0))
            rect = texto.get_rect()
            rect.center = (100, 15+i*40)
            surf.blit(texto, rect)
            texto = font.render(ms(hs[i][1]), True, (0,0,0))
            rect = texto.get_rect()
            rect.center = (300, 15+i*40)
            surf.blit(texto, rect)
        for i in range(len(hs),10) :
            texto = font.render('---', True, (0,0,0))
            rect = texto.get_rect()
            rect.center = (100, 15+i*40)
            surf.blit(texto, rect)
            texto = font.render('-', True, (0,0,0))
            rect = texto.get_rect()
            rect.center = (300, 15+i*40)
            surf.blit(texto, rect)

def nombresito(surf,name,T,font1,font2) :
    surf.fill((255,255,255))
    texto = font2.render('Nuevo record', True, (0,0,0))
    rect = texto.get_rect()
    rect.center = (200, 20)
    surf.blit(texto, rect)
    texto = font1.render('Introduzca su nombre y presione "enter"', True, (0,0,0))
    rect = texto.get_rect()
    rect.center = (200, 100)
    surf.blit(texto, rect)
    texto = font2.render(name, True, (0,0,0))
    rect = texto.get_rect()
    rect.center = (200, 200)
    surf.blit(texto, rect)
    texto = font2.render(ms(T), True, (0,0,0))
    rect = texto.get_rect()
    rect.center = (200, 350)
    surf.blit(texto, rect)

def banderita(surf,a,b,color) :
    pygame.draw.line(surf, (0,0,0), (a+4, b+2), (a+4, b+12), 2)
    pygame.draw.polygon(surf, color, ((a+6, b+2), (a+6, b+8), (a+11, b+5)))

def Tablero(surf,M,t,font,color) :
    surf.fill((255,255,255))
    reloj = font.render(ms(time.clock()-t), True, (0,0,0))
    rect = reloj.get_rect()
    rect.center = (len(M)*17//2, 10+len(M[0])*17)
    surf.blit(reloj, rect)
    for i in range(len(M)) :
        for j in range(len(M[i])) :
            if not M[i][j].des :
                if M[i][j].flag == 1 :
                    pygame.draw.polygon(surf, (127,127,127), ((1+i*17, 1+j*17), (1+i*17, 16+j*17), (16+i*17, 16+j*17), (16+i*17, 1+j*17)))
                    banderita(surf,1+i*17, 1+j*17,color)
                elif M[i][j].flag == 2 :
                    pygame.draw.polygon(surf, (127,127,127), ((1+i*17, 1+j*17), (1+i*17, 16+j*17), (16+i*17, 16+j*17), (16+i*17, 1+j*17)))
                    numerito = font.render('?', True, (0,0,0))
                    rect = numerito.get_rect()
                    rect.center = (9+i*17, 9+j*17)
                    surf.blit(numerito, rect)
                elif not M[i][j].highlight :
                    pygame.draw.polygon(surf, (127,127,127), ((1+i*17, 1+j*17), (1+i*17, 16+j*17), (16+i*17, 16+j*17), (16+i*17, 1+j*17)))
                elif M[i][j].highlight :
                    pygame.draw.polygon(surf, (180,180,180), ((1+i*17, 1+j*17), (1+i*17, 16+j*17), (16+i*17, 16+j*17), (16+i*17, 1+j*17)))
            elif M[i][j].des :
                pygame.draw.polygon(surf, (200,200,200), ((1+i*17, 1+j*17), (1+i*17, 16+j*17), (16+i*17, 16+j*17), (16+i*17, 1+j*17)))
                if M[i][j].num != 0 :
                    numerito = font.render(str(M[i][j].num), True, (0,0,0))
                    rect = numerito.get_rect()
                    rect.center = (9+i*17, 9+j*17)
                    surf.blit(numerito, rect)

def TableroGG(surf,M,t,victory,font) :
    surf.fill((255,255,255))
    if victory :
        v = 'Victoria'
    elif not victory :
        v = 'Derrota'
    reloj = font.render(v+' '+ms(t), True, (0,0,0))
    rect = reloj.get_rect()
    rect.center = (len(M)*17//2, 10+len(M[0])*17)
    surf.blit(reloj, rect)
    for i in range(len(M)) :
        for j in range(len(M[i])) :
            if M[i][j].num != -1 :
                pygame.draw.polygon(surf, (200,200,200), ((1+i*17, 1+j*17), (1+i*17, 16+j*17), (16+i*17, 16+j*17), (16+i*17, 1+j*17)))
            elif M[i][j].num == -1 :
                pygame.draw.polygon(surf, (200,0,0), ((1+i*17, 1+j*17), (1+i*17, 16+j*17), (16+i*17, 16+j*17), (16+i*17, 1+j*17)))
            if M[i][j].mina :
                surf.blit(mine, (1+i*17, 1+j*17))
            elif M[i][j].num != 0 :
                numerito = font.render(str(M[i][j].num), True, (0,0,0))
                rect = numerito.get_rect()
                rect.center = (9+i*17, 9+j*17)
                surf.blit(numerito, rect)

def creditos(surf,n,font) :
    surf.fill((0,0,0))
    c = ['Buscaminas Tragavenao Edition 2.1','','Creado por Leonardo Lopez','Utilizando python 3.5.2 y pygame','','Agradecimientos especiales','','Satoru Iwata (QEPD)','','La estatua del buho','','','Pero mas que a nadie','a ti, jugador','por hacer todo esto','esto posible','','','','','','','','Gracias por jugar']
    for i in range(len(c)) :
        texto = font.render(c[i], True, (255,255,255))
        rect = texto.get_rect()
        rect.center = (200, n+30*i)
        surf.blit(texto, rect)

def posi(evento) :
    pos = evento.pos
    pos = (pos[0]//17,pos[1]//17)
    return pos

def posiValida(pos,A) :
    return 0 <= pos[0] < len(A) and 0 <= pos[1] < len(A[0])

def esrecord(a,b,c,T,v) :
    return v and a == 9 and b == 9 and c == 10 and ( len(geths()) < 10 or not all( T > hs[1] for hs in geths()))

def sans(n) :
    return pygame.font.Font('freesansbold.ttf', n)

def enter(e) :
    if e.type == KEYDOWN :
        if e.key == K_RETURN :
            return True
    elif e.type == MOUSEBUTTONDOWN :
        if event.button == 1 :
            return True
    return False

def derecha(e) :
    if e.type == KEYDOWN :
        if e.key == K_RIGHT :
            return True
    elif e.type == MOUSEBUTTONDOWN :
        if event.button == 1 or event.button == 4 :
            return True
    return False

def izquierda(e) :
    if e.type == KEYDOWN :
        if e.key == K_LEFT :
            return True
    elif e.type == MOUSEBUTTONDOWN :
        if event.button == 3 or event.button == 5 :
            return True
    return False

modo = 'menu'
menu = color_index = 0

pygame.init()
ventana = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Buscaminas Tragavenao')
fpsClock = pygame.time.Clock()
mine = pygame.image.load('mina.png')
(x,y,m) = getconfig()
flag_color = getcolor()

derrota = victoria = False

while True:
    if modo == 'menu' :
        menusito(ventana,menu,sans(20))
    elif modo == 'game' :
        Tablero(ventana,A,t1,sans(12),flag_color)
    elif modo == 'gg' :
        TableroGG(ventana,A,t2-t1,victoria,sans(12))
    elif modo == 'opciones' :
        opcionsitas(ventana,menu,x,y,m,sans(20),flag_color)
    elif modo == 'creditos' :
        creditos(ventana,cred,sans(20))
    elif modo == 'highscore' :
        highscores(ventana,geths(),sans(20))
    elif modo == 'nombre' :
        nombresito(ventana,nombre,t2-t1,sans(20),sans(30))

    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()

        elif modo == 'menu' :
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    pygame.quit()
                    sys.exit()
                elif event.key == K_DOWN and menu < 4 :
                    menu += 1
                elif event.key == K_UP and menu > 0 :
                    menu -= 1
            elif event.type == MOUSEMOTION :
                menu = event.pos[1] // 80
            if enter(event) :
                    if menu == 0 :
                        x,y,m = 9,9,10
                        A = GenMatriz(x,y,m)
                        modo = 'game'
                        surf = pygame.display.set_mode((1+len(A)*17, 21+len(A[0])*17))
                        derrota = victoria = False
                        t1 = time.clock()
                        #pygame.mixer.music.load('bgm.mp3')
                        #pygame.mixer.music.play(-1, 0.0)
                    elif menu == 1 :
                        (x,y,m) = getconfig()
                        A = GenMatriz(x,y,m)
                        surf = pygame.display.set_mode((1+len(A)*17, 21+len(A[0])*17))
                        modo = 'game'
                        derrota = victoria = False
                        t1 = time.clock()
                        #pygame.mixer.music.load('bgm.mp3')
                        #pygame.mixer.music.play(-1, 0.0)
                    elif menu == 2 :
                        (x,y,m) = getconfig()
                        flag_color = getcolor()
                        color_list = [flag_color,(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,0,255),(0,255,255),(150,0,200),(0,0,0)]
                        menu = color_index = 0
                        modo = 'opciones'
                    elif menu == 3 :
                        modo = 'highscore'
                    elif menu == 4 :
                        modo = 'creditos'
                        cred = 400
                        #pygame.mixer.music.load('bgm.mp3')
                        #pygame.mixer.music.play(-1, 0.0)

        elif modo == 'opciones' :
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    pygame.quit()
                    sys.exit()
                elif event.key == K_DOWN and menu < 4 :
                    menu += 1
                elif event.key == K_UP and menu > 0 :
                    menu -= 1
            if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN :
                if menu == 0 :
                    if derecha(event) and x < 75 :
                        x += 1
                    elif izquierda(event) and x > 2 :
                        x -= 1
                elif menu == 1 :
                    if derecha(event) and y < 40 :
                        y += 1
                    elif izquierda(event) and y > 2 :
                        y -= 1
                elif menu == 2 :
                    if derecha(event) and m < (x*y)-2 :
                        m += 1
                    elif izquierda(event) and m > 1 :
                        m -= 1
                elif menu == 2 :
                    if derecha(event) and m < (x*y)-2 :
                        m += 1
                    elif izquierda(event) and m > 1 :
                        m -= 1
                elif menu == 3 :
                    if derecha(event) and color_index < len(color_list)-1 :
                        color_index += 1
                    elif izquierda(event) and color_index >= 1 :
                        color_index -= 1
                elif menu == 4 :
                    if enter(event) :
                        saveconfig(x,y,m,flag_color)
                        menu = 0
                        modo = 'menu'
                if m >= (x*y)-2 :
                    m = (x*y)-2
            elif event.type == MOUSEMOTION :
                menu = event.pos[1] // 80
            flag_color = color_list[color_index]

        elif modo == 'game' :
            if event.type == MOUSEMOTION :
                pos = posi(event)
                if posiValida(pos,A) :
                    for i in range(len(A)) :
                        for j in range(len(A[0])) :
                            if i == pos[0] and j == pos[1] :
                                A[i][j].highlight = True
                            else :
                                A[i][j].highlight = False
            elif event.type == MOUSEBUTTONDOWN :
                pos = posi(event)
                if posiValida(pos,A) :
                    if event.button == 1 and A[pos[0]][pos[1]].flag == 0 :
                        if A[pos[0]][pos[1]].mina == True :
                            if all( all( not A[i][j].des for j in range(len(A[0]))) for i in range(len(A)) ) :
                                A = GenMatrizChida(x,y,m,pos[0],pos[1])
                                destapar(A,pos[0],pos[1])
                            else :
                                destapar(A,pos[0],pos[1])
                                derrota = True
                        else :
                            destapar(A,pos[0],pos[1])
                    elif event.button == 3 and not A[pos[0]][pos[1]].des :
                        if A[pos[0]][pos[1]].flag != 2 :
                            A[pos[0]][pos[1]].flag += 1
                        else :
                            A[pos[0]][pos[1]].flag = 0
            elif event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    modo = 'menu'
                    ventana = pygame.display.set_mode((400, 400))
            victoria = all( all( A[i][j].mina or A[i][j].des for j in range(len(A[0]))) for i in range(len(A)) )

        elif modo == 'gg' :
            if event.type == MOUSEBUTTONDOWN or event.type == KEYDOWN :
                #pygame.mixer.music.stop()
                if not esrecord(x,y,m,t2-t1,victoria) :
                    modo = 'menu'
                    ventana = pygame.display.set_mode((400, 400))
                elif esrecord(x,y,m,t2-t1,victoria) :
                    modo = 'nombre'
                    nombre = ''
                    ventana = pygame.display.set_mode((400, 400))

        elif modo == 'nombre' :
            if event.type == KEYDOWN :
                if event.key == K_BACKSPACE :
                    nombre = nombre[:-1]
                elif event.key == K_RETURN and len(nombre) >= 1 :
                    highS = geths()
                    highS.append([nombre,int(t2-t1)])
                    savehs(highS)
                    modo = 'highscore'
                elif len(nombre) < 10 and event.unicode != ' ' :
                    nombre += event.unicode

        elif modo == 'creditos' or modo == 'highscore' :
            if event.type == MOUSEBUTTONDOWN or event.type == KEYDOWN :
                #pygame.mixer.music.stop()
                modo = 'menu'

    if modo == 'game' :
        if derrota or victoria :
            modo = 'gg'
            t2 = time.clock()
    elif modo == 'creditos' and cred > -480 :
        cred -= 1
   
    pygame.display.update()
    fpsClock.tick(60)
