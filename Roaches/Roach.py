import pygame as py
from Notification import Subscriber
import math
import random as rand


class Behaviors:
    FLEE = 0
    WANDER = 1


class Roach(Subscriber):
    def __init__(self, surface, x=0, y=0):
        super().__init__()
        self._behaviors = {Behaviors.FLEE: self.run_away, Behaviors.WANDER: self.wander}
        self._speeds = {Behaviors.FLEE: 3, Behaviors.WANDER: 1}
        self.state = Behaviors.WANDER
        self.surface = surface
        self.location = (x, y)
        self.velocity = (0, 0)
        self.flee_location = (-50, 200)
        self.roach_size = 10
        self.roach_color = (255, 255, 255)
        self.target = None
        self.target_size = 5
        self.target_proximity = self.roach_size
        
    # Private Methods
    
    def _get_random_target(self, start_x, stop_x, start_y, stop_y):
        x = rand.randint(start_x, stop_x)
        y = rand.randint(start_y, stop_y)
        return x, y
    
    def _get_next_location(self):
        x = self.location[0] + (self.velocity[0] * self._speeds[self.state])
        y = self.location[1] + (self.velocity[1] * self._speeds[self.state])
        return x, y

    def _get_velocity(self):
        dist = self.get_distance_to_target()
        x = (self.target[0] - self.location[0]) / dist
        y = (self.target[1] - self.location[1]) / dist
        return x, y
    
    def _get_off_screen_target(self):
        # TODO : In Progress
        return self.flee_location
    
    def _is_on_screen(self):
        if self.location[0] < 0 or self.location[0] > self.surface.get_width():
            return False
        if self.location[1] < 0 or self.location[1] > self.surface.get_height():
            return False
        return True

    def _is_target_reached(self):
        return self.get_distance_to_target() <= self.target_proximity
    
    def _move_to_target(self):
        self.location = self._get_next_location()

    def _set_state(self, state: int):
        if type(state) != int:
            raise TypeError("state must be of tye int.")
        if state not in self._behaviors:
            raise KeyError("behavior state is not valid.")
        self.state = state
        self.target = None
    
    # Public API
    def get_target_location(self):
        return self.target

    def set_target_location(self, target: tuple):
        if type(target) is not tuple:
            raise TypeError("target must be uf type tuple.")
        if len(target) != 2:
            raise ValueError("target tuple must be formatted as (x, y).")
        if type(target[0]) != int or type(target[1]) != int:
            raise ValueError("values for x and y must be ints")
        self.target = target

    def get_distance_to_target(self):
        return math.dist((self.location[0], self.location[1]), (self.target[0], self.target[1]))
    
    def run_away(self):
        # TODO : in progress
        if self.target is None:
            self.set_target_location(self._get_off_screen_target())
            self.velocity = self._get_velocity()

        if self._is_target_reached():
            self.velocity = (0, 0)
        self._move_to_target()
    
    def wander(self):
        if self.target is None:
            self.set_target_location(self._get_random_target(0, self.surface.get_width(), 0, self.surface.get_height()))
            self.velocity = self._get_velocity()

        self._move_to_target()
        if self._is_target_reached():
            self.target = None
        
    def run_current_behavior(self):
        self._behaviors[self.state]()
    
    def get_notification(self, **kwargs):
        print("notified")
        if 'state' in kwargs.keys():
            if kwargs['state'] == 0:
                self._set_state(Behaviors.WANDER)
            elif kwargs['state'] == 1:
                self._set_state(Behaviors.FLEE)

    def draw(self):
        py.draw.circle(self.surface, self.roach_color, (self.location[0], self.location[1]), self.roach_size)

        if self.target:
            rect = py.rect.Rect(self.target[0], self.target[1], self.target_size, self.target_size)
            py.draw.ellipse(self.surface, (255, 255, 0), rect)
