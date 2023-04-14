from asyncio.windows_events import NULL
import glm
import pygame as pg
import math
from dependencies.engine.engine import *
from dependencies.engine.gameobject import *

FOV = 50  # deg
NEAR = 0.1
FAR = 100
SPEED = 0.005
SENSITIVITY = 0.04


class Camera:
    def __init__(self, app, position=(0, 0.2, 0.5), yaw=-90, pitch=-10, roll=0):
        self.target = NULL
        self.app = app
        self.aspect_ratio = app.WIN_SIZE[0] / app.WIN_SIZE[1]
        self.position = glm.vec3(position)
        self.up = glm.vec3(0, 1, 0)
        self.right = glm.vec3(1, 0, 0)
        self.forward = glm.vec3(0, 0, -1)
        self.yaw = yaw
        self.pitch = pitch
        self.roll = roll
        # view matrix
        self.m_view = self.get_view_matrix()
        # projection matrix
        self.m_proj = self.get_projection_matrix()

    def update_camera_vectors(self):
        if eng.Engine.Instance.deltaTime > 0:
            self.move_position = (self.position - self.prev_position)
            if math.sqrt(self.move_position.x**2 + self.move_position.y**2 + self.move_position.z**2) <= 0.1:
                self.position = self.prev_position
            else:
                self.position += self.move_position * min(eng.Engine.Instance.deltaTime*2, 1)

            self.move_yaw = (self.yaw - self.prev_yaw)
            if self.move_yaw <= 0.1:
                self.yaw = self.prev_yaw
            else:
                self.yaw += self.move_yaw * min(eng.Engine.Instance.deltaTime*2, 1)

            self.move_pitch = (self.pitch - self.prev_pitch)
            if self.move_pitch <= 0.1:
                self.pitch = self.prev_pitch
            else:
                self.pitch += self.move_pitch * min(eng.Engine.Instance.deltaTime*2, 1)

            self.move_roll = (self.roll - self.prev_roll)
            if self.move_roll <= 0.1:
                self.roll = self.prev_roll
            else:
                self.roll += self.move_roll * min(eng.Engine.Instance.deltaTime*2, 1)

        yaw, pitch, roll = glm.radians(self.yaw), glm.radians(self.pitch), glm.radians(self.roll)

        self.forward.x = glm.cos(yaw) * glm.cos(pitch)
        self.forward.y = glm.sin(pitch)
        self.forward.z = glm.sin(yaw) * glm.cos(pitch)

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(glm.sin(-roll), glm.cos(-roll), 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    def update(self):
        self.prev_position = self.target.camera_pos
        self.prev_yaw = self.target.camera_yaw
        self.prev_pitch = self.target.camera_pitch
        self.prev_roll = self.target.camera_roll

        self.update_camera_vectors()
        self.m_view = self.get_view_matrix()

    def get_view_matrix(self):
        return glm.lookAt(self.position, self.position + self.forward, self.up)

    def get_projection_matrix(self):
        return glm.perspective(glm.radians(FOV), self.aspect_ratio, NEAR, FAR)




















