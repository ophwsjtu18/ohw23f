from mcpi.minecraft import Minecraft

mc=Minecraft.create()
pos=mc.player.getTilePos()
mc.postToChat("250, 100, 200")

# 外墙
mc.setBlocks(250, 100, 200, 270, 120, 220, 1)

# 掏空
mc.setBlocks(252, 100, 202, 268, 120, 218, 0)

# 门
mc.setBlocks(258, 100, 200, 262, 105, 202, 0)

# 地板
mc.setBlocks(252, 100, 202, 268, 100, 218, 57)

# 天花板
mc.setBlocks(248, 121, 198, 272, 121, 222, 29)

# 灯
mc.setBlocks(252, 119, 202, 268, 119, 218, 20)
mc.setBlocks(252, 120, 202, 268, 120, 218, 11)

# 窗户
mc.setBlocks(250, 105, 205, 251, 115, 215, 20)
mc.setBlocks(269, 105, 205, 270, 115, 215, 20)