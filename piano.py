
# -*- coding: UTF-8 -*-
#!/usr/bin/env python
import pygame
import time
from RPi import GPIO
from array import array
from pygame.locals import *
import threading
import time


pygame.mixer.pre_init(48000, -16, 1, 1024)
pygame.init()

KEY_A = 11 
KEY_B = 13 
KEY_C = 15 
KEY_D = 16 
KEY_E = 18 
KEY_F = 22 
KEY_G = 29 
KEY_H = 31
KEY_I = 33




a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
i=0

keyUp_a=0
keyUp_b=0
keyUp_c=0
keyUp_d=0
keyUp_e=0
keyUp_f=0
keyUp_g=0
keyUp_h=0
keyUp_i=0



GPIO.setmode(GPIO.BOARD)

GPIO.setup(KEY_A,GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(KEY_B,GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(KEY_C,GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(KEY_D,GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(KEY_E,GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(KEY_F,GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(KEY_G,GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(KEY_H,GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(KEY_I,GPIO.IN, GPIO.PUD_DOWN)


GPIO.setup(3, GPIO.OUT)






piano_a = pygame.mixer.Sound("/home/pi/Desktop/project/sound1.wav")
piano_b = pygame.mixer.Sound("/home/pi/Desktop/project/sound2.wav")
piano_c = pygame.mixer.Sound("/home/pi/Desktop/project/sound3.wav")
piano_d = pygame.mixer.Sound("/home/pi/Desktop/project/sound4.wav")
piano_e = pygame.mixer.Sound("/home/pi/Desktop/project/sound5.wav")
piano_f = pygame.mixer.Sound("/home/pi/Desktop/project/sound6.wav")
piano_g = pygame.mixer.Sound("/home/pi/Desktop/project/sound7.wav")
piano_h = pygame.mixer.Sound("/home/pi/Desktop/project/sound8.wav")
piano_i = pygame.mixer.Sound("/home/pi/Desktop/project/rec.wav")



#함수를 쓰레드로 만들 때의 공유자원을 가정한 변수
globalResource = 0


#함수형 쓰레드. 사실 그 어떤 함수가 오더라도 관계가 없음.
#단 이 함수에서만 사용하는 상태변수를 격납하기 어렵다는 단점이 있다.
def clock_usingGlobalVariable(interval):
    #함수에서는 지역변수가 기본이라 global키워드를 사용해서 global변수를 사용한다고 명시적으로 지정해 줄 필요가 있음.
    global globalResource
    while True:
        globalResource += 1
        print 'this is {0}'.format(globalResource)
        time.sleep(interval)


#클래스형 쓰레드. 잘 알려진 방법으로 만들 수 있다는 것이 장점.
class Clock(threading.Thread):
    def __init__(self, interval):
        super(Clock, self).__init__()
        self.resource = 0
        self.interval = interval

    #run 프로토콜을 구현하는 것만으로 ok
    def run(self):
        while True:
            
            GPIO.output(3, False)
            #print 'this is {0}'.format(self.resource)
            time.sleep(1)
            break




while True:
#-------KEY A-------
    if GPIO.input(KEY_A) :
        if a==0 :
            a=1  
        if keyUp_a==0:
            if a==1:              
                piano_a.play() # piano_a start
                #print "a button on"
                thread = Clock(1)
                thread.demon = True
                thread.start()
                time.sleep(0.5)
                a=0
                piano_a.stop()
                print "a button off"

                

#-------KEY B-------
    if GPIO.input(KEY_B) :
        if b==0 :
            b=1
      
        if keyUp_b==0:
            if b==1:
                
                piano_b.play() # piano_b start
                print "b button on"
                time.sleep(0.5)
                b=0
                piano_b.stop()
                print "b button off"

#-------KEY C-------
    if GPIO.input(KEY_C) :
        if c==0 :
            c=1
      
        if keyUp_c==0:
            if c==1:
                piano_c.play() # piano_c start
                print "c button on"
                time.sleep(0.5)
                c=0
                piano_c.stop()
                print "c button off"

#-------KEY D-------
    if GPIO.input(KEY_D) :
        if d==0 :
            d=1
      
        if keyUp_d==0:
            if d==1:
                
                 
                piano_d.play() # piano_d start
                print "d button on"
                time.sleep(0.5)
                d=0
                piano_d.stop()
                print "d button off"

#-------KEY E-------
    if GPIO.input(KEY_E) :
        if e==0 :
            e=1
      
        if keyUp_e==0:
            if e==1:
                piano_e.play() # piano_e start
                print "e button on"
                time.sleep(0.5)
                e=0
                piano_e.stop()
                print "e button off"

#-------KEY F-------
    if GPIO.input(KEY_F) :
        if f==0 :
            f=1
      
        if keyUp_f==0:
            if f==1:
                piano_f.play() # piano_f start
                print "f button on"
                time.sleep(0.5)
                f=0
                piano_f.stop()
                print "f button off"

#-------KEY G-------
    if GPIO.input(KEY_G) :
        if g==0 :
            g=1
      
        if keyUp_g==0:
            if g==1:
                piano_g.play() # piano_g start
                print "g button on"
                time.sleep(0.5)
                g=0
                piano_g.stop()
                print "g button off"

#-------KEY H-------
    if GPIO.input(KEY_H) :
        if h==0 :
            h=1
      
        if keyUp_h==0:
            if h==1:
                piano_h.play() # piano_h start
                print "h button on"
                time.sleep(0.5)
                h=0
                piano_h.stop()
                print "h button off"

#-------KEY I-------
    if GPIO.input(KEY_I) :
        if i==0 :
            i=1
      
        if keyUp_i==0:
            if i==1:
                piano_i.play() # piano_i start
                print "i button on"
                time.sleep(10)
                i=0
                piano_i.stop()
                print "i button off"
