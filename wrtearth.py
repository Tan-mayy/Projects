from vpython import *
from time import *
from PIL import Image


# Create the scene
scene = canvas(width = 1366, height = 768, fullscreen = True) 

# Create the planet
planet = sphere(pos=vector(-15, -3, 0), radius=15.2, texture = "https://i.imgur.com/HQnc5Xy.jpg", shininess = 1)

radius_earth = 16
earth = sphere(pos=vector(140,-30,20), texture=textures.earth, radius=radius_earth , shininess = 0)



# Define the parameters for the elliptical path
a = 20 # Semi-major axis
b = 40 # Semi-minor axis


size = 0.04
boxx = box(pos = vector(0,0,0), color= color.yellow, shininess = 0, size = vector(1,1,1.5))
cy_left = cylinder(pos = vector(0,0.5,0), axis = vector(0, 1, 0), radius = size)
cy_rgt = cylinder(pos = vector(0,-0.5,0), axis = vector(0, -1, 0), radius = size)

panel1 = box(pos = vector(0,1.5,0), size = vector(1.2,1.3,0.1)) #, texture = "https://i.imgur.com/iA8P9ws.jpg"
panel2 = box(pos = vector(0,-1.5,0), size = vector(1.2,1.3,0.1)) 


merge_sat = compound([boxx, cy_left, cy_rgt, panel1, panel2])

#merge_sat.pos = vector(-1,0,0)
merge_sat.axis = vector(-1.5, -1.5, 0)


# Create the satellite
#satellite = sphere(radius=1, color=color.white )

# Create the trail
trail = curve(color=color.white)

# Define the animation loop
t = 0
dt = 0.01

camera = scene.camera

#camera.pos = vector(160,-30,20)
#camera.axis = vector(1, 0, 0)
#camera.up = vector(0, 0, 1)

while True:
    rate(100)  # Controls the animation speed

    planet.rotate(angle=radians(0.1), axis = vector(-10,10,-10))
    earth.rotate(angle=radians(0.5), axis = vector(-0.5,-1,0))
    
    # Calculate the position of the satellite on the elliptical path
    x = b * sin(t)
    y = 0.5 * a * sin(t)
    z = a * cos(t)  # Adjust the z coordinate to create an inclined orbit
    
    
    # Set the satellite's position relative to the planet
    merge_sat.pos = vector(x, y, z)
    
    
    # Update time
    t += dt
