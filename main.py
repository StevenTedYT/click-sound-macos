from pynput import mouse
import pygame

pygame.mixer.init()
volume = 0.25

click_sound_input = pygame.mixer.Sound('click_sound_input.wav')
click_sound_output = pygame.mixer.Sound('click_sound_output.wav')

click_sound_input.set_volume(volume)
click_sound_output.set_volume(volume)

def on_click(x, y, button, pressed):
    if pressed:
        click_sound_input.play()
    else:
        click_sound_output.play()

with mouse.Listener(on_click=on_click) as listener:
    listener.join()