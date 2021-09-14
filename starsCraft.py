import math
import random
import time

import arcade
from arcade import key
from arcade.window_commands import set_background_color

class Enemy(arcade.Sprite):
    def __init__(self,w,h):
        super().__init__(':resources:images/space_shooter/playerShip2_orange.png')
        self.speed=4
        self.center_x=random.randint(0,w)
        self.center_y=h
        self.angle=180
        self.width=48
        self.height=48

    def move(self):
        self.center_y-=self.speed





class SpaceCraft(arcade.Sprite):
    def __init__(self,w,h):
        super().__init__(":resources:images/space_shooter/playerShip1_green.png")
        self.width=48
        self.height=48
        self.center_x=w//2
        self.center_y=48
        self.angle=0
        self.change_angle=0
        self.bullet_list=[]
        self.speed=4


    def rotate(self):
        self.angle+=self.change_angle*self.speed 

    def fire(self):
        self.bullet_list.append(Bullet(self))     
    

class Bullet(arcade.Sprite):
    def __init__(self,host):
        super().__init__(':resources:images/space_shooter/laserRed01.png')
        self.speed=4
        self.angle=host.angle
        self.center_x=host.center_x
        self.center_y=host.center_y

    def move(self):
        angle_rad=math.radians(self.angle)
        self.center_x-=self.speed*math.sin(angle_rad)
        self.center_y+=self.speed*math.cos(angle_rad)


class Game(arcade.Window):
    def __init__(self):
        self.w=800
        self.h=600
        super().__init__(self.w,self.h,'Silver SpaceCraft')
        arcade.set_background_color(arcade.color.BLACK)
        
        self.background_image=arcade.load_texture(':resources:images/backgrounds/stars.png')
        self.me=SpaceCraft(self.w,self.h)
        self.enemy_list=[]
        self.start_time=time.time()
        
        


    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,self.w,self.h,self.background_image)
        self.me.draw()
      

        for i in range(len(self.me.bullet_list)):
            self.me.bullet_list[i].draw()

        for i in range(len(self.enemy_list)):
            self.enemy_list[i].draw()      


        #self.enemy.draw()    

    def on_update(self, delta_time):
        self.end_time=time.time()
        if self.end_time-self.start_time>5:
            self.enemy_list.append(Enemy(self.w,self.h))
            self.start_time=time.time()

        self.me.rotate()



        

        for i in range(len(self.me.bullet_list)):
            self.me.bullet_list[i].move()

        for i in range(len(self.enemy_list)):
            self.enemy_list[i].move()    

        #self.enemy.move()    
    

    def on_key_press(self,key,modifiers):
        if key==arcade.key.RIGHT:
            self.me.change_angle=-1
        elif key==arcade.key.LEFT:
            self.me.change_angle=1
        elif key==arcade.key.SPACE:
            self.me.fire()


    def on_key_release(self,key,modifiers):
        self.me.change_angle=0


game=Game()
arcade.run()
