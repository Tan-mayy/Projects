from vpython import *
from time import *
from PIL import Image
'''
        axial_tilt_venus = 177.3 degrees , In radians = 3.0944, 
        axial_tilt_earth = 23.5 degrees , in rad = 0.4102
        earth angular_velo = 1
        venus angular_velo = 1/255

'''
# Create the scene
scene = canvas(width = 1366, height = 768, fullscreen = True) 

# Create the planet
venus = sphere(pos=vector(-15, -1, 0), radius=15.2, texture = "https://i.imgur.com/HQnc5Xy.jpg", shininess = 0)

radius_earth = 20
earth = sphere(pos=vector(140,-30,35), texture=textures.earth, radius=radius_earth , shininess = 0)

#venus_light = local_light(pos = vector(-15,-1,0), color = color.white)
#earth_light = local_light(pos = vector(140,-30,35))

# parameters that define shape of the elliptical orbit
a = 20 # Semi-major axis
b = 40 # Semi-minor axis
eccentricity = sqrt(1 - (a ** 2) / (b ** 2))
satellite_angle = 0
satellite_change_angle = 0.01



size = 0.04
boxx = box(pos = vector(0,0,0), color= color.yellow, shininess = 0, size = vector(1,1,1.5))
cy_left = cylinder(pos = vector(0,0.5,0), axis = vector(0, 1, 0), radius = size)
cy_rgt = cylinder(pos = vector(0,-0.5,0), axis = vector(0, -1, 0), radius = size)

panel1 = box(pos = vector(0,1.5,0), size = vector(1.2,1.3,0.1)) #, texture = "https://i.imgur.com/iA8P9ws.jpg"
panel2 = box(pos = vector(0,-1.5,0), size = vector(1.2,1.3,0.1)) 


merge_sat = compound([boxx, cy_left, cy_rgt, panel1, panel2])

#merge_sat.pos = vector(-1,0,0)
merge_sat.axis = vector(0, 1, 1)


# Create the satellite
#satellite = sphere(radius=1, color=color.white )

# Create the trail
#trail = curve(color=color.white)

# Define the animation loop
''' satellite_angle = 0
satellite_change_angle = 0.01
'''

print(scene.camera.pos)
#combined_sat_venusMotion = compound([venus, merge_sat])

r1 = ring(pos = vector(-0.1,0,0), axis = vector(1,0,0), radius = 0.95, thickness = 0.1)
r2 = ring(pos = vector(-0.2,0,0), axis = vector(1,0,0), radius = 0.9, thickness = 0.1)
r3 = ring(pos = vector(-0.3,0,0), axis = vector(1,0,0), radius = 0.85, thickness = 0.1)
r4 = ring(pos = vector(-0.4,0,0), axis = vector(1,0,0), radius = 0.80, thickness = 0.1)
r5 = ring(pos = vector(-0.5,0,0), axis = vector(1,0,0), radius = 0.72, thickness = 0.1)
r6 = ring(pos = vector(-0.6,0,0), axis = vector(1,0,0), radius = 0.65, thickness = 0.1)
r7 = ring(pos = vector(-0.7,0,0), axis = vector(1,0,0), radius = 0.58, thickness = 0.1)
r8 = ring(pos = vector(-0.8,0,0), axis = vector(1,0,0), radius = 0.49, thickness = 0.1)
r9 = ring(pos = vector(-0.9,0,0), axis = vector(1,0,0), radius = 0.40, thickness = 0.1)
r10 = ring(pos = vector(-1,0,0), axis = vector(1,0,0), radius = 0.33, thickness = 0.1)

sph_support = sphere(pos = vector(-1.1, 0,0), axis = vector(1,0,0), size = vector(0.6,0.6,0.6))

cone_sph_support = cone(pos = vector(150, -13, 35), axis = vector(0.3, 1, 0), radius = 0.4, length = 0.9)

ant_merge = compound([r1, r2,r3,r4,r5,r6,r7,r8,r9,r10, sph_support])

ant_merge.axis = vector(-9,5,-5)

ant_merge.pos = vector(150.2, -11.86, 35)

start_point = vector(-5, 0, 0)
end_point = vector(5, 0, 0)

# Create the line
#line = curve(pos=[start_point, end_point], color=color.white, radius=0.05)

# Defining the perigee's coordinates on cartesian plane

x_pos = -41
y_pos = 1
z_pos = 0

#sph = sphere(pos = vector(x_pos,y_pos,z_pos), radius = 0.5, color = color.blue)

#scene.after(8000, )
while True:
    rate(100)  # Controls the animation speed

    venus.rotate(angle=radians(0.06), axis = vector(0.06,-1,0))
    #earth.rotate(angle=radians(0.65), axis = vector(0.5,-1,0))
    
    # Calculate the position of the satellite on the elliptical path
    x = b * sin(satellite_angle)
    y = -0.07 * a * sin(satellite_angle)
    z = a * cos(satellite_angle)  # Adjust the z coordinate to create an inclined orbit
    
    distance_from_perigee = b * (1 - eccentricity)

    #plane = box(pos = vector(-38,1.14,0), size = vector(23,1.2,38), color = color.black)
    # Set the satellite's position relative to the planet
    merge_sat.pos = vector(x, y, z)
    
    # Calculating distance of revolving sat wrt to perigee
    dist = sqrt((x_pos - x)**2 + (y_pos - y)**2 + (z_pos - z)**2)


    #max apogee coordinates (39.9997, -1.39999, 0.0796325)
    #when about to move to blind spot from -z coordinate(-16.1357, 0.56475, -18.3005)
    #Distance will be under root{(-41 - (-16.1357))**2 + (1 - (-1))**2 + (0 - 0.0796325)**2}
    # 618.2334 + 4 + 0.00634133 = 622.239741



    #scene.camera.pos = vector(170,-10,70)
    ####scene.camera.axis = vector(-20, 0, 0)


    # Case 1 - With Respect to earth being on earth the receiver and the earth will be considered as stationary 

    # Fixed camera position and axis is :
    '''scene.camera.pos = vector(155,-9.35,25)  # 140, -10, 45
    scene.camera.axis = vector(-35, -1, 0) 
    '''
    #print(scene.camera.axis)

    #scene.camera.pos = vector(155,-9.35,25)  # 140, -10, 45
    #scene.camera.axis = vector(-35, -1, 0) 

    '''if distance_from_perigee <= 3:
        satellite_angle += 0.05  # Increase speed when close to perigee
        
    else:
        satellite_angle += 0.01  # Regular speed when away from perigee

          
'''

    p1 = vector(150.2, -10.96, 35)
    p2 = vector (x, y, z)


   # signal = curve([p1, p2])

    satellite_angle -= satellite_change_angle

    #if dist < 622.239741:
        #signal.color = color.black

    
    #print(merge_sat.pos)
   # '''sign = signal.visible
    #scene.after(100, sign = False)
