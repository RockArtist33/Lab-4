####################################### Imports
from msilib.schema import Upgrade
import pygame
from pygame import mixer # Audio
mixer.init()
import sys , os
import time # Currently goes unused
import random # Random audio file played 
import json
import pickle
####################################### main storage
Counter_num = 0
Counter_auto = 0    
Counter_click = 1
Counter_mult = 1.0
Price_inc = 1.0
####################################### normal upgrades
upgrademult1 = 1
upgrademult2 = 1
upgrademult3 = 1
upgrademult4 = 1
upgrademult5 = 1
upgrademult6 = 1
#---------------------------------------# 
upgradeprice1 = 50
upgradeprice2 = 300
upgradeprice3 = 1000
upgradeprice4 = 10000
upgradeprice5 = 25000
upgradeprice6 = 100000
####################################### Clicker upgrades
clickerprice1 = 1000
clickerprice2 = 2500
clickerprice3 = 50000
clickerprice4 = 100000
clickerprice5 = 200000
background = pygame.image.load(os.path.join("./assets/images/Backround.png"))
printer = pygame.image.load(os.path.join("./assets/images/Printer.png"))
moneyicon = pygame.image.load(os.path.join("./assets/images/Money-icon.png"))
mouse1 = pygame.image.load(os.path.join("./assets/images/mouse1.png"))
mouse2 = pygame.image.load(os.path.join("./assets/images/mouse2.png"))
mouse3 = pygame.image.load(os.path.join("./assets/images/mouse3.png"))
mouse4 = pygame.image.load(os.path.join("./assets/images/mouse4.png"))
mouse5 = pygame.image.load(os.path.join("./assets/images/mouse5.png"))
picupgrade1 = pygame.image.load(os.path.join("./assets/images/upgrade1.png"))
picupgrade2 = pygame.image.load(os.path.join("./assets/images/upgrade2.png"))
picupgrade3 = pygame.image.load(os.path.join("./assets/images/upgrade3.png"))
picupgrade4 = pygame.image.load(os.path.join("./assets/images/upgrade4.png"))
picupgrade5 = pygame.image.load(os.path.join("./assets/images/upgrade5.png"))
picupgrade6 = pygame.image.load(os.path.join("./assets/images/upgrade6.png"))
exitsign = pygame.image.load(os.path.join("./assets/images/exit.png"))
shopsign = pygame.image.load(os.path.join("./assets/images/shop.png"))
cap_swosh = pygame.mixer.Sound(os.path.join("./assets/audio/music/Swish_Swosh_loop.mp3"))
cap_person = pygame.mixer.Sound(os.path.join("./assets/audio/music/Nice_Person_loop.mp3"))
cap_ryan_1 = pygame.mixer.Sound(os.path.join("./assets/audio/capitalism/cap_ryan_1.mp3")) 
cap_ryan_2 = pygame.mixer.Sound(os.path.join("./assets/audio/capitalism/cap_ryan_2.mp3")) 
cap_ryan_3 = pygame.mixer.Sound(os.path.join("./assets/audio/capitalism/cap_ryan_3.mp3"))
cap_ryan_4_noyay = pygame.mixer.Sound(os.path.join("./assets/audio/capitalism/cap_ryan_4_noyay.mp3"))
cap_ryan_4_yay = pygame.mixer.Sound(os.path.join("./assets/audio/capitalism/cap_ryan_4_yay.mp3"))
cap_ryan_5 = pygame.mixer.Sound(os.path.join("./assets/audio/capitalism/cap_ryan_5.mp3"))
cap_ryan_6 = pygame.mixer.Sound(os.path.join("./assets/audio/capitalism/cap_ryan_6.mp3"))
cap_ryan_7 = pygame.mixer.Sound(os.path.join("./assets/audio/capitalism/cap_ryan_7.mp3"))
#pop_1 = pygame.mixer.music.load(os.path.join("./assets/audio/pop/pop_1"))
#pop_1 = pygame.mixer.music.load(os.path.join("./assets/audio/pop/pop_1")) 
#pop_1 = pygame.mixer.music.load(os.path.join("./assets/audio/pop/pop_1"))  
#pop_1 = pygame.mixer.music.load(os.path.join("./assets/audio/pop/pop_1"))    
#pop_1 = pygame.mixer.music.load(os.path.join("./assets/audio/pop/pop_1") ) 
print_1 = pygame.mixer.Sound(os.path.join("./assets/audio/printer/print_1.mp3"))
print_2 = pygame.mixer.Sound(os.path.join("./assets/audio/printer/print_2.mp3"))
print_3 = pygame.mixer.Sound(os.path.join("./assets/audio/printer/print_3.mp3"))
frameback = pygame.image.load(os.path.join("./assets/images/frameback.png"))
cap_ryan_sounds = ["./assets/audio/capitalism/cap_ryan_1.mp3",
                   "./assets/audio/capitalism/cap_ryan_2.mp3",
                   "./assets/audio/capitalism/cap_ryan_3.mp3",
                   "./assets/audio/capitalism/cap_ryan_4_noyay.mp3",
                   "./assets/audio/capitalism/cap_ryan_4_yay.mp3",
                   "./assets/audio/capitalism/cap_ryan_5.mp3",
                   "./assets/audio/capitalism/cap_ryan_6.mp3",
                   "./assets/audio/capitalism/cap_ryan_7.mp3"
                   ]
ding = ["./assets/audio/printer/ding.mp3"]
print_audio = ["./assets/audio/printer/print_1.mp3",
             "./assets/audio/printer/print_2.mp3",
             "./assets/audio/printer/print_3.mp3"]
pop_audio = ["./assets/audio/pop/pop_1.mp3", #MAY
             "./assets/audio/pop/pop_2.mp3", #GO
             "./assets/audio/pop/pop_3.mp3", #UNUSED
             "./assets/audio/pop/pop_4.mp3", #BRUH
             "./assets/audio/pop/pop_5.mp3",]
pygame.mixer.set_num_channels(100)
pygame.mixer.set_reserved(1)
####################################### Upgrade functions

def Text_create(txt,color_of_text, rect_area_color, font_size, pos_x, pos_y):
    pixel_font = pygame.font.Font('./assets/Font/fffforward.ttf',font_size)
    pixel_text = pixel_font.render(txt, True, color_of_text)
    pixel_txt_Rect = pixel_text.get_rect()
    pixel_txt_Rect.center = (pos_x,pos_y)
    screen.blit(pixel_text,pixel_txt_Rect)

def play_audio(audio_list, item):
    s = pygame.mixer.Sound(os.path.join(audio_list[item]))
    emptychannel = mixer.find_channel()
    emptychannel.set_volume(0.3)
    emptychannel.play(s)


def upgrade1():
    cant = False
    global Counter_num
    global Counter_auto
    global upgrademult1
    if Counter_num >= upgradeprice1:
        math = Counter_num - upgradeprice1
        Counter_num = math
        Counter_auto += 0.25
        upgrademult1 += 0.18
        print(Counter_num)
        print(Counter_auto)
        print(upgrademult1)
        print(upgradeprice1)
        play_audio(pop_audio, random.randint(0,4))
    else:
        cant = True
    return cant
        
def upgrade2():
    cant = False
    global Counter_num
    global Counter_auto
    global upgrademult2
    if Counter_num >= upgradeprice2:
        math = Counter_num - upgradeprice2
        Counter_num = math
        Counter_auto += 1
        upgrademult2 += 0.3
        print(Counter_num)
        print(Counter_auto)
        play_audio(pop_audio, random.randint(0,4))
    else:
        cant = True
    return cant
        
def upgrade3():
    cant = False
    global Counter_num
    global Counter_auto
    global upgrademult3
    if Counter_num >= upgradeprice3:
        math = Counter_num - upgradeprice3
        Counter_num = math
        Counter_auto +=15
        upgrademult3 += 0.4
        print(Counter_num)
        print(Counter_auto)
        play_audio(pop_audio, random.randint(0,4))
    else:
        cant = True
    return cant
        
def upgrade4():
    cant = False
    global Counter_num
    global upgrademult4
    global Counter_auto
    if Counter_num >= upgradeprice4:
        math = Counter_num - upgradeprice4
        Counter_num = math
        Counter_auto += 100
        upgrademult4 += 0.7
        print(Counter_num)
        print(Counter_auto)
        play_audio(pop_audio, random.randint(0,4))
    else:
        cant = True
    return cant
        
def upgrade5():
    cant = False
    global Counter_num
    global Counter_auto
    global upgrademult5
    if Counter_num >= upgradeprice5:
        math = Counter_num - upgradeprice5
        Counter_num = math
        Counter_auto += 500
        upgrademult5 += 1.7
        print(Counter_num)
        print(Counter_auto)
        play_audio(pop_audio, random.randint(0,4))
    else:
        cant = True
    return cant
        
def upgrade6():
    cant = False
    global Counter_num
    global Counter_auto
    global upgrademult6
    if Counter_num >= upgradeprice6:
        math = Counter_num - upgradeprice6
        Counter_num = math
        Counter_auto += 1000
        upgrademult6 += 2.8
        print(Counter_num)
        print(Counter_auto)
        play_audio(pop_audio, random.randint(0,4))
    else:
        cant = True
    return cant
        

####################################### Clicker functions
def clicker1():
    cant = False
    global Counter_num
    global Counter_click
    if Counter_num >= clickerprice1:
        Counter_num = Counter_num - clickerprice1
        Counter_click = 10
        print(Counter_num)
        print(Counter_click)
        play_audio(pop_audio, random.randint(0,4))
        cant = False
        print("1")
    else:
        cant = True
        print("2")
    return cant
        
def clicker2():
    cant = False
    global Counter_num
    global Counter_click
    if Counter_num >= clickerprice2:
        Counter_num = Counter_num - clickerprice2
        Counter_click = 50
        print(Counter_num)
        print(Counter_click)
        play_audio(pop_audio, random.randint(0,4))
        cant = False
    else:
        cant = True
    return cant

def clicker3():
    cant = False
    global Counter_num
    global Counter_click
    if Counter_num >= clickerprice3:
        Counter_num = Counter_num - clickerprice3
        Counter_click = 100
        print(Counter_num)
        print(Counter_click)
        play_audio(pop_audio, random.randint(0,4))
        cant = False
    else:
        cant = True
    return cant
def clicker4():
    cant = False
    global Counter_num
    global Counter_click
    if Counter_num >= clickerprice4:
        Counter_num = Counter_num - clickerprice4
        Counter_click = 500
        print(Counter_num)
        print(Counter_click)
        play_audio(pop_audio, random.randint(0,4))
        cant = False
    else:
        cant = True
    return cant

def clicker5():
    cant = False
    global Counter_num
    global Counter_click
    if Counter_num >= clickerprice5:
        Counter_num = Counter_num - clickerprice5
        Counter_click = 1000
        print(Counter_num)
        print(Counter_click)
        play_audio(pop_audio, random.randint(0,4))
        cant = False
    else:
        cant = True
    return cant


####################################### Initalise Pygame window
pygame.init()
screen_size = (1200,900)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Capitalism")
pygame.display.set_icon(moneyicon)
white = (255,255,255)
black = (0,0,0)
dark_grey = (32,33,33)
darker_grey = (22,23,23)
light_grey = (80,80,80)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
color_light = (170,170,170)
color_dark = (100,100,100)
width = screen.get_width()
height = screen.get_height()
price = (10*Price_inc)
y = 0
bought = True
cant_buy1 = True
cant_buy2 = True
cant_buy3 = True
cant_buy4 = True
cant_buy5 = True
cant_buy6 = True





####################################### this function is the money per seconds 
def auto_click():
    global Counter_num, Counter_click
    time.sleep(0.1)
    Counter_num = Counter_num + Counter_auto
####################################### all this does is create so called templates
active = True
class Button_make:

    def button(place_x,place_y,size_x,size_y,transparency,picture):
        #pygame.draw.rect(screen,button_color,[place_x,place_y,size_x,size_y])
        bttn = pygame.Surface((size_x, size_y))
        bttn.set_alpha(transparency)
        picture = pygame.transform.scale(picture, (size_x,size_y))
        screen.blit(picture, (place_x, place_y))
        screen.blit(bttn, (place_x,place_y))
        
        return int(place_x),int(place_y),int(size_x),int(size_y)
    
    def button_fill(button_color,place_x,place_y,size_x,size_y,transparency):
        pygame.draw.rect(screen,button_color,[place_x,place_y,size_x,size_y])
        bttn = pygame.Surface((size_x, size_y))
        bttn.set_alpha(transparency)
        bttn.fill((button_color))
        screen.blit(bttn, (place_x,place_y))

        
        return int(place_x),int(place_y),int(size_x),int(size_y)

    def circle(screen, colour_circle, x,y, radius, width_of_line,top_left,top_right,bottom_left,bottom_right, picture):
        pygame.draw.circle(screen,colour_circle,(x,y), radius-5, width_of_line,top_left,top_right,bottom_left,bottom_right)
        picture = pygame.transform.scale(picture, (radius*2+5, radius*2+5))
        screen.blit(picture, (x-50,y-50))
        return radius, x, y
        
####################################### counters for all 

def hub_ui():
    Button_make.button_fill(dark_grey,0,638,800,300,0)
    Button_make.button_fill(dark_grey,787,0,450,900,0)
    Button_make.button_fill(darker_grey,20, 660, 1160, 220, 0)
    Button_make.button_fill(darker_grey,810, 20, 370, 810, 0)
    Counter_Text = Text_create("Money = £"+str(f"{Counter_num:.2f}"), white, darker_grey, 20, 227, 700)
    Money_per_click = Text_create("Money per click: £"+str(f"{Counter_click}"), white, darker_grey, 20, 200,740)
    Money_per_second = Text_create("Money per second: £"+str(f"{Counter_auto*10}"),white,black,20,217, 780)
    shopopne, starty_7, sizex_7, sizey_7 = Button_make.button(67,800,150,75,0, shopsign)
    
def hub_ui2():
    Button_make.button_fill(dark_grey,0,638,800,300,0)
    Button_make.button_fill(dark_grey,787,0,450,900,0)
    Button_make.button_fill(dark_grey,0,0,413,900,0)
    Button_make.button_fill(darker_grey,20, 660, 1160, 220, 0)
    Button_make.button_fill(darker_grey,810, 20, 370, 810, 0)
    Button_make.button_fill(darker_grey,20, 20, 370, 810, 0)
    Counter_Text = Text_create("Money = £"+str(f"{Counter_num:.2f}"), white, darker_grey, 20, 227, 700)
    Money_per_click = Text_create("Money per click: £"+str(f"{Counter_click}"), white, darker_grey, 20, 200,740)
    Money_per_second = Text_create("Money per second: £"+str(f"{Counter_auto*10}"),white,black,20,217, 780)
    shopopne, starty_7, sizex_7, sizey_7 = Button_make.button(67,800,150,75,0, shopsign)
    
####################################### main menue

def start_menu():
    global bought, cant_buy1, cant_buy2, cant_buy3, cant_buy4, cant_buy5, cant_buy6
    x_button = 125
    y_button = 60
    active = True
    
    while active:
        mouse_pos1 = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if x_pos1 <= mouse_pos1[0] <= (x_pos1+x_size1) and y_pos1 <= mouse_pos1[1] <= (y_pos1+y_size1):
                    active == False
                    main_loop()
                if x_pos2 <= mouse_pos1[0] <= (x_pos2+x_size2) and y_pos2 <= mouse_pos1[1] <= (y_pos2+y_size2):
                    sys.exit()
        screen.fill(black)
        x_pos1, y_pos1, x_size1, y_size1 = Button_make.button_fill(light_grey, ((1200/2)-(x_button)/2), ((900/2)-(y_button)/2), x_button, y_button, 128)
        x_pos2, y_pos2, x_size2, y_size2 = Button_make.button_fill(light_grey, ((1200/2)-(x_button)/2), ((900/2)-(y_button)/2)+80, x_button, y_button, 128)
        Text_create("Capitalism", white,None, 40, 1200/2, 900-600)
        Text_create("START",white,None,20,x_pos1+x_size1/2, y_pos1+y_size1/2)
        Text_create("QUIT",white,None,20,x_pos1+x_size1/2, y_pos1+y_size1/2 + 80)
        
    
        print(x_pos1, y_pos1, x_size1, y_size1, mouse_pos1[0], mouse_pos1[1])
        pygame.display.update()
    
    screen.fill(dark_grey) 
    

####################################### this is the shop gui


def shop():
    global printer,Counter_num, Counter_auto,Counter_click,Counter_mult,Price_inc, background, upgradeprice1,upgradeprice2,upgradeprice3,upgradeprice4,upgradeprice5,upgradeprice6
    global bought, cant_buy1, cant_buy2, cant_buy3, cant_buy4, cant_buy5, cant_buy6
    active = True
    cant1 = False
    clock = pygame.time.Clock()
    start_time = None
    dt = 0
    background.set_alpha(180)

    while active:
        mouse_pos = pygame.mouse.get_pos()
        screen.fill(black)
        screen.blit(background,(0,0))
        if active:
            auto_click()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Upgrade1 <= mouse_pos[0] <= (Upgrade1+sizex_1) and starty_1 <= mouse_pos[1] <= starty_1+sizey_1:
                    cant1 = upgrade1()
                    start_time = pygame.time.get_ticks()
                    upgradeprice1 = (50*upgrademult1)
                elif Upgrade2 <= mouse_pos[0] <= (Upgrade2+sizex_2) and starty_2 <= mouse_pos[1] <= starty_2+sizey_2:
                    cant1 = upgrade2()
                    start_time = pygame.time.get_ticks()
                    upgradeprice2 = (300*upgrademult2)
                elif Upgrade3 <= mouse_pos[0] <= (Upgrade3+sizex_3) and starty_3 <= mouse_pos[1] <= starty_3+sizey_3:
                    cant1 = upgrade3()
                    start_time = pygame.time.get_ticks()
                    upgradeprice3 = (1000*upgrademult3)
                elif Upgrade4 <= mouse_pos[0] <= (Upgrade4+sizex_4) and starty_4 <= mouse_pos[1] <= starty_4+sizey_4:
                    cant1 = upgrade4()
                    start_time = pygame.time.get_ticks()
                    upgradeprice4 = (10000*upgrademult4)
                elif Upgrade5 <= mouse_pos[0] <= (Upgrade5+sizex_5) and starty_5 <= mouse_pos[1] <= starty_5+sizey_5:
                    cant1 = upgrade5()
                    start_time = pygame.time.get_ticks()
                    upgradeprice5 = (25000*upgrademult5)
                    
                print(x1,y1,clicker_radius1,sizey_6, mouse_pos[0],mouse_pos[1])
                if Upgrade6 <= mouse_pos[0] <= (Upgrade6+sizex_6) and starty_6 <= mouse_pos[1] <= starty_6+sizey_6: 
                    cant1 = upgrade6()
                    start_time = pygame.time.get_ticks()
                    upgradeprice6 = (100000*upgrademult6)
                elif 130 <= mouse_pos[0] <= 280 and 800 <= mouse_pos[1] <= 880:
                    main_loop()
                elif x1 - clicker_radius1 <= mouse_pos[0] <= x1+ clicker_radius1 and y1 - clicker_radius1 <= mouse_pos[1] <= y1 + clicker_radius1 and cant_buy1 == True:
                    print(cant_buy1)
                    cant1 = clicker1()
                    start_time = pygame.time.get_ticks()
                    cant_buy1 = cant1
                elif x2 - clicker_radius2 <= mouse_pos[0] <= x2+ clicker_radius2 and y2 - clicker_radius2 <= mouse_pos[1] <= y2 + clicker_radius2 and cant_buy1 == False and cant_buy2 == True:

                    cant2 = clicker2()
                    start_time = pygame.time.get_ticks()
                    cant_buy2 = cant2
                elif x3 - clicker_radius3 <= mouse_pos[0] <= x3+ clicker_radius3 and y3 - clicker_radius3 <= mouse_pos[1] <= y3 + clicker_radius3 and cant_buy1 == False and cant_buy2 == False and cant_buy3 == True:
                    cant3 = clicker3()
                    start_time = pygame.time.get_ticks()
                    cant_buy3 = cant3
                elif x4 - clicker_radius4 <= mouse_pos[0] <= x4+ clicker_radius4 and y4 - clicker_radius4 <= mouse_pos[1] <= y4 + clicker_radius4 and cant_buy1 == False and cant_buy2 == False and cant_buy3 == False and cant_buy4 == True:
                    cant4 = clicker4()
                    start_time = pygame.time.get_ticks()
                    cant_buy4 = cant4
                elif x5 - clicker_radius3 <= mouse_pos[0] <= x5+ clicker_radius5 and y5 - clicker_radius5 <= mouse_pos[1] <= y5 + clicker_radius5 and cant_buy1 == False and cant_buy2 == False and cant_buy3 == False and cant_buy4 == False and cant_buy5 == True:
                    cant5 = clicker5()
                    start_time = pygame.time.get_ticks()
                    cant_buy5 = cant5
                
        
        global printer, exitsign
        
        
 ####################################### buttons with pixtures for shop ui
 
 
        hub_ui2()
        Upgrade1, starty_1, sizex_1, sizey_1 = Button_make.button(870,60,250,125,0, picupgrade1)
        Upgrade2, starty_2, sizex_2, sizey_2 = Button_make.button(870,190,250,125,0, picupgrade2)
        Upgrade3, starty_3, sizex_3, sizey_3 = Button_make.button(870,320,250,125,0, picupgrade3)
        Upgrade4, starty_4, sizex_4, sizey_4 = Button_make.button(870,450,250,125,0, picupgrade4)
        Upgrade5, starty_5, sizex_5, sizey_5 = Button_make.button(870,580,250,125,0, picupgrade5)
        Upgrade6, starty_6, sizex_6, sizey_6 = Button_make.button(870,720,250,125,0, picupgrade6)
        shopexit, starty_7, sizex_7, sizey_7 = Button_make.button(67,800,150,75,0, exitsign)
        counterup1 = Text_create("£ "+str(f"{upgradeprice1:.2f}"), white, dark_grey, 20, 990, 160)
        counterup2 = Text_create("£ "+str(f"{upgradeprice2:.2f}"), white, dark_grey, 20, 990, 290)
        counterup3 = Text_create("£ "+str(f"{upgradeprice3:.2f}"), white, dark_grey, 20, 990, 420)
        counterup4 = Text_create("£ "+str(f"{upgradeprice4:.2f}"), white, dark_grey, 20, 990, 550)
        counterup5 = Text_create("£ "+str(f"{upgradeprice5:.2f}"), white, dark_grey, 20, 990, 680)
        counterup6 = Text_create("£ "+str(f"{upgradeprice6:.2f}"), white, dark_grey, 20, 990, 821)
        global clickerprice1
        if cant_buy1 == False:
            clickup1 = Text_create("BOUGHT", white, dark_grey, 20, 250, 120)
        else:
            clickup1 = Text_create("£ "+str(f"{clickerprice1:.2f}"), white, dark_grey, 20, 250, 120)
        if cant_buy2 == False:
            clickup2 = Text_create("BOUGHT", white, dark_grey, 20, 250, 235)
        else:
            clickup2 = Text_create("£ "+str(f"{clickerprice2:.2f}"), white, dark_grey, 20, 250, 235)
            
        if cant_buy3 == False:
            clickup3 = Text_create("BOUGHT", white, dark_grey, 20, 250, 350)
        else:
            clickup3 = Text_create("£ "+str(f"{clickerprice3:.2f}"), white, dark_grey, 20, 250, 350)
        
        if cant_buy4 == False:
            clickup4 = Text_create("BOUGHT", white, dark_grey, 20, 250, 465)
        else:
            clickup4 = Text_create("£ "+str(f"{clickerprice4:.2f}"), white, dark_grey, 20, 260, 465)
        
        if cant_buy5 == False:
            clickup5 = Text_create("BOUGHT", white, dark_grey, 20, 250, 580)
        else:
            clickup5 = Text_create("£ "+str(f"{clickerprice5:.2f}"), white, dark_grey, 20, 260, 580)
        
        clicker_radius1, x1, y1 = Button_make.circle(screen,dark_grey,120,120,50,50,True,True,True,True,mouse1)
        clicker_radius2, x2, y2 = Button_make.circle(screen,dark_grey,120,235,50,50,True,True,True,True,mouse2)
        clicker_radius3, x3, y3 = Button_make.circle(screen,dark_grey,120,350,50,50,True,True,True,True,mouse3)
        clicker_radius4, x4, y4 = Button_make.circle(screen,dark_grey,120,465,50,50,True,True,True,True,mouse4)
        clicker_radius5, x5 ,y5 = Button_make.circle(screen,dark_grey,120,580,50,50,True,True,True,True,mouse5)
        shop_clicker_text = Text_create("Clicker Upgrades", "#A3EBB1", black, 19, 200, 42)
        shop_text = Text_create("Printer Upgrades", "#A3EBB1", black, 19, 990, 42)
        shop_text = Text_create("Shop", white, black, 50, 600, 50)
        y = 0
        if cant1 == True:
            print(pygame.time.get_ticks() - start_time)
            backroundframes, starty_1, sizex_1, sizey_1 = Button_make.button(145,390,905,105, 0,frameback)
            Text_create("NOT ENOUGH MONEY!!!", white, black, 60, 600,450)
            if start_time and pygame.time.get_ticks() - start_time > 300:
                cant1 = False
        
        
        
        
        pygame.display.update()
        dt = clock.tick(60)
cap_swosh.set_volume(0.2)
pygame.mixer.Channel(1).play(cap_swosh, loops=-1)
####################################### this is the main function for the first page, aka the clicker page
def main_loop():
    global printer,Counter_num, Counter_auto,Counter_click,Counter_mult,Price_inc, background, upgradeprice1,upgradeprice2,upgradeprice3,upgradeprice4,upgradeprice5,upgradeprice6
    global bought, cant_buy1, cant_buy2, cant_buy3, cant_buy4, cant_buy5, cant_buy6
    
    active = True
    print(Counter_num,Counter_auto,Counter_click,Counter_mult,Price_inc)
    cant1 = False
    clock = pygame.time.Clock()
    start_time = None
    dt = 0
    background.set_alpha(180)
    while active:
        screen.fill(black)
        screen.blit(background,(0,0))
        if active:
            auto_click()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if startx <= mouse_pos[0] <= (startx+sizex) and starty <= mouse_pos[1] <= (starty+sizey):
                    Counter_num = Counter_num + Counter_click
                    play_audio(print_audio, random.randint(0,2))
                elif 130 <= mouse_pos[0] <= 280 and 800 <= mouse_pos[1] <= 880: 
                    shop()
        global printer 
        
        mouse_pos = pygame.mouse.get_pos()
        startx, starty, sizex, sizey = Button_make.button(120,70,500,500,0, printer)
        clickerup1 = Button_make.circle(screen,dark_grey,50,850,50,50,True,True,True,True,mouse1)
        hub_ui()
        
        y = 0
        
        if cant1 == True:
            print(pygame.time.get_ticks() - start_time)
            Counter_Text = Text_create("Money = £"+str(f"{Counter_num:.2f}"), white, black, 20, 198, 39)
            if start_time and pygame.time.get_ticks() - start_time > 300:
                cant1 = False
         
        pygame.display.update()
        dt = clock.tick(60)
 


start_menu()


#pygame.event.set_blocked(pygame.{PLEASE PUT MOUSE WHEELE HERE})
