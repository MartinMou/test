import pygame as pg
from pygame.locals import (K_UP, K_DOWN)
import random as rd



VINDU_BREDDE = 720
VINDU_HOYDE  = 480
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])



l1 = []
for i in range(-400,-200):
    l1.append(i)

for i in range(200,400):
    l1.append(i)    

tilfeldig_tall = rd.randint(0,200)
tilfeldig_tall2= rd.randint(0,200)



class Ball:
  """Klasse for å representere en ball"""
  def __init__(self, x, y, radius, farge, vindusobjekt):
    """Konstruktør"""
    self.x = x
    self.y = y
    self.radius = radius
    self.farge = farge
    self.vindusobjekt = vindusobjekt
  
  def tegn(self):
    """Metode for å tegne ballen"""
    pg.draw.circle(self.vindusobjekt, self.farge, (self.x, self.y), self.radius)

class Hinder(Ball):
    def __init__(self, x, y, radius, farge, vindusobjekt, xFart, yFart):
        super().__init__(x, y, radius, farge, vindusobjekt)
        self.xFart = xFart
        self.yFart = yFart
    
    def flytt(self,rectangle1,rectangle2):
        """Metode for å flytte hinderet"""
        # Sjekker om hinderet er utenfor høyre/venstre kant
        if ((self.x + self.radius)>=VINDU_BREDDE):
            self.xFart = -self.xFart
            rectangle1.increase_score()
        if ((self.x - self.radius) <= 0):
            self.xFart = -self.xFart
            rectangle2.increase_score()
    
        # Sjekker om hinderet er utenfor øvre/nedre kant
        if ((self.y - self.radius) <= 0) or ((self.y + self.radius) >= self.vindusobjekt.get_height()):
            self.yFart = -self.yFart

        if ((self.x - self.radius <= 21) and (rectangle1.ypos1 <= self.y <= rectangle1.ypos1 + 120)) or \
            ((self.x + self.radius >= 699) and (rectangle2.ypos2 <= self.y <= rectangle2.ypos2 + 120)):
             self.xFart = -self.xFart

        # Flytter hinderet
        self.x += self.xFart
        self.y += self.yFart
        return True
    
class Rectangle:
    def __init__(self,høyde,bredde,farge,vindu,fart):
        self.høyde = høyde
        self.bredde = bredde
        self.farge = farge
        self.vindu = vindu
        self.fart = fart
        self.ypos1 = 180
        self.ypos2 = 180
        self.score = 0
    
    def increase_score(self):
        self.score += 1       
        print(self, self.score)

    def tegn(self):
         """Metode for å tegne rektangelet"""
         pg.draw.rect(vindu,(255,255,255),(1,self.ypos1,20,120))
         pg.draw.rect(vindu,(255,255,255),(699,self.ypos2,20,120))

    def flytt(self, taster):
        """Metode for å flytte spilleren"""
        if taster[pg.K_w]:
         self.ypos1 -= self.fart
        if taster[pg.K_s]:
            self.ypos1 += self.fart
        if taster[K_UP]:
         self.ypos2 -= self.fart
        if taster[K_DOWN]:
            self.ypos2 += self.fart
        
rektangel1 = Rectangle(25,10,(255,255,255),vindu,0.6)
rektangel2 = Rectangle(25,10,(255,255,255),vindu,0.6)
hinder = Hinder(360, 240, 10, (255, 255, 255), vindu, l1[tilfeldig_tall]/1000, l1[tilfeldig_tall2]/1000)

fortsett = True
kjører = True


while fortsett:

    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
    
    trykkede_taster = pg.key.get_pressed()

    # Farger bakgrunnen lyseblå
    vindu.fill((110, 110, 110))
    rektangel1.tegn()
    rektangel2.tegn()
    hinder.tegn()
    hinder.flytt(rektangel1,rektangel2)
    rektangel1.flytt(trykkede_taster)
    rektangel2.flytt(trykkede_taster)

    if rektangel1.score == 0:
        bilde1 = pg.image.load("0.png")
    if rektangel1.score == 1:
        bilde1 = pg.image.load("1.png")
    if rektangel1.score == 2:
        bilde1 = pg.image.load("2.png")
    if rektangel1.score == 3:
        bilde1 = pg.image.load("3.png")
    if rektangel1.score == 4:
        bilde1 = pg.image.load("4.png")
    if rektangel1.score == 5:
        bilde1 = pg.image.load("5.png")
    if rektangel1.score == 6:
        bilde1 = pg.image.load("6.png")
    if rektangel1.score == 7:
        bilde1 = pg.image.load("7.png")
    if rektangel1.score == 8:
        bilde1 = pg.image.load("8.png")
    if rektangel1.score == 9:
        bilde1 = pg.image.load("9.png")
    
    if rektangel2.score == 0:
        bilde2 = pg.image.load("0.png")
    if rektangel2.score == 1:
        bilde2 = pg.image.load("1.png")
    if rektangel2.score == 2:
        bilde2 = pg.image.load("2.png")
    if rektangel2.score == 3:
        bilde2 = pg.image.load("3.png")
    if rektangel2.score == 4:
        bilde2 = pg.image.load("4.png")
    if rektangel2.score == 5:
        bilde2 = pg.image.load("5.png")
    if rektangel2.score == 6:
        bilde2 = pg.image.load("6.png")
    if rektangel2.score == 7:
        bilde2 = pg.image.load("7.png")
    if rektangel2.score == 8:
        bilde2 = pg.image.load("8.png")
    if rektangel2.score == 9:
        bilde2 = pg.image.load("9.png")

    

    score_display1 = vindu.blit(bilde1,(140,70))
    score_display2 = vindu.blit(bilde2,(510,70))
    
    
    if rektangel2.score == 10:
        print("Spiller 1 vant")
    if rektangel1.score == 10:
        print("spiller 2 vant")

    pg.display.flip()

pg.quit()