from mcpi.minecraft import Minecraft
import time
import os
import pygame

pygame.mixer.init()

sound_path = r'haoyunlai.wav'
pygame.mixer.music.load(sound_path)

# try:
#     pygame.mixer.music.play()
#     while pygame.mixer.music.get_busy() == True:
#         continue
# except Exception as e:
#     print(f"An error occurred while playing the sound: {e}")

mc = Minecraft.create()

target_location = (158, 2, 162)



def play_sound_at_door():
    try:
        pygame.mixer.music.play()
        time.sleep(12)
        pygame.mixer.music.stop()
    except Exception as e:
        print(f"An error occurred while playing the sound: {e}")

# play_sound_at_door()

while True:

    pos = mc.player.getTilePos()
    
    if pos.x == target_location[0] and pos.y == target_location[1] and pos.z == target_location[2]:
        play_sound_at_door()

    time.sleep(0.1)
