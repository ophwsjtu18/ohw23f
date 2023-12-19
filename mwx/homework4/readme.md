# 在minecraft中建房子
---
## 代码

```
{
import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

def buildhouse(x,y,z):
    print(x,y,z)
    mc.postToChat("X: " + str(x) + " Y: " + str(y) + " Z: " + str(z))
    mc.setBlocks(x,y+1,z,x+13,y+1,z+13,4)
    mc.setBlocks(x-1,y,z-1,x+14,y,z+14,4)
    mc.setBlocks(x+1,y+2,z+1,x+12,y+13,z+12,1)
    mc.setBlocks(x+2,y+3,z+2,x+11,y+12,z+11,0)
    mc.setBlocks(x+1,y+2,z+1,x+1,y+13,z+1,17)
    mc.setBlocks(x+12,y+2,z+1,x+12,y+13,z+1,17)
    mc.setBlocks(x+1,y+2,z+12,x+1,y+13,z+12,17)
    mc.setBlocks(x+12,y+2,z+12,x+12,y+13,z+12,17)
    mc.setBlocks(x+1,y+13,z+1,x+12,y+13,z+12,17)
    mc.setBlocks(x+3,y+8,z+1,x+5,y+10,z+1,20)
    mc.setBlocks(x+8,y+8,z+1,x+10,y+10,z+1,20)
    mc.setBlocks(x+3,y+8,z+12,x+5,y+10,z+12,20)
    mc.setBlocks(x+8,y+8,z+12,x+10,y+10,z+12,20)
    mc.setBlocks(x+1,y+8,z+3,x+1,y+10,z+5,20)
    mc.setBlocks(x+1,y+8,z+8,x+1,y+10,z+10,20)
    mc.setBlocks(x+12,y+8,z+3,x+12,y+10,z+5,20)
    mc.setBlocks(x+12,y+8,z+8,x+12,y+10,z+10,20)
    mc.setBlocks(x+6,y+3,z+1,x+7,y+5,z+1,0)
    for i in range(7):
        mc.setBlocks(x+6-i,y+20-i,z+6-i,x+9+i-2,y+20-i,z+7+i,5)


buildhouse(280,60,280)

}
```
---
