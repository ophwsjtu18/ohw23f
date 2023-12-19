from mcpi.minecraft import Minecraft
import time
import pygame

mc=Minecraft.create()
pos=mc.player.getTilePos()
print("player pos is",pos)

def buildhouse(a,b,c):
    #深色橡木门197
    #打地基
    mc.setBlocks(a,b,c+5,a+15,b-3,c+16,155)
    mc.setBlocks(a,b,c,a,b-3,c+5,155)
    mc.setBlocks(a,b,c,a+15,b-3,c,155)
    mc.setBlocks(a+15,b,c,a+15,b-3,c+12,155)
    mc.setBlocks(a,b-3,c,a+15,b-3,c+16,155)
    mc.setBlocks(a+1,b,c+1,a+9,b-2,c+4,9)
    mc.setBlocks(a+10,b,c+1,a+14,b-2,c+11,9)

    #第一层房柱
    mc.setBlocks(a,b,c+5,a,b+4,c+5,155)
    mc.setBlocks(a+9,b,c+5,a+9,b+4,c+5,155)
    mc.setBlocks(a+9,b,c+12,a+9,b+4,c+12,155)
    mc.setBlocks(a+15,b,c+12,a+15,b+4,c+12,155)
    mc.setBlocks(a+15,b,c+16,a+15,b+4,c+16,155)
    mc.setBlocks(a,b,c+16,a,b+4,c+16,155)

    #铺第一层房顶
    mc.setBlocks(a,b+4,c+5,a+9,b+4,c+16,155)
    mc.setBlocks(a+9,b+4,c+12,a+15,b+4,c+16,155)

    #门那一面
    mc.setBlocks(a+15,b+1,c+13,a+15,b+3,c+13,162,13)
    mc.setBlocks(a+15,b+1,c+15,a+15,b+3,c+15,162,13)
    mc.setBlock(a+15,b+3,c+14,162,13)
    mc.setBlock(a+15,b+2,c+14,197)
    #mc.setBlock(a+15,b+1,c+14,64)

    #门旁边的小墙
    mc.setBlocks(a+12,b+1,c+12,a+14,b+3,c+12,20)
    mc.setBlocks(a+9,b+1,c+12,a+11,b+3,c+12,162,13)

    #旁边的小墙
    mc.setBlocks(a+9,b+1,c+6,a+9,b+3,c+9,20)
    mc.setBlocks(a+9,b+1,c+10,a+9,b+3,c+11,162,13)

    #旁边的小墙 泳池门
    mc.setBlocks(a+5,b+1,c+5,a+8,b+3,c+5,126,5)
    mc.setBlocks(a+4,b+1,c+5,a+1,b+3,c+5,155)
    mc.setBlocks(a+1,b+3,c+5,a+8,b+3,c+5,126,5)

    #旁边的小墙
    mc.setBlocks(a,b+1,c+14,a,b+3,c+16,20)
    mc.setBlocks(a,b+1,c+6,a,b+3,c+13,155)

    #旁边的小墙
    mc.setBlocks(a+1,b+1,c+16,a+3,b+3,c+16,20)
    mc.setBlocks(a+4,b+1,c+16,a+14,b+3,c+16,155)
    mc.setBlocks(a+2,b+1,c+5,a+3,b+2,c+5,0)
    mc.setBlocks(a+2,b,c+4,a+3,b-3,c+4,155)
    mc.setBlocks(a+2,b-1,c+3,a+3,b-3,c+3,155)
    mc.setBlocks(a+2,b-2,c+2,a+3,b-3,c+2,155)

    #第二层屋顶
    mc.setBlocks(a,b+5,c+16,a+9,b+8,c+16,155)
    mc.setBlocks(a,b+8,c+5,a+9,b+8,c+16,155)

    #第二层
    mc.setBlocks(a+1,b+5,c+16,a+2,b+7,c+16,20)
    mc.setBlocks(a,b+5,c+14,a,b+7,c+16,20)
    mc.setBlocks(a,b+5,c+13,a,b+7,c+10,155)
    mc.setBlocks(a+9,b+5,c+15,a+9,b+7,c+10,162,13)
    mc.setBlocks(a+1,b+5,c+10,a+8,b+7,c+10,20)
    mc.setBlocks(a+4,b+5,c+10,a+5,b+6,c+10,0)
    mc.setBlocks(a+9,b+5,c+14,a+9,b+6,c+14,0)
    #mc.setBlocks(a+4,b+5,c+10,a+5,b+6,c+10,197)#放门

    #第二层放玻璃板102
    d=102
    mc.setBlocks(a,b+5,c+5,a,b+5,c+9,d)
    mc.setBlocks(a+9,b+5,c+5,a+9,b+5,c+9,d)
    mc.setBlocks(a,b+5,c+5,a+9,b+5,c+5,d)
    mc.setBlocks(a+10,b+5,c+12,a+15,b+5,c+12,d)
    mc.setBlocks(a+10,b+5,c+16,a+15,b+5,c+16,d)
    mc.setBlocks(a+15,b+5,c+12,a+15,b+5,c+16,d)

    #第二层铺草
    mc.setBlocks(a+1,b+5,c+6,a+8,b+5,c+8,171,5)
    mc.setBlocks(a+10,b+4,c+13,a+14,b+4,c+15,2)

    #第二层装饰
    mc.setBlocks(a+4,b+5,c+7,a+5,b+5,c+8,201)
    #mc.setBlock(a+7,b+6,c+7,138)灯
    #mc.setBlock(a+4,b+5,c+7,203)#需转向
    mc.setBlocks(a+7,b+5,c+8,a+7,b+5,c+7,205)
    mc.setBlocks(a+2,b+5,c+8,a+2,b+5,c+7,205)

    mc.setBlocks(a+11,b+5,c+13,a+14,b+5,c+15,37)

    #放门
    mc.setBlock(a+15,b+2,c+14,197)
    

buildhouse(50,0,50)
# while(1):
#     pos=mc.player.getTilePos()
#     print("player pos is",pos)
#     if pos.x==-41 and pos.y==56 and pos.z==-808:
#         print("到达")
#         pygame.mixer.init()
#         pygame.mixer.music.load("minecraft_m3_all\kenan.mp3")
#         pygame.mixer.music.play()
#         while pygame.mixer.music.get_busy() == True:
#             continue
