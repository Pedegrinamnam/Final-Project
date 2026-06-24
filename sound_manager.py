import pygame




# Еее, мьюзик
import pygame


class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.current_music = None
        self.music_volume = 0.5
        self.sound_volume = 0.5

    def play_music(self, path):
        if self.current_music == path:
            return
        self.current_music = path
        pygame.mixer.music.stop()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(-1)

    # Запустить музыку
    def play_music(self, path):
        if self.current_music == path:
            return

        self.current_music = path

        pygame.mixer.music.load(path)
        pygame.mixer.music.set_volume(self.music_volume)
        pygame.mixer.music.play(-1)


    def stop_music(self):
        pygame.mixer.music.stop()
        self.current_music = None


    def set_music_volume(self, volume):
        self.music_volume = volume
        pygame.mixer.music.set_volume(volume)


    def play_sound(self, path):
        sound = pygame.mixer.Sound(path)
        sound.set_volume(self.sound_volume)
        sound.play()
