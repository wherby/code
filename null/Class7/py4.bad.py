# program template for Spaceship
import simplegui
import math
import random

# globals for user interface
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
score = 0
lives = 3
time = 0.5

# helper functions
def add_vector(a, b, plus = 1):
    a[0] += plus*b[0]
    a[1] += plus*b[1]
    
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]

def dist(p,q):
    return math.sqrt((p[0] - q[0]) ** 2+(p[1] - q[1]) ** 2)



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
ship_thrust_info = ImageInfo([135, 45], [90, 90], 35)
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


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info, thrust_info, thrust_sound = None):
        self.pos = [pos[0],pos[1]]
        self.vel = [vel[0],vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()		
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.image_thurst_center = thrust_info.get_center()
        self.thrust_sound = thrust_sound
        self.c = 0.3
        
    def draw(self, canvas):
        if self.thrust:
            center = self.image_thurst_center
            ship_thrust_sound.play()
        else:
            center = self.image_center
            ship_thrust_sound.rewind()        
        canvas.draw_image(self.image, center, self.image_size,
                          self.pos, self.image_size, self.angle)
                          
    def update(self):
        #angle update
        self.angle += self.angle_vel
        
        #position update
        add_vector(self.pos, self.vel)
        self.pos[0] %= CANVAS_WIDTH
        self.pos[1] %= CANVAS_HEIGHT
        
        #friction update
        self.vel[0] *= (1-self.c)
        self.vel[1] *= (1-self.c)
        
        #Thrust update - acceleration in direction of forward vector
        forward = angle_to_vector(self.angle)
        if self.thrust:
            add_vector(self.vel, forward)
            
    def shoot(self):
        a_missile.pos = list(self.pos)
        forward = angle_to_vector(self.angle)
        a_missile.vel = [self.vel[i] + 4*forward[i] for i in range(2)]
        a_missile.sound.play()
    
    
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
        self.sound = sound
        if sound:
            sound.rewind()
            sound.play()
   
    def draw(self, canvas):
        canvas.draw_image(self.image, self.image_center, self.image_size,
                          self.pos, self.image_size, self.angle)
    
    def update(self):
        self.angle += self.angle_vel
        
        add_vector(self.pos, self.vel)
        self.pos[0] %= CANVAS_WIDTH
        self.pos[1] %= CANVAS_HEIGHT


#event handlers   
     
def draw(canvas):
    global time
    
    # animiate background
    time += 1
    center = debris_info.get_center()
    size = debris_info.get_size()
    wtime = (time / 8) % center[0]
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2], [CANVAS_WIDTH, CANVAS_HEIGHT])
    canvas.draw_image(debris_image, [center[0] - wtime, center[1]], [size[0] - 2 * wtime, size[1]], 
                                [CANVAS_WIDTH / 2 + 1.25 * wtime, CANVAS_HEIGHT / 2], [CANVAS_WIDTH - 2.5 * wtime, CANVAS_HEIGHT])
    canvas.draw_image(debris_image, [size[0] - wtime, center[1]], [2 * wtime, size[1]], 
                                [1.25 * wtime, CANVAS_HEIGHT / 2], [2.5 * wtime, CANVAS_HEIGHT])

    # draw ship and sprites
    my_ship.draw(canvas)
    my_ship.update()
    a_rock.draw(canvas)
    a_missile.draw(canvas)
    
    # update ship and sprites
    my_ship.update()
    a_rock.update()
    a_missile.update()
    
    # score and lives
    canvas.draw_text("Lives", [70, 100], 40, "White")
    canvas.draw_text(str(lives), [100, 150], 40, "White")
    canvas.draw_text("Score", [CANVAS_WIDTH-180, 100], 40, "White")
    canvas.draw_text(str(score), [CANVAS_WIDTH-150, 150], 40, "White")
    
    
#Handler for keydown:
def keydown(key):
    if key == simplegui.KEY_MAP["up"]:
        my_ship.thrust = True
    elif key == simplegui.KEY_MAP["left"]:
        my_ship.angle_vel = -0.05
    elif key == simplegui.KEY_MAP["right"]:
        my_ship.angle_vel = +0.05
    elif key == simplegui.KEY_MAP["space"]:        
        my_ship.shoot()
        
#Handler for keyup:
def keyup(key):
    if key == simplegui.KEY_MAP["up"]:
        my_ship.thrust = False
    elif key == simplegui.KEY_MAP["left"] or key == simplegui.KEY_MAP["right"]:
        my_ship.angle_vel = 0		
            
# timer handler that spawns a rock    
def rock_spawner():
    global a_rock
    vel = [random.randrange(-10,10)/10, random.randrange(-10,10)/10]
    a_rock = Sprite([random.random()*CANVAS_WIDTH, random.random()*CANVAS_HEIGHT], vel,
                    0, random.random()/10, 
                    asteroid_image, asteroid_info)
    
# initialize frame
frame = simplegui.create_frame("Asteroids", CANVAS_WIDTH, CANVAS_HEIGHT)

# initialize ship and two sprites
my_ship = Ship([CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2], [0, 0], 0, ship_image, ship_info, ship_thrust_info, ship_thrust_sound)
a_rock = Sprite([CANVAS_WIDTH / 3, CANVAS_HEIGHT / 3], [1, 1], 0, 0, asteroid_image, asteroid_info)
a_missile = Sprite([2 * CANVAS_WIDTH / 3, 2 * CANVAS_HEIGHT / 3], [-1,1], 0, 0, missile_image, missile_info, missile_sound)

# register handlers
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

timer = simplegui.create_timer(1000.0, rock_spawner)

# get things rolling
timer.start()
frame.start()
