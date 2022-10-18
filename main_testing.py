import pygame
import sys , os
import time



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
upgradeprice1 = (100*upgrademult1)
upgradeprice2 = (1000*upgrademult2)
upgradeprice3 = (20000*upgrademult3)
upgradeprice4 = (50000*upgrademult4)
upgradeprice5 = (100000*upgrademult5)
upgradeprice6 = (150000*upgrademult6)
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
def upgrade1():
    global Counter_num
    global Counter_auto
    if Counter_num >= upgradeprice1:
        math = Counter_num - upgradeprice1
        Counter_num = math
        Counter_auto += 0.01
        print(Counter_num)
        print(Counter_auto)
        
def upgrade2():
    global Counter_num
    global Counter_auto
    if Counter_num >= upgradeprice2:
        math = Counter_num - upgradeprice2
        Counter_num = math
        Counter_auto += 0.05
        print(Counter_num)
        print(Counter_auto)
        
def upgrade3():
    global Counter_num
    global Counter_auto
    if Counter_num >= upgradeprice3:
        math = Counter_num - upgradeprice3
        Counter_num = math
        Counter_auto += 0.5
        print(Counter_num)
        print(Counter_auto)
        
def upgrade4():
    global Counter_num
    global Counter_auto
    if Counter_num >= upgradeprice4:
        math = Counter_num - upgradeprice4
        Counter_num = math
        Counter_auto += 1.5
        print(Counter_num)
        print(Counter_auto)
        
def upgrade5():
    global Counter_num
    global Counter_auto
    if Counter_num >= upgradeprice5:
        math = Counter_num - upgradeprice5
        Counter_num = math
        Counter_auto += 10
        print(Counter_num)
        print(Counter_auto)
        
def upgrade6():
    global Counter_num
    global Counter_auto
    if Counter_num >= upgradeprice6:
        math = Counter_num - upgradeprice6
        Counter_num = math
        Counter_auto += 100
        print(Counter_num)
        print(Counter_auto)
        

####################################### Clicker functions
def clicker1():
    global Counter_num
    global Counter_click
    if Counter_num >= clickerprice1:
        Counter_num - clickerprice1
        Counter_click = 10
        print(Counter_num)
        print(Counter_click)
        
def clicker2():
    global Counter_num
    global Counter_click
    if Counter_num >= clickerprice2:
        Counter_num - clickerprice2
        Counter_click = 50
        print(Counter_num)
        print(Counter_click)
        
def clicker3():
    global Counter_num
    global Counter_click
    if Counter_num >= clickerprice3:
        Counter_num - clickerprice3
        Counter_click = 100
        print(Counter_num)
        print(Counter_click)
        
def clicker4():
    global Counter_num
    global Counter_click
    if Counter_num >= clickerprice4:
        Counter_num - clickerprice4
        Counter_click = 500
        print(Counter_num)
        print(Counter_click)
        
def clicker5():
    global Counter_num
    global Counter_click
    if Counter_num >= clickerprice5:
        Counter_num - clickerprice5
        Counter_click = 1000
        print(Counter_num)
        print(Counter_click)        

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


pygame.init()
screen_size = (800,600)
screen = pygame.display.set_mode(screen_size)
white = (255,255,255)
black = (0,0,0)
dark_grey = (40,40,40)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
color_light = (170,170,170)
color_dark = (100,100,100)
width = screen.get_width()
height = screen.get_height()
price = (10*Price_inc)
y = 0

def Text_create(txt,color_of_text, rect_area_color, font_size, pos_x, pos_y):
    pixel_font = pygame.font.Font('./assets/Font/fffforward.ttf',font_size)
    pixel_text = pixel_font.render(txt, True, color_of_text, rect_area_color)
    pixel_txt_Rect = pixel_text.get_rect()
    pixel_txt_Rect.center = (pos_x,pos_y)
    screen.blit(pixel_text, pixel_txt_Rect)

def auto_click():
    global Counter_num, Counter_click
    time.sleep(0.1)
    Counter_num = Counter_num + Counter_auto

active = True
class Button_make:

    def button(button_color,place_x,place_y,size_x,size_y,transparency):
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
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active == False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
    
    screen.fill(dark_grey)
    
        
        
        
#Main loop
def main_loop():
    global printer, Counter_num, Counter_click, price
    active = True
    while active:
        if active:
            auto_click()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                global Counter_num
                if startx <= mouse_pos[0] <= (startx+sizex) and starty <= mouse_pos[1] <= (starty+sizey):
                    Counter_num = Counter_num + Counter_click
            
                elif Upgrade1 <= mouse_pos[0] <= (Upgrade1+sizex_1) and starty_1 <= mouse_pos[1] <= starty_1+sizey_1:
                    upgrade1()
                elif Upgrade2 <= mouse_pos[0] <= (Upgrade2+sizex_2) and starty_2 <= mouse_pos[1] <= starty_2+sizey_2:
                    upgrade2()
                elif Upgrade3 <= mouse_pos[0] <= (Upgrade3+sizex_3) and starty_3 <= mouse_pos[1] <= starty_3+sizey_3:
                    upgrade3()
                elif Upgrade4 <= mouse_pos[0] <= (Upgrade4+sizex_4) and starty_4 <= mouse_pos[1] <= starty_4+sizey_4:
                    upgrade4()
                elif Upgrade5 <= mouse_pos[0] <= (Upgrade5+sizex_5) and starty_5 <= mouse_pos[1] <= starty_5+sizey_5:
                    upgrade5()
                elif Upgrade6 <= mouse_pos[0] <= (Upgrade6+sizex_6) and starty_6 <= mouse_pos[1] <= starty_6+sizey_6:
                    upgrade6()
            
                
        global printer 
        screen.blit(background,(0,0)) 
        mouse_pos = pygame.mouse.get_pos()
        startx, starty, sizex, sizey = Button_make.button(dark_grey,50,50,200,200,160)
        printer = pygame.transform.scale(printer,(sizex, sizey))
        picupgrade1 = pygame.transform.scale(picupgrade1,(sizex, sizey))
        picupgrade2 = pygame.transform.scale(picupgrade2,(sizex, sizey))
        picupgrade3 = pygame.transform.scale(picupgrade3,(sizex, sizey))
        picupgrade4 = pygame.transform.scale(picupgrade4,(sizex, sizey))
        picupgrade5 = pygame.transform.scale(picupgrade5,(sizex, sizey))
        picupgrade6 = pygame.transform.scale(picupgrade6,(sizex, sizey))
        screen.blit(printer,(startx, starty),)
        screen.blit(picupgrade1,(startx, starty),)
        screen.blit(picupgrade2,(startx, starty),)
        screen.blit(picupgrade3,(startx, starty),)
        screen.blit(picupgrade4,(startx, starty),)
        screen.blit(picupgrade5,(startx, starty),)
        screen.blit(picupgrade6,(startx, starty),)
        Upgrade1, starty_1, sizex_1, sizey_1 = Button_make.button(dark_grey,575,25,200,65,128)
        Upgrade2, starty_2, sizex_2, sizey_2 = Button_make.button(dark_grey,575,112.5,200,65,128)
        Upgrade3, starty_3, sizex_3, sizey_3 = Button_make.button(dark_grey,575,200,200,65,128)
        Upgrade4, starty_4, sizex_4, sizey_4 = Button_make.button(dark_grey,575,287.5,200,65,128)
        Upgrade5, starty_5, sizex_5, sizey_5 = Button_make.button(dark_grey,575,375,200,65,128)
        Upgrade6, starty_6, sizex_6, sizey_6 = Button_make.button(dark_grey,575,462.5,200,65,128)
        radius1 = Button_make.circle(screen,dark_grey,(400,600),50,48,True,True,True,True)
        Counter_Text = Text_create("Money amount = £"+str(f"{Counter_num:.2f}"), white, black, 20, 198, 275)
        y = 0
        pygame.display.update()
 


main_loop()