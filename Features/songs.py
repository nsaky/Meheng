import pygame
import keyboard
import time

def play_song():
    try:
        pygame.init()
        pygame.mixer.music.load('./Resouces/Songs/Song_MSD.mp3')
        pygame.mixer.music.play()
        while True:
            if keyboard.is_pressed('space'):
                print("Spacebar pressed, stopping the music.")
                pygame.mixer.music.stop()  # Stop the music
                break
            time.sleep(0.1)
        return "Played your favourite song"
    except:
        return "unable to play the song at the moment."

