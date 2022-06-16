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
missile_shot = False

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
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        
    def draw(self,canvas):
        #canvas.draw_circle(self.pos, self.radius, 1, "White", "White")
        if self.thrust:
            canvas.draw_image(self.image, [self.image_center[0] + 85,self.image_center[1]] , self.image_size, self.pos, self.image_size, self.angle)
        else:
            canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        c = .03
        self.angle += self.angle_vel
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT 
        
        self.vel[0] *= (1 - c)
        self.vel[1] *= (1 - c)
        
        #forward = [math.cos(self.angle), math.sin(self.angle)]
        forward = angle_to_vector(self.angle)
        
        
        if self.thrust:
            self.vel[0] += forward[0]
            self.vel[1] += forward[1]
    
    def inc_angle_velocity(self):
        self.angle_vel += .1
        
    def dec_angle_velocity(self):
        self.angle_vel -= .1
        
    def set_angle_vel(self,value):
        self.angle_vel = value
    
    def thrusters_on(self,value):
        self.thrust = value
        if value:
            ship_thrust_sound.set_volume(.5)
            ship_thrust_sound.play()
        else:
            ship_thrust_sound.rewind()
            
    def shoot(self):
        global a_missile
        forward = angle_to_vector(self.angle)
        missile_pos = list(self.pos)
        missile_vel = list(self.vel)
        missile_pos[0] += forward[0] * self.image_center[0]
        missile_vel[0] += forward[0] * 2
        missile_pos[1] += forward[1] * self.image_center[1]
        missile_vel[1] += forward[1] * 2
        a_missile = Sprite(missile_pos, missile_vel, self.angle, 0, missile_image,missile_info, missile_sound)
    
# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound = None):
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
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        #canvas.draw_circle(self.pos, self.radius, 1, "Red", "Red")
        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)
    
    def update(self):
        self.angle += self.angle_vel
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
    
    def set_pos(self,pos):
        self.pos = pos
    
    def set_vel(self,vel):
        self.vel = vel
        
    def set_angle_vel(self,angle_vel):
        self.angle_vel = angle_vel
        
           
def draw(canvas):
    global time,lives
    

    
    
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

    #Draw Number of lives
    #canvas.draw_text("Lives: " + str(lives), [50, 50], 40, "White")
    canvas.draw_text("Lives", [50, 50], 30, "White")
    canvas.draw_text(str(lives), [50, 80], 30, "White")
    #Draw Score
    #canvas.draw_text("Score: " + str(score), [650, 50], 40, "White")
    canvas.draw_text("Score", [650, 50], 30, "White")
    canvas.draw_text(str(score), [650, 80], 30, "White")
    
    # draw ship and sprites
    my_ship.draw(canvas)
    a_rock.draw(canvas)
    
    #If missile is shot draw the missile
    #if missile_shot:
    a_missile.draw(canvas)
    a_missile.update()
    
    # update ship and sprites
    my_ship.update()
    a_rock.update()
    
    
def keydown(key):
    global my_ship,missile_shot
    acc = 1
    
    if key==simplegui.KEY_MAP["right"]:
        my_ship.inc_angle_velocity()
    elif key==simplegui.KEY_MAP["left"]:
        my_ship.dec_angle_velocity()
    elif key==simplegui.KEY_MAP["up"]:
        my_ship.thrusters_on(True)
    elif key==simplegui.KEY_MAP["space"]:
        missile_shot = True
        my_ship.shoot()

        
        
def keyup(key):
    global my_ship
    
    if key==simplegui.KEY_MAP["left"]:
        my_ship.set_angle_vel(0)
    elif key==simplegui.KEY_MAP["right"]:
        my_ship.set_angle_vel(0)
    elif key==simplegui.KEY_MAP["up"]:
        my_ship.thrusters_on(False)

            
# timer handler that spawns a rock    
def rock_spawner():
    global a_rock
    #(pos, vel, ang, ang_vel, image, info, sound = None)
    pos = [random.randrange(0, WIDTH+1),random.randrange(0,HEIGHT+1)]
    vel = [random.randrange(-10,11)/10,random.randrange(0,11)/10]
    angle_vel = random.randrange(-10,11)/100
    a_rock.set_pos(pos)
    a_rock.set_vel(vel)
    a_rock.set_angle_vel(angle_vel)
    
# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
a_rock = Sprite([WIDTH / 3, HEIGHT / 3], [1, 1], 0, 0, asteroid_image, asteroid_info)
a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
