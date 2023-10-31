from mcpi.minecraft import Minecraft
import time

print("loc: (150,0,150)")
mc=Minecraft.create()

x = 150
y = 0
z = 150
# pos=mc.player.getTilePos()
# init_x = pos.x
# init_y = pos.y
# init_z = pos.z

def buildMyHouse(init_x,init_y,init_z):
    #floor
    mc.setBlocks(init_x,init_y,init_z,init_x+10,init_y,init_z+10,57)

    # back wall
    for i in range(12):
        for j in range(10):
            mc.setBlock(init_x+i,init_y+j,init_z,57)


    # side walls
    for i in range(10):
        for j in range(10):
            if i>2 and i<6 and j>3 and j<7:
                mc.setBlock(init_x,init_y+j,init_z+1+i,20)
                mc.setBlock(init_x+11,init_y+j,init_z+1+i,20)
            else:
                mc.setBlock(init_x,init_y+j,init_z+1+i,57)
                mc.setBlock(init_x+11,init_y+j,init_z+1+i,57)

    # front wall
    for i in range(12):
        for j in range(10):
            if i>1 and i<5 and j>3 and j<7:
                mc.setBlock(init_x+i,init_y+j,init_z+10,20)
            elif i>7 and i<10 and j<7:
                pass
            else:
                mc.setBlock(init_x+i,init_y+j,init_z+10,57)
        
    # roof
    mc.setBlocks(init_x,init_y+10,init_z,init_x+11,init_y+10,init_z+10,41)


    # vegetation or flowers
    for i in [2,4,5,9]:
        mc.setBlock(init_x-1, init_y, init_z+i, 37)  # Dandelion
        mc.setBlock(init_x+12, init_y, init_z+i, 37)
        mc.setBlock(init_x+i, init_y, init_z+11, 38)  # Poppy


    # table and chairs
    mc.setBlocks(init_x+3, init_y+1, init_z+5, init_x+4, init_y+2, init_z+6, 5)   
    mc.setBlock(init_x+3, init_y+2, init_z+3, 53, 3)  
    mc.setBlock(init_x+4, init_y+2, init_z+3, 53, 3)  
    mc.setBlocks(init_x+3, init_y+1, init_z+3, init_x+4, init_y+1, init_z+3,1)

    # Add indoor lighting
    mc.setBlock(init_x+5, init_y+9, init_z+5, 89)  # Glowstone block on the ceiling

    # roof top tree
    center_x = init_x + 5
    center_y = init_y + 11
    center_z = init_z + 4

    # Create the tree canopy with leaves
    canopy_radius = 3  # You can adjust the radius of the tree canopy
    for x in range(-3, 4):
        for y in range(2, 9):
            for z in range(-3, 5):
                if x**2 + (y - 5)**2 + z**2 <= 3**2:
                    mc.setBlock(center_x + x, center_y + y, center_z + z, 18)  # Oak leaves block
    for i in range(6):
        mc.setBlock(center_x, center_y+i, center_z, 17)  # Oak log block

    mc.setBlock(init_x+6, init_y+11, init_z+5, 40)


buildMyHouse(150,0,150)
# buildMyHouse(150,0,180)

mc.player.setPos(150,0,140)