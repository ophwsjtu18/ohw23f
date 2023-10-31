from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
pos=mc.player.getTilePos()
print("player pos is",pos)

# mc.setBlock(pos.x,pos.y,pos.z,35)
# for i in range(10):
#     mc.setBlock(pos.x,pos.y+i,pos.z)

# stayed_time=0
# while True:
#     print("stay_time"+str(stayed_time))
#     time.sleep(0.5)
#     pos=mc.player.getTilePos()
#     mc.postToChat("please go to home x=98 y=30 z=234 for 15s to fly")
#     mc.postToChat("x:"+str(pos.x)+"y:"+str(pos.y)+"z:"+str(pos.z)) 
#     if pos.x==98 and pos.z==234 and pos.y==30:
#         mc.postToChat("welcome home,count down"+str(30-stayed_time))
#         stayed_time=stayed_time+1
#         if stayed_time>=0:
#             mc.player.setTilePos(58,26,-103)
#             stayed_time=0
#     else:
#         stayed_time=0
        

height = 7

for level in range(height):
    for i in range(level,2*(height-2)-level+1):
        for j in range(level,2*(height-2)-level+1):
            mc.setBlock(pos.x+i,pos.y+level,pos.z+j,41)

print("Pyramid built!")