from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
pos=mc.player.getTilePos()
print("player pos is",pos)
mc.player.setTilePos(140,0,140)
for i in range(0,10):
    for j in range(0,10):
        mc.setBlock(120+i, 0, 120+j, 57)
        mc.setBlock(120 + i, 9, 120 + j, 152)
for k in range(1,9):
    for i in range(0, 10):
        mc.setBlock(120 + i, k, 129, 56)
        mc.setBlock(120 + i, k, 120, 56)
        mc.setBlock(120, k, 120 + i, 56)
        mc.setBlock(129, k, 120 + i, 56)
for k in range(1, 3):
    for i in range(4, 6):
        mc.setBlock(129, k, 120 + i, 0)
for k in range(5, 7):
    for i in range(4, 6):
        mc.setBlock(120 + i, k, 129, 0)
        mc.setBlock(120 + i, k, 120, 0)
        mc.setBlock(120, k, 120 + i, 0)
        mc.setBlock(129, k, 120 + i, 0)


