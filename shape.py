from vpython import *

scene = canvas(width = 1366, height = 640, fullscreen = True)
size = 0.04

##### Main body
boxx = box(pos = vector(0,0,0), color= color.yellow, shininess = 0, size = vector(1,1,1.5), texture = {'file' : "https://i.imgur.com/1uo6oHa.jpg", 'bumpmap' : bumpmaps.stones})#

boxx_front_brown = box(pos = vector(0,0,0.741), size = vector(0.99,0.99,0.02) , texture = {'file' : 'https://i.imgur.com/U5S2Idv.jpg'})

boxx_top_brown = box(pos = vector(0,0.495,0), size = vector(0.013,1,1.504), texture = {'file' : 'https://i.imgur.com/zhqZ2xH.jpg'}, axis = vector(0,1,0))

#boxx_bottom_brown = box(pos = vector(0,-0.495,0), size = vector(0.013,1,1.504), texture = {'file' : 'https://i.imgur.com/zhqZ2xH.jpg'}, axis = vector(0,1,0))


##### Support cylinders
cy_left = cylinder(pos = vector(0,0.5,0), axis = vector(0, 1, 0), radius = size, texture = textures.metal)
cy_rgt = cylinder(pos = vector(0,-0.5,0), axis = vector(0, -1, 0), radius = size, texture = textures.metal)


##### Solar Arrays
panel1 = box(pos = vector(0,1.5,0), size = vector(1.2,1.3,0.1), texture = "https://i.imgur.com/iA8P9ws.jpg") #
panel2 = box(pos = vector(0,-1.5,0), size = vector(1.2,1.3,0.1), texture = "https://i.imgur.com/iA8P9ws.jpg") 

'''
tri_fig = shapes.triangle(size = vector(1,1,1))
extrud = ([vector(0,0,0), vector(0,0,0.1)])
shape_tri = extrusion(shape = tri_fig, path = extrud)
shape_tri.pos = vector(2,2,2)'''
#cover = box(pos = vector(1.2,1.8,0), size = vector(1.2,1.3,0.1), color = color.white)

##### Box Support for disc
boxx_mid_left = box(pos = vector(-0.475,0,0.769), shininess = 0, size = vector(0.047,0.07,0.136), texture = "https://i.imgur.com/aZClncF.jpg")


boxx_top = box(pos = vector(-0,0.32,0.769), shininess = 0, size = vector(0.047,0.07,0.14), texture = "https://i.imgur.com/aZClncF.jpg", axis = vector(-2,-4,0))


boxx_bottom_right = box(pos = vector(0.015,-0.316,0.769), shininess = 0, size = vector(0.047,0.07,0.14), texture = "https://i.imgur.com/aZClncF.jpg", axis = vector(-4,7,0))


boxx_rgt_corner = box(pos = vector(0.350,0.022,0.769), shininess = 0, size = vector(0.047,0.07,0.14), texture = "https://i.imgur.com/aZClncF.jpg")



boxx_rgt_top_corner1 = box(pos = vector(0.4450,0.235,0.769), shininess = 0, size = vector(0.047,0.047,0.047), texture = "https://i.imgur.com/aZClncF.jpg")



boxx_rgt_top_corner2 = box(pos = vector(0.4450,0.165,0.769), shininess = 0, size = vector(0.05,0.05,0.05), texture = "https://i.imgur.com/aZClncF.jpg")


##### Left Box
boxx_top_left = box(pos = vector(-0.427,0.410,0.7810), shininess = 0, size = vector(0.14,0.15,0.1), texture = "https://i.imgur.com/mqJrnUT.jpg")

##### Cylin on left box
box_left_cylin = cylinder(pos = vector(-0.427, 0.465, 0.7810), radius = 0.01, size = vector(0.08,0.08,0.08), axis = vector(0,1,0))

##### Cylin on left box coming out
box_left_cylin_o = cylinder(pos = vector(-0.427, 0.5338, 0.7810), radius = 0.01, size = vector(0.05,0.05,0.05), axis = vector(0,0,1))


##### Bottom Left Box
boxx_bottom_left = box(pos = vector(-0.427,-0.410,0.7810), shininess = 0, size = vector(0.14,0.15,0.1), texture = 'https://i.imgur.com/mqJrnUT.jpg')

##### Cylin on left bottom box
box_bt_left_cylin = cylinder(pos = vector(-0.427, -0.545, 0.7810), radius = 0.01, size = vector(0.08,0.08,0.08), axis = vector(0,1,0))

##### Cylin on left bottom box coming out
box_bt_left_cylin_o = cylinder(pos = vector(-0.427, -0.5338, 0.7810), radius = 0.01, size = vector(0.05,0.05,0.05), axis = vector(0,0,1))


boxx_top_right = box(pos = vector(+0.427,0.410,0.7810), shininess = 0, size = vector(0.14,0.15,0.1), texture = 'https://i.imgur.com/mqJrnUT.jpg')

##### Cylin on right box
box_top_right_cylin = cylinder(pos = vector(0.427, 0.465, 0.7810), radius = 0.01, size = vector(0.08,0.08,0.08), axis = vector(0,1,0))

##### Cylin on right box coming out
box_left_cylin_o = cylinder(pos = vector(+0.427, 0.5338, 0.7810), radius = 0.01, size = vector(0.05,0.05,0.05), axis = vector(0,0,1))


# down to the right box 
boxx_down_right = box(pos = vector(+0.427,-0.410,0.7810), shininess = 0, size = vector(0.14,0.15,0.1), texture = 'https://i.imgur.com/mqJrnUT.jpg')

##### Cylin on right down below box CHECK THIS YET TO BE FIXED...................................
box_down_right_cylin = cylinder(pos = vector(0.427, -0.550, 0.7810), radius = 0.01, size = vector(0.08, 0.08, 0.08), axis = vector(0,1,0))

##### Cylin on right box coming out
box_down_cylin_right_o = cylinder(pos = vector(0.427, -0.5338, 0.7810), radius = 0.01, size = vector(0.05,0.05,0.05), axis = vector(0,0,1))


#box_right_botto = box(pos=vector(0.427,0.410,0.7810), shininess = 0, size = vector(0.14,0.15,0.1), texture = textures.metal )


# For Top Face ...........

triangle_lar = shapes.triangle(length = 0.01, thickness=4)
pathh = [vector(0,0,0), vector(0,0,0.15)]
extru_tri = extrusion(path = pathh , shape = triangle_lar)
extru_tri.pos = vector(-0.327,0.529,0)
extru_tri.axis = vector(1.2,2,0)
extru_tri.texture = {'file' : textures.wood, 'bumpmap' : bumpmaps.stucco, 'place' : ['sides', 'all']}


triangle_lar2 = shapes.triangle(length = 0.01, thickness=4)
pathh2 = [vector(0,0,0), vector(0,0,0.15)]
extru_tria = extrusion(path = pathh2 , shape = triangle_lar2)
extru_tria.pos = vector(-0.40,0.529,0.4)
extru_tria.axis = vector(1.2,2,0)
extru_tria.texture = {'file' : textures.wood, 'bumpmap' : bumpmaps.stucco, 'place' : ['sides', 'all']}

###### WORk Cubes, cylinder on top face.....................
cylinder_topf_ = cylinder(axis = vector(0,1,0), pos = vector(-0,0.500,-0.68), radius = 0.037, size = vector(0.15,0.15,0.15), texture = {'file' : textures.wood, 'bumpmap' : bumpmaps.stucco, 'place' : ['sides', 'all']})

cube_topf_ = box(axis = vector(0,1,0), pos = vector(-0,0.620,-0.68), size = vector(0.06,0.14,0.13), texture = {'file' : "https://i.imgur.com/1uo6oHa.jpg", 'bumpmap' : bumpmaps.stones})

cube_topf_plate  = box(axis = vector(1,0,0), pos = vector(-0,0.647,-0.68), size = vector(0.15,0.01,0.13))


cylinder_topf_2 = cylinder(axis = vector(0,1,0), pos = vector(0.325,0.500,0.68), radius = 0.034, size = vector(0.15,0.15,0.15), texture = {'file' : textures.wood, 'bumpmap' : bumpmaps.stucco, 'place' : ['sides', 'all']})

cube_topf_2 = box(axis = vector(0,1,0), pos = vector(0.325,0.620,0.68), size = vector(0.06,0.14,0.13), texture = {'file' : "https://i.imgur.com/1uo6oHa.jpg", 'bumpmap' : bumpmaps.stones})

cube_topf_plate2  = box(axis = vector(1,0,0), pos = vector(0.325,0.647,0.68), size = vector(0.15,0.01,0.13))



#Back face......................................

circular_disc3 = shapes.circle(radius=0.4)
circular_path = [vector(0,0,0), vector(0,0,0.15)]
disc = extrusion(path = circular_path, shape = circular_disc3)
disc.pos = vector(-0,0,-0.79)
disc.texture = {'file' : 'https://i.imgur.com/flc2mOj.jpg'}
#disc.texture = textures.metal

circular_disc4 = shapes.circle(radius=0.397)
circular_path = [vector(0,0,0), vector(0,0,0.15)]
disc = extrusion(path = circular_path, shape = circular_disc4)
disc.pos = vector(-0,0,-0.791)
disc.color = color.black

#disc.texture = {'file' : 'https://i.imgur.com/flc2mOj.jpg'}
#disc.texture = textures.metal


circular_disc5 = shapes.circle(radius=0.290)
circular_path = [vector(0,0,0), vector(0,0,0.15)]
disc = extrusion(path = circular_path, shape = circular_disc5)
disc.pos = vector(-0,0,-0.792)
disc.texture = {'file' : 'https://i.imgur.com/flc2mOj.jpg'}

circular_disc6 = shapes.circle(radius=0.0410)
circular_path = [vector(0,0,0), vector(0,0,0.15)]
disc = extrusion(path = circular_path, shape = circular_disc6)
disc.pos = vector(-0,0,-0.793)
disc.color = color.black
disc.texture = {'file' : 'https://i.imgur.com/flc2mOj.jpg'}



### This is the section for Gimval...
r1 = ring(pos = vector(3, 0,0), axis = vector(1,0,0), radius = 0.95, thickness = 0.1)
r2 = ring(pos = vector(2.9, 0,0), axis = vector(1,0,0), radius = 0.9, thickness = 0.1)
r3 = ring(pos = vector(2.8, 0,0), axis = vector(1,0,0), radius = 0.85, thickness = 0.1)
r4 = ring(pos = vector(2.7, 0,0), axis = vector(1,0,0), radius = 0.8, thickness = 0.1)
r5 = ring(pos = vector(2.6, 0,0), axis = vector(1,0,0), radius = 0.72, thickness = 0.1)
r6 = ring(pos = vector(2.5, 0,0), axis = vector(1,0,0), radius = 0.65, thickness = 0.1)
r7 = ring(pos = vector(2.4, 0,0), axis = vector(1,0,0), radius = 0.58, thickness = 0.1)
r8 = ring(pos = vector(2.3, 0,0), axis = vector(1,0,0), radius = 0.49, thickness = 0.1)
r9 = ring(pos = vector(2.2, 0,0), axis = vector(1,0,0), radius = 0.40, thickness = 0.1)
r10 = ring(pos = vector(2.1, 0,0), axis = vector(1,0,0), radius = 0.33, thickness = 0.1)
r11 = ring(pos = vector(2.2, 0,0), axis = vector(1,0,0), radius = 0.26, thickness = 0.1)
r12 = ring(pos = vector(2.1, 0,0), axis = vector(1,0,0), radius = 0.19, thickness = 0.1)
r13 = ring(pos = vector(2, 0,0), axis = vector(1,0,0), radius = 0.12, thickness = 0.1)

cylin_handle = cylinder(pos = vector(1.4, 0,0), axis = vector(1,0,0), radius = 0.13, size = vector(0.5,0.6,0.6))

orbital_manu_obj = compound([r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,cylin_handle])

orbital_manu_obj.size = vector(0.5,0.5,0.5)
orbital_manu_obj.pos = vector(0,0,-0.996)
orbital_manu_obj.axis = vector(0,0,-1)

# Below these is boxes and cylinder mounted by another cylinder for back face....

# back face top right boxx 

boxx_right_face_top_rgt = box(pos = vector(-0.425,0.410,-.810), shininess = 0, size = vector(0.14,0.15,0.1), texture = textures.metal)
boxx_right_face_top_rgt_small = box(pos = vector(-0.425,0.350,-.810), shininess = 0, size = vector(0.10,0.10,0.1), texture = textures.metal)
box_left_backf_cylin1 = cylinder(pos = vector(-0.427, 0.465, -0.7860), radius = 0.01, size = vector(0.08,0.08,0.08), axis = vector(0,1,0))
#mounting cylin
box_left_backf_cylin = cylinder(pos = vector(-0.427, 0.465, -0.810), radius = 0.01, size = vector(0.077,0.077,0.077), axis = vector(0,1,0))
##### Cylin on box coming out backface
box_left_cylin_x = cylinder(pos = vector(-0.427, 0.5338, -0.810), radius = 0.01, size = vector(0.048,0.048,0.048), axis = vector(0,0,-1))



#back face right cylinder bottom

boxx_bottom_right_rightf = box(pos = vector(-0.427,-0.410,-0.810), shininess = 0, size = vector(0.14,0.15,0.1), texture = textures.metal)
boxx_bottom_right_rightf_small = box(pos = vector(-0.427,-0.350,-0.810), shininess = 0, size = vector(0.10,0.10,0.1), texture = textures.metal)
##### Cylin on rgt bottom box
box_bt_rgt_cylin = cylinder(pos = vector(-0.427, -0.55, -0.7740), radius = 0.01, size = vector(0.1,0.1,0.1), axis = vector(0,1,0))
box_bt_rgt_cylin1 = cylinder(pos = vector(-0.427, -0.54, -0.8), radius = 0.01, size = vector(0.08,0.08,0.08), axis = vector(0,1,0))
##### Cylin on left bottom box coming out
box_bt_rgt_cylin_x = cylinder(pos = vector(-0.427, -0.540, -0.79), radius = 0.01, size = vector(0.05,0.05,0.05), axis = vector(0,0,-1))



# back face left down 

boxx_down_left_rgtf = box(pos = vector(+0.427,-0.410,-0.810), shininess = 0, size = vector(0.14,0.15,0.1), texture = textures.metal)
boxx_down_left_rgtf_small = box(pos = vector(+0.427,-0.350,-0.810), shininess = 0, size = vector(0.10,0.10,0.1), texture = textures.metal)
box_down_left_cylin = cylinder(pos = vector(0.427, -0.550, -0.7740), radius = 0.01, size = vector(0.08, 0.08, 0.08), axis = vector(0,1,0))
box_down_left_cylin_mount = cylinder(pos = vector(0.427, -0.550, -0.80), radius = 0.01, size = vector(0.08, 0.08, 0.08), axis = vector(0,1,0))
##### Cylin on right box coming out
box_down_cylin_left_x = cylinder(pos = vector(0.427, -0.5338, -0.80), radius = 0.01, size = vector(0.05,0.05,0.05), axis = vector(0,0,-1))



# back face top left boxx
boxx_top_left_rgtf = box(pos = vector(+0.427,0.410,-0.810), shininess = 0, size = vector(0.14,0.15,0.1), texture = textures.metal)
boxx_top_left_rgtf_small = box(pos = vector(+0.427,0.350,-0.810), shininess = 0, size = vector(0.10,0.10,0.1), texture = textures.metal)
box_top_left_cylin1 = cylinder(pos = vector(0.427, 0.465, -0.7860), radius = 0.01, size = vector(0.08,0.08,0.08), axis = vector(0,1,0))
box_top_left_cylin_mount = cylinder(pos = vector(0.427, 0.465, -0.810), radius = 0.01, size = vector(0.08,0.08,0.08), axis = vector(0,1,0))
##### Cylin on right box coming out
box_top_left_cylin_o = cylinder(pos = vector(+0.427, 0.5340, -0.810), radius = 0.01, size = vector(0.05,0.05,0.05), axis = vector(0,0,-1))

backf_surface_wooden = box(pos = vector(0,0,-0.741), size = vector(0.99,0.99,0.02) , texture = {'file' : 'https://i.imgur.com/U5S2Idv.jpg'})


######## Top face rec surfaces 

rec_sur = shapes.rectangle(width = 0.548, height=0.429)
path_rec = [vector(0,0,0), vector(0,0.01,0)]
rec_ext = extrusion(path= path_rec, shape = rec_sur)
rec_ext.pos = pos=vector(-0.27, 0.498,-0.44)
rec_ext.texture = {'file' : 'https://i.imgur.com/H0YpMtw.png'}

rec_sur1 = shapes.rectangle(width = 0.86, height=0.218)
path_rec1 = [vector(0,0,0), vector(0,0.01,0)]
rec_ext1 = extrusion(path= path_rec1, shape = rec_sur1)
rec_ext1.pos = pos=vector(-0.159, 0.498,0.30)
rec_ext1.texture = {'file' : 'https://i.imgur.com/H0YpMtw.png'}

rec_sur2 = shapes.rectangle(width = 0.21, height=0.3)
path_rec2 = [vector(0,0,0), vector(0,0.01,0)]
rec_ext2 = extrusion(path= path_rec2, shape = rec_sur2)
rec_ext2.pos = pos=vector(-0.329, 0.498,0.20)
rec_ext2.texture = {'file' : 'https://i.imgur.com/H0YpMtw.png'}

rec_sur3 = shapes.rectangle(width = 0.21, height=0.3)
path_rec3 = [vector(0,0,0), vector(0,0.01,0)]
rec_ext3 = extrusion(path= path_rec3, shape = rec_sur3)
rec_ext3.pos = pos=vector(-0.329, 0.498,0.63)
rec_ext3.texture = {'file' : 'https://i.imgur.com/H0YpMtw.png'}

rec_sur4 = shapes.rectangle(width = 0.86, height=0.218)
path_rec4 = [vector(0,0,0), vector(0,0.01,0)]
rec_ext4 = extrusion(path= path_rec4, shape = rec_sur4)
rec_ext4.pos = pos=vector(0.179, 0.498,0.30)
rec_ext4.texture = {'file' : 'https://i.imgur.com/H0YpMtw.png'}

rec_sur5 = shapes.rectangle(width = 0.35, height=0.368)
path_rec5 = [vector(0,0,0), vector(0,0.01,0)]
rec_ext5 = extrusion(path= path_rec5, shape = rec_sur5)
rec_ext5.pos = pos=vector(0.209, 0.498,0.30)
rec_ext5.texture = {'file' : 'https://i.imgur.com/H0YpMtw.png'}

rec_sur6 = shapes.rectangle(width = 0.46, height=0.218)
path_rec6 = [vector(0,0,0), vector(0,0.01,0)]
rec_ext6 = extrusion(path= path_rec6, shape = rec_sur6)
rec_ext6.pos = pos=vector(0.179, 0.498,-0.30)
rec_ext6.texture = {'file' : 'https://i.imgur.com/H0YpMtw.png'}

rec_sur7 = shapes.rectangle(width = 0.46, height=0.218)
path_rec7 = [vector(0,0,0), vector(0,0.01,0)]
rec_ext7 = extrusion(path= path_rec7, shape = rec_sur7)
rec_ext7.pos = pos=vector(0.314, 0.498,-0.40)
rec_ext7.texture = {'file' : 'https://i.imgur.com/H0YpMtw.png'}


###### Left Face

sph_left = sphere(pos = vector(-0.3,0,-0.3), radius = 0.34, texture = {'file' : "https://i.imgur.com/aZClncF.jpg", 'bumpmap' : bumpmaps.rock})

cylinder_leftface = cylinder(axis = vector(1,0,0), pos = vector(-.7, -0.04,0.05) , radius = 0.035, size = vector(0.4,0.4,.4), texture = {'file' : textures.wood, 'bumpmap' : bumpmaps.stucco, 'place' : ['sides', 'all']})

circular_top_left = shapes.circle(radius = 0.035)
path_cir = [vector(0,0,0), vector(0.01,0,0)]
extru_cir_cap = extrusion(shape = circular_top_left, path = path_cir)
extru_cir_cap.pos = vector(-0.705, -0.04,0.05)

#rec_frame = shapes.rectangle(width = 0.39, height = 0.67)
#rec_path = [vector(0,0,0), vector(0.01, 0, 0)]
#ext_recf = extrusion(path = rec_path, shape= rec_frame)
#ext_recf.pos = vector(-0.53, 0.06, 0.34)
#ext_recf.texture = {'file' : "https://i.imgur.com/m4q1qTZ.jpg", 'turn':-3, 'flipx':True, 'bumpmap':bumpmaps.stucco }

cube_extruded = box(pos = vector(-0.51, 0.028, 0.38), texture = {'file' : "https://i.imgur.com/aZClncF.jpg", 'bumpmap' : bumpmaps.rock}, size = vector(0.01, 0.5, 0.5))

# FOR IR2...........................................................................................................
'''ir2 = box(pos = vector(-0.7, -0.,0.09), size = vector(0.05, 0.15, 0.2))
ir_blackbox = box(pos = vector(-0.701, -0.,0.09), size = vector(0.05, 0.10, 0.14), color = color.black)
ir_blackbox2 = box(pos = vector(-0.702, -0.,0.09), size = vector(0.05, 0.0999, 0.1399))
'''
#### IR2 
left_1 = box(pos = vector(-0.7, -0.5, 0.09), size = vector(0.05, 0.13, 0.05))
left_2 = box(pos = vector(-0.7, -0.5, 0.28), size = vector(0.05, 0.13, 0.05))

top_1 = box(pos = vector(-0.7, -0.45, 0.185), size = vector(0.05, 0.05, 0.24) )
top_2 = box(pos = vector(-0.7, -0.55, 0.185), size = vector(0.05, 0.05, 0.24) )

inner_box = box(pos = vector(-0.693,-0.5,0.20), size = vector(0.04, 0.05, 0.20))
black_inside_box = box(pos = vector(-0.686,-0.5,0.19), size = vector(0.060,0.03,0.03), color = color.black)

ir2 = compound([left_1, left_2, top_1, top_2, inner_box, black_inside_box])
ir2.pos = vector(-0.433,-0.455,-0.30)
ir2.size = vector(0.25, 0.24, 0.32)

ir1 = compound([left_1, left_2, top_1, top_2, inner_box, black_inside_box])
ir1.pos = vector(-0.433,-0.455, 0.08)
ir1.size = vector(0.25, 0.19, 0.21)

uv1_box = box(pos = vector(-0.4990,-0.4533,0.1), size = vector(0.01, 0.05, 0.06))
uv1_black = box(pos = vector(-0.4991,-0.4533,0.1), size = vector(0.01, 0.02, 0.02), color = color.black)
uv1 = compound([uv1_black,uv1_box])
uv1.pos = vector(-0.47,-0.4330,0.34)
uv1.size = vector(0.07,0.07,0.07)


######### LIR
ri1 = ring(pos = vector(0, -0.1,0), axis = vector(-1,0,0), radius = 0.5, thickness = 0.03)
ri2 = ring(pos = vector(-0.02, -0.1,0), axis = vector(-1,0,0), radius = 0.48, thickness = 0.03)
ri3 = ring(pos = vector(-0.04,-0.1,0), axis = vector(-1,0,0), radius = 0.46, thickness = 0.03)
ri4 = ring(pos = vector(-0.06,-0.1,0), axis = vector(-1,0,0), radius = 0.44, thickness = 0.03)
ri5 = ring(pos = vector(-0.08,-0.1,0), axis = vector(-1,0,0), radius = 0.42, thickness = 0.03)
ri6 = ring(pos = vector(-0.1,-0.1,0), axis = vector(-1,0,0), radius = 0.4, thickness = 0.03)
ri7 = ring(pos = vector(-0.12,-0.1,0), axis = vector(-1,0,0), radius = 0.38, thickness = 0.03)
ri8 = ring(pos = vector(-0.14,-0.1,0), axis = vector(-1,0,0), radius = 0.36, thickness = 0.03)
ri9 = ring(pos = vector(-0.16,-0.1,0), axis = vector(-1,0,0), radius = 0.34, thickness = 0.03)
ri10 = ring(pos = vector(-0.18,-0.1,0), axis = vector(-1,0,0), radius = 0.32, thickness = 0.03)
ri11 = ring(pos = vector (-0.20,-0.1,0), axis = vector(-1,0,0), radius = 0.3, thickness = 0.03)
ri12 = ring(pos = vector(-0.22,-0.1,0), axis = vector(-1,0,0), radius = 0.28, thickness = 0.03)

circle_base = shapes.circle(radius= 0.0443)
base_path = [vector(0,0,0), vector(0.03,0,0)]
bse = extrusion(shape = circle_base, path = base_path)
bse.pos = vector(-0.489,-.438, 0.5)
bse.texture = textures.metal


lir = compound([ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10, ri11, ri12])
lir.pos = vector(-0.529,-0.436,0.5)
lir.axis = vector(-1,0,0)
lir.size = vector(0.157,0.157,0.157)
lir.texture = textures.metal

block_above_lir = box(pos = vector(-0.512,-0.35,0.4), size = vector(0.028,0.055,0.04), texture = 'https://i.imgur.com/aZClncF.jpg')
block_on_top = box(pos = vector(-0.512,0.45,0.67), size = vector(0.036,0.058,0.08), texture = 'https://i.imgur.com/aZClncF.jpg')
block_on_top_left = box(pos = vector(-0.512,0.45,-0.67), size = vector(0.036,0.058,0.08), texture = 'https://i.imgur.com/aZClncF.jpg')

block_left_lir = box(pos = vector(-0.512,-0.34,-0.6), size = vector(0.028,0.058,0.03), texture = 'https://i.imgur.com/aZClncF.jpg')

block_left_lir2 = box(pos = vector(-0.512,-0.37,-0.65), size = vector(0.039,0.066,0.05), texture = 'https://i.imgur.com/aZClncF.jpg')









#box_gold_big = box(pos = vector(-0.53, -0.8, 0.18), size = vector(0.3, 0.1, 0.3), color = color.white)

### Right Face

cylinder_rgtface = cylinder(axis = vector(1,0,0), pos = vector(0.25, -0.02,0) , radius = 0.035, size = vector(0.4,0.4,.4), texture = {'file' : textures.wood, 'bumpmap' : bumpmaps.stucco, 'place' : ['sides', 'all']})

cube_extruded2 = box(pos = vector(0.51, 0.028, 0.38), texture = {'file' : "https://i.imgur.com/aZClncF.jpg", 'bumpmap' : bumpmaps.rock}, size = vector(0.01, 0.5, 0.5))

cube_extruded3 = box(pos = vector(0.51, 0.028, -0.38), texture = {'file' : "https://i.imgur.com/aZClncF.jpg", 'bumpmap' : bumpmaps.rock}, size = vector(0.01, 0.5, 0.5))


circular_top_1 = shapes.circle(radius = 0.0353)
path = [vector(0,0,0), vector(0.01,0,0)]
extru_cir_cap_right = extrusion(shape = circular_top_1, path = path)
extru_cir_cap_right.pos = vector(0.649, -0.02,0)

cylin_hori = cylinder(axis = vector(0,0,1), pos = vector(0.5, -0.425, -0.35), radius = 0.075, size = vector(0.7,0.4,0.4), texture = {'file' : textures.wood, 'bumpmap' : bumpmaps.stucco, 'place' : ['sides', 'all']} )
#cylin_disc = disc(pos = vector(1.1, -0.04, 0.05) , radius = 0.0351)


rgt_1 = box(pos = vector(0.7, -0.5, 0.09), size = vector(0.05, 0.13, 0.05))
rgt_2 = box(pos = vector(0.7, -0.5, 0.28), size = vector(0.05, 0.13, 0.05))

top_01 = box(pos = vector(0.7, -0.45, 0.185), size = vector(0.05, 0.05, 0.24) )
top_02 = box(pos = vector(0.7, -0.55, 0.185), size = vector(0.05, 0.05, 0.24) )

outer_frme = compound([rgt_1,rgt_2, top_01, top_02])
outer_frme.size = vector(0.1,0.156, 0.08)

outer_frme.pos = vector(0.5, -0.42, -0.67)
inner_box = box(pos = vector(0.5, -0.42, -0.67), size = vector(0.04, 0.08, 0.08))

outer_frme2 = compound([rgt_1,rgt_2, top_01, top_02])
outer_frme2.size = vector(0.1,0.08, 0.15)
outer_frme2.pos = vector(0.5, -0.42, -0.52)

inner_box2 = box(pos = vector(0.5, -0.42, -0.52), size = vector(0.05, 0.05, 0.1))


box_support_bottom0 = box(pos = vector(0.5, -0.2, -0.686), size = vector(0.08, 0.07, 0.05), texture = 'https://i.imgur.com/aZClncF.jpg')
box_support_bottom1 = box(pos = vector(0.5, 0.253, -0.686), size = vector(0.08, 0.07, 0.05), texture = 'https://i.imgur.com/aZClncF.jpg')
box_support_bottom2 = box(pos = vector(0.5, 0.353, -0.686), size = vector(0.08, 0.07, 0.05), axis = vector(0,0,1), texture = 'https://i.imgur.com/aZClncF.jpg')


### Front face Circular shapes

circular_disc_silver = shapes.circle(radius=0.335)
circular_path = [vector(0,0,0), vector(0,0,0.15)]
disc = extrusion(path = circular_path, shape = circular_disc_silver)
disc.pos = vector(-0.14,0,0.77)
#disc.texture = {'file' : 'https://i.imgur.com/flc2mOj.jpg'}
disc.texture = {'file' : 'https://i.imgur.com/mqJrnUT.jpg'} ### Silver foil light

circular_disc_white = shapes.circle(radius=0.327)
circular_path = [vector(0,0,0), vector(0,0,0.165)]
disc = extrusion(path = circular_path, shape = circular_disc_white)
disc.pos = vector(-0.14,0,0.77)
disc.texture = {'file' : 'https://i.imgur.com/X7okD2B.jpg'}


#disc.texture = textures.meta


circular_disc_small = shapes.circle(radius=0.152)
circular_path_small = [vector(0,0,0), vector(0,0,0.115)]
disc2 = extrusion(path = circular_path_small, shape = circular_disc_small)
disc2.pos = vector(0.335,-0.16,0.77)
disc2.texture = {'file' : 'https://i.imgur.com/X7okD2B.jpg'}


circular_disc_small_silver = shapes.circle(radius=0.157)
circular_path_small = [vector(0,0,0), vector(0,0,0.100)]
disc2 = extrusion(path = circular_path_small, shape = circular_disc_small_silver)
disc2.pos = vector(0.335,-0.16,0.77)
disc2.texture = {'file' : 'https://i.imgur.com/mqJrnUT.jpg'}



#ring_cen = ring(pos = vector(-0.14,0,0.7),axis = vector(0,0,1), radius=0.122, thickness=0.01)
#disc.texture = textures.metal
#disc.size = vector()


#merge_sat = compound([boxx, cy_left, cy_rgt, panel1, panel2])
#cy_left.texture = "https://i.imgur.com/iA8P9ws.jpg"
#cy_rgt.texture = "https://i.imgur.com/iA8P9ws.jpg"
#merge_sat.pos = vector(-1,0,0)
#merge_sat.axis = vector(-1.5, -1.5, 0)
#merge_sat.size = 1
#merge_sat.pos = vector(-30,0,0)
#merge_sat.rotate(angle=pi/4, axis = vector(1, 0, 0))





# Merging every shape ...
'''complete_sat = compound([boxx , cy_left , cy_rgt , panel1, panel2, boxx_mid_left , boxx_top, boxx_bottom_right, boxx_rgt_corner, boxx_rgt_top_corner1 , boxx_rgt_top_corner2 , boxx_top_left, box_left_cylin , box_left_cylin_o , boxx_bottom_left , box_bt_left_cylin , box_bt_left_cylin_o, boxx_top_right , box_top_right_cylin , box_left_cylin_o , boxx_down_right, box_down_right_cylin , box_down_cylin_right_o , triangle_lar , triangle_lar2 , cylinder_topf_ , cube_topf_ , cube_topf_plate , cylinder_topf_2 , cube_topf_2, cube_topf_plate2 , circular_disc3 , circular_disc4 , circular_disc5 , circular_disc6 , boxx_right_face_top_rgt , boxx_right_face_top_rgt_small, boxx_bottom_right_rightf , boxx_bottom_right_rightf_small , boxx_down_left_rgtf, boxx_down_left_rgtf_small , boxx_top_left_rgtf , boxx_top_left_rgtf_small, rec_sur , rec_sur1 , rec_sur2 , rec_sur3 , rec_sur4 , rec_sur5, rec_sur6, rec_sur7 , sph_left , cylinder_leftface , cube_extruded , circular_disc_silver , circular_disc_white , circular_disc_small , circular_disc_small_silver])

'''
#complete_sat.size = vector(1,1,1)

#backlight = local_light(pos = vector(-0,0,-5.79))


##################################   Face down 

sphere_on_left = sphere(pos = vector(0.407, -0.5, 0.3), radius = 0.07, texture = {'file' : "https://i.imgur.com/1uo6oHa.jpg", 'bumpmap' : bumpmaps.stones})
sphere_on_rgt = sphere(pos = vector(0.407, -0.5, -0.3), radius = 0.07, texture = {'file' : textures.wood, 'bumpmap' : bumpmaps.stucco, 'place' : ['sides', 'all']})

funnel_lft = compound([ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10, ri11, ri12])
funnel_lft.pos = vector(0.407, -0.56, 0.35)
funnel_lft.axis = vector(0.4,-1,1)
funnel_lft.size = vector(0.103,0.103,0.103)
#funnel_lft.texture = textures.metal

funnel_rgt = compound([ri1, ri2, ri3, ri4, ri5, ri6, ri7, ri8, ri9, ri10, ri11, ri12])
funnel_rgt.pos = vector(0.425, -0.554, -0.3)
funnel_rgt.axis = vector(1.4,-1.5,-1)
funnel_rgt.size = vector(0.103,0.103,0.103)

rec_sur_bottom = shapes.rectangle(width = 0.548, height = 0.30)
path_rec = [vector(0,0,0), vector(0,0.01,0)]
rec_ext = extrusion(path = path_rec, shape = rec_sur_bottom)
rec_ext.pos = vector(0.27, -0.498, -0.04)


rec_sur_bottom_2 = shapes.rectangle(width = 0.278, height = 0.259)
path_rec1 = [vector(0,0,0), vector(0,0.01,0)]
rec_ext1 = extrusion(path = path_rec1, shape = rec_sur_bottom_2)
rec_ext1.pos = vector(-0.37, -0.498, 0.12)

rec_sur_bottom_3 = shapes.rectangle(width = 0.259, height = 0.358)
path_rec2 = [vector(0,0,0), vector(0,0.01,0)]
rec_ext2 = extrusion(path = path_rec2, shape = rec_sur_bottom_3)
rec_ext2.pos = vector(-0.32, -0.498, 0.5)

rec_sur_bottom_4 = shapes.rectangle(width = 0.643, height = 0.612)
path_rec3 = [vector(0,0,0), vector(0,0.01,0)]
rec_ext3 = extrusion(path = path_rec3, shape = rec_sur_bottom_4)
rec_ext3.pos = vector(-0.193, -0.498, -0.42)

uso = box(pos = vector(-0.15, -0.5, -0.3), size = vector(0.06, 0.06, 0.06), color = color.black)

'''def move_camera():
        while(scene.camera.up != vector(-1,0,0)):
            scene.camera.up = vector(-i,0,0)
            i = i + 0.1  
        

    #scene.camera.up = vector(-1,0,0)


button_widget = button(bind=move_camera, text='Change Orientation')
#button_widget2 = button(bind=move_to_antenna, text='High Gain Antenna', pos = vector(1,1,1))

'''
#############################BG  '''
'''scene.autoscale = False
sphere(pos = vector(0,0,0), texture = "https://i.imgur.com/1nVWbbd.jpg", radius = 50, shininess =0)
scene.range.x = 100
scene.range.y = 100'''



camera_up_toggle = False


def button_click_orient():
    global camera_up_toggle

    if not camera_up_toggle:
        scene.camera.up = vector(-1, 0, 0)  # Change the camera up vector
        camera_up_toggle = True
    else:
        scene.camera.up = vector(0, 1, 0)  # Reset the camera up vector to default
        camera_up_toggle = False

button_widget = button(bind = button_click_orient, text='Change Orientation' , align = 'center')    

'''
a = 20 # Semi-major axis
b = 40 # Semi-minor axis

satellite_angle = 0
satellite_change_angle = 0.01


def rotation():
    x = b * sin(satellite_angle)
    y = -0.07 * a * sin(satellite_angle)
    z = a * cos(satellite_angle)  # Adjust the z coordinate to create an inclined orbit

    satellite_angle += satellite_change_angle

    scene.camera.pos = vector(x, y, z)

    
button_widget = button(bind=rotation , text = 'Rotation', align = 'center')    

'''
while True:
    rate(100)
    print(scene.camera.pos)


    
    #scene.camera.pos = vector(-2,0,0)
    # scene.camera.axis = vector(-1.732,0,0)
    #scene.camera.rotate(0.001, axis=vector(0,1,0))
    #scene.camera.pos = vector(-200,10,10)
    #scene.camera.axis = vector(0,0,1)