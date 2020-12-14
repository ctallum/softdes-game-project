import sys
import pygame
from pygame.locals import *

class Doors:
    def __init__(self):
        self.player_at_door = False
        self.height_raised = 0
        self.door_open = False

        self.load_images()
        self.make_rects()
    
    def load_images(self):
        self.frame_image = pygame.image.load("data/door_images/door_frame.png")
        self.door_background = pygame.image.load("data/door_images/door_background.png")

    def make_rects(self):
        self.rect = pygame.Rect(self.door_location[0], self.door_location[1],
                                self.door_image.get_width(), self.door_image.get_height())

    def get_door(self):
        return self.rect

    def is_door_open(self):
        return self.door_open

    def try_raise_door(self):
        DOOR_SPEED = 1.5
        if self.player_at_door and not self.door_open:
            self.door_location = (self.door_location[0], self.door_location[1] - DOOR_SPEED)
            self.height_raised += DOOR_SPEED
            if self.height_raised >= 31:
                self.door_open = True
        elif not self.player_at_door:
            if self.height_raised > 0:
                self.height_raised -= DOOR_SPEED
                self.door_location = (self.door_location[0], self.door_location[1] + DOOR_SPEED)
                self.door_open = False
    

class FireDoor(Doors):
    def __init__(self, door_location, background_location, frame_location):
        self.door_location = door_location
        self.background_location = background_location
        self.frame_location = frame_location
        self.door_image = pygame.image.load("data/door_images/fire_door.png")
        super().__init__()

class WaterDoor(Doors):
    def __init__(self, door_location, background_location, frame_location):
        self.door_location = door_location
        self.background_location = background_location
        self.frame_location = frame_location
        self.door_image = pygame.image.load("data/door_images/water_door.png")
        super().__init__()