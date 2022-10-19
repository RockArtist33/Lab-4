####################################### Imports
from msilib.schema import Upgrade
import pygame
from pygame import mixer
mixer.init()
import sys , os
import time
import random
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
upgradeprice1 = (50*upgrademult1)
upgradeprice2 = (300*upgrademult2)
upgradeprice3 = (1000*upgrademult3)
upgradeprice4 = (1500*upgrademult4)
upgradeprice5 = (3000*upgrademult5)
upgradeprice6 = (10000*upgrademult6)
####################################### Clicker upgrades
clickermult1 = 1
clickermult2 = 1
clickermult3 = 1
clickermult4 = 1
clickermult5 = 1
#---------------------------------------#
clickerprice1 = (1000*clickermult1)
clickerprice2 = (10000*clickermult2)
clickerprice3 = (50000*clickermult3)
clickerprice4 = (100000*clickermult4)
clickerprice5 = (200000*clickermult5)
####################################### Upgrade functions

def Text_create(txt,color_of_text, rect_area_color, font_size, pos_x, pos_y):
    pixel_font = pygame.font.Font('./assets/Font/fffforward.ttf',font_size)
    pixel_text = pixel_font.render(txt, True, color_of_text, rect_area_color)
    pixel_txt_Rect = pixel_text.get_rect()
    pixel_txt_Rect.center = (pos_x,pos_y)
    screen.blit(pixel_text,pixel_txt_Rect)



def upgrade1():
    cant = False
    global Counter_num
    global Counter_auto
    global upgrademult1
    if Counter_num >= upgradeprice1:
        math = Counter_num - upgradeprice1
        Counter_num = math
        Counter_auto += 0.01
        upgrademult1 += 0.15
        print(Counter_num)
        print(Counter_auto)
        print(upgrademult1)
        print(upgradeprice1)
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
        Counter_auto += 0.05
        upgrademult2 += 0.18
        print(Counter_num)
        print(Counter_auto)
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
        Counter_auto += 0.5
        upgrademult3 += 0.3
        print(Counter_num)
        print(Counter_auto)
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
        Counter_auto += 1.5
        upgrademult4 += 0.6
        print(Counter_num)
        print(Counter_auto)
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
        Counter_auto += 10
        upgrademult5 += 0.4
        print(Counter_num)
        print(Counter_auto)
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
        Counter_auto += 100
        upgrademult6 += 0.4
        print(Counter_num)
        print(Counter_auto)
    else:
        cant = True
    return cant
        

####################################### Clicker functions
def clicker1():
    global Counter_num
    global Counter_click
    if Counter_num >= clickerprice1:
        Counter_num - clickerprice1
        Counter_click = 10
        print(Counter_num)
        print(Counter_click)
    else:
        print("You do not have enough money")
        
        
def clicker2():
    global Counter_num
    global Counter_click
    if Counter_num >= clickerprice2:
        Counter_num - clickerprice2
        Counter_click = 50
        print(Counter_num)
        print(Counter_click)
    else:
        print("You do not have enough money")
        
def clicker3():
    global Counter_num
    global Counter_click
    if Counter_num >= clickerprice3:
        Counter_num - clickerprice3
        Counter_click = 100
        print(Counter_num)
        print(Counter_click)
    else:
        print("You do not have enough money")
        
def clicker4():
    global Counter_num
    global Counter_click
    if Counter_num >= clickerprice4:
        Counter_num - clickerprice4
        Counter_click = 500
        print(Counter_num)
        print(Counter_click)
    else:
        print("You do not have enough money")
        
def clicker5():
    global Counter_num
    global Counter_click
    if Counter_num >= clickerprice5:
        Counter_num - clickerprice5
        Counter_click = 1000
        print(Counter_num)
        print(Counter_click)
    else:
        print("You do not have enough money")        

pygame.mixer.set_num_channels(100)


####################################### Calling assets
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
cap_ryan_1 = pygame.mixer.music.load(os.path.join("./assets/audio/capitalism/cap_ryan_1.mp3")) 
cap_ryan_2 = pygame.mixer.music.load(os.path.join("./assets/audio/capitalism/cap_ryan_2.mp3"))
cap_ryan_3 = pygame.mixer.music.load(os.path.join("./assets/audio/capitalism/cap_ryan_3.mp3"))
cap_ryan_4_noyay = pygame.mixer.music.load(os.path.join("./assets/audio/capitalism/cap_ryan_4_noyay.mp3"))
cap_ryan_4_yay = pygame.mixer.music.load(os.path.join("./assets/audio/capitalism/cap_ryan_4_yay.mp3"))
cap_ryan_5 = pygame.mixer.music.load(os.path.join("./assets/audio/capitalism/cap_ryan_5.mp3"))
cap_ryan_6 = pygame.mixer.music.load(os.path.join("./assets/audio/capitalism/cap_ryan_6.mp3"))
cap_ryan_7 = pygame.mixer.music.load(os.path.join("./assets/audio/capitalism/cap_ryan_7.mp3"))

print_audio = ["./assets/audio/printer/printer_1.mp3",
               "./assets/audio/printer/printer_2.mp3",
               "./assets/audio/printer/printer_3.mp3",
               "./assets/audio/printer/printer_4.mp3",
               "./assets/audio/printer/printer_5.mp3"]

pygame.init()
screen_size = (1200,900)
screen = pygame.display.set_mode(screen_size)
white = (255,255,255)
black = (0,0,0)
dark_grey = (32,33,33)
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



def play_audio(audio_list, item):
    s = pygame.mixer.Sound(os.path.join(audio_list[item]))
    emptychannel = mixer.find_channel()
    emptychannel.set_volume(0.2)
    emptychannel.play(s)

def auto_click():
    global Counter_num, Counter_click
    time.sleep(0.1)
    Counter_num = Counter_num + Counter_auto

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
        #pygame.draw.rect(screen,button_color,[place_x,place_y,size_x,size_y])
        bttn = pygame.Surface((size_x, size_y))
        bttn.set_alpha(transparency)
        bttn.fill((button_color))
        screen.blit(bttn, (place_x,place_y))
        
        return int(place_x),int(place_y),int(size_x),int(size_y)

    def circle(screen, colour_circle, center_location, radius, width_of_line,top_left,top_right,bottom_left,bottom_right):
        pygame.draw.circle(screen,colour_circle,center_location, radius, width_of_line,top_left,top_right,bottom_left,bottom_right)
        return radius
        






def start_menu():
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
    

def shop():
    global printer, background, upgradeprice1,upgradeprice2,upgradeprice3,upgradeprice4,upgradeprice5,upgradeprice6
    active = True
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
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                global Counter_num
                
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
                    mixer.music.set_volume(1); mixer.music.play()  
                    upgradeprice3 = (1000*upgrademult3)
                elif Upgrade4 <= mouse_pos[0] <= (Upgrade4+sizex_4) and starty_4 <= mouse_pos[1] <= starty_4+sizey_4:
                    cant1 = upgrade4()
                    start_time = pygame.time.get_ticks()
                    mixer.music.set_volume(1); mixer.music.play()  
                    upgradeprice4 = (1500*upgrademult4)
                elif Upgrade5 <= mouse_pos[0] <= (Upgrade5+sizex_5) and starty_5 <= mouse_pos[1] <= starty_5+sizey_5:
                    cant1 = upgrade5()
                    start_time = pygame.time.get_ticks()
                    mixer.music.set_volume(1); mixer.music.play()  
                    upgradeprice5 = (3000*upgrademult5)
                elif Upgrade6 <= mouse_pos[0] <= (Upgrade6+sizex_6) and starty_6 <= mouse_pos[1] <= starty_6+sizey_6:
                    cant1 = upgrade6()
                    start_time = pygame.time.get_ticks()
                    mixer.music.set_volume(1); mixer.music.play()  
                    upgradeprice6 = (10000*upgrademult6)
                elif 0 <= mouse_pos[0] <= 100 and 800 <= mouse_pos[1] <= 900:
                    main_loop()
        global printer 
        
        mouse_pos = pygame.mouse.get_pos()

        Upgrade1, starty_1, sizex_1, sizey_1 = Button_make.button(475,100,250,125,0, picupgrade1)
        Upgrade2, starty_2, sizex_2, sizey_2 = Button_make.button(475,230,250,125,0, picupgrade2)
        Upgrade3, starty_3, sizex_3, sizey_3 = Button_make.button(475,360,250,125,0, picupgrade3)
        Upgrade4, starty_4, sizex_4, sizey_4 = Button_make.button(475,490,250,125,0, picupgrade4)
        Upgrade5, starty_5, sizex_5, sizey_5 = Button_make.button(475,620,250,125,0, picupgrade5)
        Upgrade6, starty_6, sizex_6, sizey_6 = Button_make.button(475,750,250,125,0, picupgrade6)
        counterup1 = Text_create("£ "+str(f"{upgradeprice1:.2f}"), white, dark_grey, 20, 600, 200)
        counterup2 = Text_create("£ "+str(f"{upgradeprice2:.2f}"), white, dark_grey, 20, 600, 330)
        counterup3 = Text_create("£ "+str(f"{upgradeprice3:.2f}"), white, dark_grey, 20, 600, 460)
        counterup4 = Text_create("£ "+str(f"{upgradeprice4:.2f}"), white, dark_grey, 20, 600, 590)
        counterup5 = Text_create("£ "+str(f"{upgradeprice5:.2f}"), white, dark_grey, 20, 600, 720)
        counterup6 = Text_create("£ "+str(f"{upgradeprice6:.2f}"), white, dark_grey, 20, 600, 850)
        shop_clicker_text = Text_create("Clicker Upgrades", white, black, 20, 170, 100)
        clickerup1 = Button_make.circle(screen,dark_grey,(120,200),50,50,True,True,True,True)
        clickerup2 = Button_make.circle(screen,dark_grey,(120,325),50,50,True,True,True,True)
        clickerup3 = Button_make.circle(screen,dark_grey,(120,450),50,50,True,True,True,True)
        clickerup4 = Button_make.circle(screen,dark_grey,(120,575),50,50,True,True,True,True)
        clickerup5 = Button_make.circle(screen,dark_grey,(120,700),50,50,True,True,True,True)
        Counter_Text = Text_create("Money amount = £"+str(f"{Counter_num:.2f}"), white, black, 20, 198, 25)
        shop_text = Text_create("The SHOP", white, black, 40, 600, 50)
        y = 0
        
        if cant1 == True:
            print(pygame.time.get_ticks() - start_time)
            Text_create("NOT ENOUGH MONEY!!!", white, black, 60, 600,450)
            if start_time and pygame.time.get_ticks() - start_time > 3000:
                cant1 = False
         
        pygame.display.update()
        dt = clock.tick(60)


#Main loop
def main_loop():
    global printer, background, upgradeprice1,upgradeprice2,upgradeprice3,upgradeprice4,upgradeprice5,upgradeprice6
    active = True
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
                global Counter_num
                if startx <= mouse_pos[0] <= (startx+sizex) and starty <= mouse_pos[1] <= (starty+sizey):
                    Counter_num = Counter_num + Counter_click
                    play_audio(print_audio, random.randint(0,4))
                elif Upgrade1 <= mouse_pos[0] <= (Upgrade1+sizex_1) and starty_1 <= mouse_pos[1] <= starty_1+sizey_1:
                    cant1 = upgrade1()
                    start_time = pygame.time.get_ticks()
                    mixer.music.set_volume(1); mixer.music.play()   
                    upgradeprice1 = (50*upgrademult1)
                elif Upgrade2 <= mouse_pos[0] <= (Upgrade2+sizex_2) and starty_2 <= mouse_pos[1] <= starty_2+sizey_2:
                    cant1 = upgrade2()
                    start_time = pygame.time.get_ticks()  
                    upgradeprice2 = (300*upgrademult2)
                elif Upgrade3 <= mouse_pos[0] <= (Upgrade3+sizex_3) and starty_3 <= mouse_pos[1] <= starty_3+sizey_3:
                    cant1 = upgrade3()
                    start_time = pygame.time.get_ticks()
                    mixer.music.set_volume(1); mixer.music.play()  
                    upgradeprice3 = (1000*upgrademult3)
                elif Upgrade4 <= mouse_pos[0] <= (Upgrade4+sizex_4) and starty_4 <= mouse_pos[1] <= starty_4+sizey_4:
                    cant1 = upgrade4()
                    start_time = pygame.time.get_ticks()
                    mixer.music.set_volume(1); mixer.music.play()  
                    upgradeprice4 = (1500*upgrademult4)
                elif Upgrade5 <= mouse_pos[0] <= (Upgrade5+sizex_5) and starty_5 <= mouse_pos[1] <= starty_5+sizey_5:
                    cant1 = upgrade5()
                    start_time = pygame.time.get_ticks()
                    mixer.music.set_volume(1); mixer.music.play()  
                    upgradeprice5 = (3000*upgrademult5)
                elif Upgrade6 <= mouse_pos[0] <= (Upgrade6+sizex_6) and starty_6 <= mouse_pos[1] <= starty_6+sizey_6:
                    cant1 = upgrade6()
                    start_time = pygame.time.get_ticks()
                    mixer.music.set_volume(1); mixer.music.play()  
                    upgradeprice6 = (10000*upgrademult6)
                
                elif 0 <= mouse_pos[0] <= 100 and 800 <= mouse_pos[1] <= 900:
                    shop()
        global printer 
        
        mouse_pos = pygame.mouse.get_pos()
        startx, starty, sizex, sizey = Button_make.button(50,50,500,500,0, printer)

        Upgrade1, starty_1, sizex_1, sizey_1 = Button_make.button(875,25,200,100,0, picupgrade1)
        Upgrade2, starty_2, sizex_2, sizey_2 = Button_make.button(875,125,200,100,0, picupgrade2)
        Upgrade3, starty_3, sizex_3, sizey_3 = Button_make.button(875,225,200,100,0, picupgrade3)
        Upgrade4, starty_4, sizex_4, sizey_4 = Button_make.button(875,325.5,200,100,0, picupgrade4)
        Upgrade5, starty_5, sizex_5, sizey_5 = Button_make.button(875,425,200,100,0, picupgrade5)
        Upgrade6, starty_6, sizex_6, sizey_6 = Button_make.button(875,525.5,200,100,0, picupgrade6)
        counterup1 = Text_create("£ "+str(f"{upgradeprice1:.2f}"), white, dark_grey, 20, 976, 106)
        counterup2 = Text_create("£ "+str(f"{upgradeprice2:.2f}"), white, dark_grey, 20, 976, 206)
        counterup3 = Text_create("£ "+str(f"{upgradeprice3:.2f}"), white, dark_grey, 20, 976, 306)
        counterup4 = Text_create("£ "+str(f"{upgradeprice4:.2f}"), white, dark_grey, 20, 976, 406)
        counterup5 = Text_create("£ "+str(f"{upgradeprice5:.2f}"), white, dark_grey, 20, 976, 506)
        counterup6 = Text_create("£ "+str(f"{upgradeprice6:.2f}"), white, dark_grey, 20, 976, 606)
        clickerup1 = Button_make.circle(screen,dark_grey,(50,850),50,50,True,True,True,True)
        clickerup2 = Button_make.circle(screen,dark_grey,(150,850),50,50,True,True,True,True)
        clickerup3 = Button_make.circle(screen,dark_grey,(250,850),50,50,True,True,True,True)
        clickerup4 = Button_make.circle(screen,dark_grey,(350,850),50,50,True,True,True,True)
        clickerup5 = Button_make.circle(screen,dark_grey,(450,850),50,50,True,True,True,True)
        Counter_Text = Text_create("Money amount = £"+str(f"{Counter_num:.2f}"), white, black, 20, 198, 25)
        y = 0
        
        if cant1 == True:
            print(pygame.time.get_ticks() - start_time)
            Text_create("NOT ENOUGH MONEY!!!", white, black, 60, 600,450)
            if start_time and pygame.time.get_ticks() - start_time > 3000:
                cant1 = False
         
        pygame.display.update()
        dt = clock.tick(60)
 


start_menu()

