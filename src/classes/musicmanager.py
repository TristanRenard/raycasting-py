import pygame

class MusicManager:
    def __init__(self,music_path):
        pygame.mixer.init()
        self.music_path = music_path
        self.music = pygame.mixer.music.load(self.music_path)
        self.music_playing = False
        self.pos = None

    def play_music(self):
        self.music = pygame.mixer.music.load(self.music_path)
        pygame.mixer.music.play(-1)
        self.music_playing = True

    def unloaded(self):
        pygame.mixer.music.unload()

    def pause_music(self):
        pygame.mixer.music.pause()
        self.music_playing = False

    def resume_music(self):
        pygame.mixer.music.unpause()
        self.music_playing = True

    def stop_music(self):
        pygame.mixer.music.stop()
        self.music_playing = False

    def is_playing(self):
        return self.music_playing

    def get_music_path(self):
        return self.music_path

    def get_music_length(self):
        return pygame.mixer.music.get_length()

    def get_music_position(self):
        self.pos = pygame.mixer.music.get_pos()
        return self.pos

    def set_music_position(self):
        pygame.mixer.music.set_pos(self.pos)

    def set_volume(self, volume):
        pygame.mixer.music.set_volume(volume)

    def get_volume(self):
        return pygame.mixer.music.get_volume()