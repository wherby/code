################################################################
#
# A shield is added when "s" is pressed.
#
################################################################

# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0.5
missile = False
shield_image_number = 0

class ImageInfo:
    def __init__(self, center, size, radius = 0, lifespan = None, animated = False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated

    
# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim
    
# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")
T_ship_info = ImageInfo([135,45],[90,90],35)

#shield image
shield_info = ImageInfo([45, 45], [90, 90], 35)
shield_image = simplegui.load_image("https://dl.dropboxusercontent.com/u/3775463/py_space/shield.png")
#shield sound
shield_sound = simplegui.load_sound("https://dl.dropboxusercontent.com/u/3775463/py_space/electricshock.mp3")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5,5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")

# sound assets purchased from sounddogs.com, please do not redistribute
soundtrack = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/soundtrack.mp3")
missile_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/missile.mp3")
missile_sound.set_volume(.5)
ship_thrust_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/thrust.mp3")
explosion_sound = simplegui.load_sound("http://commondatastorage.googleapis.com/codeskulptor-assets/sounddogs/explosion.mp3")

# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info, t_info, s_lives = 3):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.t_info = t_info
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lives = s_lives
        self.shielded = False
        self.acel = [0,0]
        
    def draw(self,canvas):
        canvas.draw_image(self.image,self.image_center,
                          self.image_size, self.pos,
                          self.image_size, self.angle)
        if self.shielded == True:
            canvas.draw_image(shield_image,
                 [45+90*(shield_image_number%12),45],
                  my_ship.image_size, my_ship.pos,
                  my_ship.image_size, my_ship.angle)
            while shield_sound.play() == False:
                shield_sound.play()
    def shield_add(self):
        self.shielded = True
        shield_timer.start()
                
    def shield_remove(self):
        self.shielded = False
        shield_timer.stop()
        shield_sound.pause()
        shield_sound.rewind()
        
    def update(self):
        self.angle = self.angle + self.angle_vel
        self.acel = [math.cos(self.angle),math.sin(self.angle)]
        if self.thrust == True:
            ship_thrust_sound.play()
            self.image_center = self.t_info.get_center()
            for i in [0,1]:
                self.vel[i] = self.vel[i] + self.acel[i]
                self.vel[i] *= 0.9 

        else: 
            ship_thrust_sound.pause()
            ship_thrust_sound.rewind()              
            self.image_center = ship_info.get_center()
            for i in [0,1]:
                self.vel[i] *= 0.93
        self.pos[0] = (self.pos[0] + self.vel[0])%WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1])%HEIGHT

    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None, beam = False):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        self.beam = beam
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        canvas.draw_image(self.image,self.image_center,
                          self.image_size, self.pos, self.image_size,self.angle)
    
    def update(self):
        self.angle += self.angle_vel
        for i in [[0,WIDTH],[1,HEIGHT]]:
            self.pos[i[0]] = (self.pos[i[0]] + self.vel[i[0]])%i[1] 

           
def draw(canvas):
    global time
    
    # animiate background
    time += 1
    center = debris_info.get_center()
    size = debris_info.get_size()
    wtime = (time / 8) % center[0]
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2], [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, [center[0] - wtime, center[1]], [size[0] - 2 * wtime, size[1]], 
                                [WIDTH / 2 + 1.25 * wtime, HEIGHT / 2], [WIDTH - 2.5 * wtime, HEIGHT])
    canvas.draw_image(debris_image, [size[0] - wtime, center[1]], [2 * wtime, size[1]], 
                                [1.25 * wtime, HEIGHT / 2], [2.5 * wtime, HEIGHT])

    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    if missile == True:
        a_missile.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    a_rock.update()
    if missile:
        a_missile.update()
    
    #Draw score and lives
    canvas.draw_text("Lives: " + str(lives), [20,30], 20, "white")
    canvas.draw_text("Score: " + str(score), [WIDTH - 120,30], 20, "white")
    
# timer handler that spawns a rock    
def rock_spawner():
    global a_rock
    rock_spin = random.randrange(1,10)/100
    rock_vel = [0,0]
    rock_w = random.randrange(0,WIDTH)
    rock_h = random.randrange(0,HEIGHT)
    for i in [0,1]:
        rock_vel[i] = random.randrange(-180,180)/60
    a_rock = Sprite([rock_w, rock_h], rock_vel, 0, rock_spin, asteroid_image, asteroid_info)

# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info,T_ship_info)
a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0.01, asteroid_image, asteroid_info)

# register handlers
frame.set_draw_handler(draw)

def keydown(key):
    global missile, a_missile
    if key == simplegui.KEY_MAP["left"]:
        my_ship.angle_vel = -0.1
    if key == simplegui.KEY_MAP["right"]:
        my_ship.angle_vel = 0.1
    if key == simplegui.KEY_MAP["up"]:
        my_ship.thrust = True
    if key == simplegui.KEY_MAP["space"]:
        missile_speed = [0,0]
        missile_pos = [0,0]
        for i in [0,1]:
            missile_speed[i] = my_ship.vel[i] + my_ship.acel[i]*3
            missile_pos[i] = my_ship.pos[i]+ my_ship.acel[i]*40
        missile = True
        a_missile = Sprite(missile_pos, missile_speed, my_ship.angle, 0, missile_image, missile_info, missile_sound, beam = True)
    if key == simplegui.KEY_MAP["s"]:
        if my_ship.shielded == True:
            my_ship.shield_remove()
        elif my_ship.shielded == False:
            my_ship.shield_add()
def keyup(key):
    for side in ["left","right"]:
        if key == simplegui.KEY_MAP[side]:
            my_ship.angle_vel = 0
    if key == simplegui.KEY_MAP["up"]:
            my_ship.thrust = False

def shield_drawer():
    global shield_image_number
    shield_image_number += 1
    print shield_image_number
    print shield_image_number%13
    
timer = simplegui.create_timer(3000.0, rock_spawner)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
shield_timer = simplegui.create_timer(60, shield_drawer)

# get things rolling
timer.start()
frame.start()
