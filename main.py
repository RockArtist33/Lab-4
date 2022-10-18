import pygame
import sys , os
import time


Counter_num = 0
Counter_auto = 0    
Counter_inc = 1
Counter_mult = 1.0
Price_inc = 1.0

printer = pygame.image.load(os.path.join("./assets/images/printer.png"))

pygame.init()
screen_size = (1024,768)
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
    global Counter_num, Counter_inc
    time.sleep(0.1)
    Counter_num = Counter_num + Counter_auto

active = True
class Button_make:

    def button(button_color,place_x,place_y,size_x,size_y):
        pygame.draw.rect(screen,button_color,[place_x,place_y,size_x,size_y])
        return int(place_x),int(place_y),int(size_x),int(size_y)

    def circle(screen, colour_circle, center_location, radius, width_of_line,top_left,top_right,bottom_left,bottom_right):
        pygame.draw.circle(screen,colour_circle,center_location, radius, width_of_line,top_left,top_right,bottom_left,bottom_right)
        return radius
        



#Main loop
while active:
    if active:
        auto_click()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if startx <= mouse_pos[0] <= (startx+sizex) and starty <= mouse_pos[1] <= (starty+sizey):
                Counter_num = Counter_num + Counter_inc
            
            elif startx_1 <= mouse_pos[0] <= (startx_1+sizex_1) and starty_1 <= mouse_pos[1] <= starty_1+sizey_1:
                Counter_auto += 0.1
            elif startx_2 <= mouse_pos[0] <= (startx_2+sizex_2) and starty_2 <= mouse_pos[1] <= starty_2+sizey_2:
                print("hello2")
            elif startx_3 <= mouse_pos[0] <= (startx_3+sizex_3) and starty_3 <= mouse_pos[1] <= starty_3+sizey_3:
                print("hello3")
            elif startx_4 <= mouse_pos[0] <= (startx_4+sizex_4) and starty_4 <= mouse_pos[1] <= starty_4+sizey_4:
                print("hello4")
            elif startx_5 <= mouse_pos[0] <= (startx_5+sizex_5) and starty_5 <= mouse_pos[1] <= starty_5+sizey_5:
                print("hello5")
            elif startx_6 <= mouse_pos[0] <= (startx_6+sizex_6) and starty_6 <= mouse_pos[1] <= starty_6+sizey_6:
                print("hello6")
            
                
                
    screen.fill(black) 
    mouse_pos = pygame.mouse.get_pos()
    startx, starty, sizex, sizey = Button_make.button(dark_grey,50,50,200,200)
    printer = pygame.transform.scale(printer,(sizex, sizey))
    screen.blit(printer,(startx, starty),)
    startx_1, starty_1, sizex_1, sizey_1 = Button_make.button(dark_grey,700,25,300,75)
    startx_2, starty_2, sizex_2, sizey_2 = Button_make.button(dark_grey,700,125,300,75)
    startx_3, starty_3, sizex_3, sizey_3 = Button_make.button(dark_grey,700,225,300,75)
    startx_4, starty_4, sizex_4, sizey_4 = Button_make.button(dark_grey,700,325,300,75)
    startx_5, starty_5, sizex_5, sizey_5 = Button_make.button(dark_grey,700,425,300,75)
    startx_6, starty_6, sizex_6, sizey_6 = Button_make.button(dark_grey,700,525,300,75)
    radius1 = Button_make.circle(screen,dark_grey,(400,600),50,48,True,True,True,True)
    text = Text_create("Money Printer", white, black, 20, 400, 200)
    Counter_Text = Text_create("Money amount = £"+str(f"{Counter_num:.2f}"), white, black, 20, 400, 300)
    Price = Counter_Text = Text_create("Price: £"+str(f"{price:.2f}"), white, black, 20, 400, 400)
    y = 0
    pygame.display.update()
 

    
    