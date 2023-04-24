from dependencies.engine.Untils.vector import Magnitude
from asyncio.windows_events import NULL
import dependencies.engine.engine as eng
import glm
import math

from dependencies.moderngl.model import ExtendedBaseModel


class GameObject(ExtendedBaseModel):
    def __init__(self, pos = (0, 0, 0), rot = (0, 0, 0), scale = (1, 1, 1)):
        self.position = glm.vec3(pos)
        self.modelRotation = glm.vec3(rot)
        self.rotation = glm.vec3(0, 0, 0)
        self.scale = scale
        self.UID = "-1"

        self.isCollide = False
        self.collideBox = None
        self.velocity = (0, 0, 0)

        self.forward = (0, 0, 1)
        self.right = (1, 0, 0)
        self.up = (0, 1, 0)
        self.UpdateLocalAxis()

        self.model = None

    def SetModel(self, name):
        if(eng.Engine.Instance == None) : return
        
        text_id = eng.Engine.Instance.graphicEngine.mesh.texture.AddTexture(name)
        eng.Engine.Instance.graphicEngine.mesh.vao.vbo.AddVBO(name)
        eng.Engine.Instance.graphicEngine.mesh.vao.AddVAO(name)
        self.model = ExtendedBaseModel(eng.Engine.Instance.graphicEngine, name, text_id, self.position, glm.radians(self.rotation), self.scale)
        eng.Engine.Instance.graphicEngine.scene.AddObject(self.model)
        
    def Destroy(self):
        eng.Engine.Instance.graphicEngine.scene.RemoveObject(self.model)

    def SetCollider(self, size):
        self.isCollide = True
        self.collideBox = size

    def OnCollide(self, colider):
        pass

    def Raycast(self, dir, max = 150):
        """Envoie un rayon depuis l'objet.
        return (hitObj, hitPoint) || False"""
        collider = col = eng.Engine.Instance.gameObjects
        point = (self.position[0], self.position[1], self.position[2])
        ray = dir * 0.1
        #Optimisation sans prendre compte de l'intérieur de la collideBox
        for i in range(0, max * 10, 1):
            j = 0
            for obj in collider:
                o = eng.Engine.Instance.gameObjects[obj]
                if(Magnitude(self.position - o.position) > max or Magnitude(self.position - o.position) < i or o.UID == self.UID) : 
                    #col.pop(j)
                    continue
                point += ray
                
                axisIn = 0
                for i in range(3):
                    pos2 = o.position[i] + o.collideBox[i]
                    posn2 = o.position[i] - o.collideBox[i]
                    if(point[i] > posn2 and point[i] < pos2 or point[i] > posn2 and point[i] < pos2 or
                    pos2 > point[i] and pos2 < point[i] or posn2 > point[i] and posn2 < point[i] ) : axisIn += 1
                if(axisIn == 3) : return (o, point)
                
                j += 1
            collider = col
        return False

    def UpdateLocalAxis(self):
        pitch, yaw, roll = glm.radians(self.rotation[0]), glm.radians(self.rotation[1]), glm.radians(self.rotation[2])

        self.forward = (-glm.sin(yaw) * glm.cos(pitch), glm.sin(pitch), glm.cos(yaw) * glm.cos(pitch))

        self.forward = glm.normalize(self.forward)
        self.right = glm.normalize(glm.cross(self.forward, glm.vec3(glm.sin(-roll), glm.cos(-roll), 0)))
        self.up = glm.normalize(glm.cross(self.right, self.forward))

    # Utiliser cette fonction pour avoir les collision
    def Move(self, translation: tuple) -> None:
        """Fonction pour déplacer l'objet et permettre les collision\n
        translation: (x, y, z) déplacement de l'objet"""
        self.position += translation
        self.velocity = translation
    
    # Utiliser cette fonction pour définir la rotation
    def Rotate(self, angle: float, axis: tuple) -> None:
        """Fonction pour faire tourner l'objet\n
        orientation: (x, y, z) orientation de l'objet"""
        self.rotation += angle * axis
    
    def LookAt(self, target):
        nForward = math.sqrt(self.forward[0] ** 2 + self.forward[1] ** 2 + self.forward[2] ** 2)
        posTarget = target - self.position
        nTarget = math.sqrt(posTarget[0] ** 2 + posTarget[1] ** 2 + posTarget[2] ** 2)
        if(nTarget == 0) : return
        
        angle = (self.forward[0] * posTarget[0] + self.forward[1] * posTarget[1] + self.forward[2] * posTarget[2]) / (nForward * nTarget)
        angle = math.acos(angle)
        angle = math.degrees(angle)
        angle = math.ceil(angle)
        axis = glm.vec3(0, 0, 0)
        if(angle != 180 and angle != 0 and angle != -180):
            axis = -glm.vec3(self.forward[1] * posTarget[2] - self.forward[2] * posTarget[1]
                    ,self.forward[2] * posTarget[0] - self.forward[0] * posTarget[2]
                    ,self.forward[0] * posTarget[1] - self.forward[1] * posTarget[0])
            axis /= math.sqrt(axis[0] ** 2 + axis[1] ** 2 + axis[2] ** 2)

        self.Rotate(angle, axis)


    def Update(self):
        self.UpdateLocalAxis()
        if(self.model != None) : 
            self.model.pos = self.position
            self.model.rot = glm.radians(self.rotation + self.modelRotation)
            self.model.m_model = self.model.get_model_matrix()
from asyncio.windows_events import NULL
import dependencies.engine.engine as Eng
import glm
import math

from dependencies.moderngl.model import ExtendedBaseModel


class GameObject(ExtendedBaseModel):
    def __init__(self, model_name = "cube", pos = (0, 0, 0), rot = (0, 0, 0), scale = (1, 1, 1)):
        self.position = glm.vec3(pos)
        self.prev_position = self.position
        self.camera_pos = self.position + glm.vec3([0, 0.2, 0.5])
        self.rotation = glm.vec3(rot)
        self.prev_rotation = self.rotation
        self.camera_yaw = self.rotation[1] - 90
        self.camera_pitch = self.rotation[0] - 10
        self.camera_roll = self.rotation[2]
        self.scale = scale
        self.UID = "-1"

        self.isCollide = False
        self.collideBox = NULL

        self.model = NULL
        self.SetModel(model_name, pos, rot, scale)

    def SetModel(self, name, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        if(Eng.Engine.Instance == NULL) : return
        
        text_id = Eng.Engine.Instance.graphicEngine.mesh.texture.AddTexture(name)
        Eng.Engine.Instance.graphicEngine.mesh.vao.vbo.AddVBO(name)
        Eng.Engine.Instance.graphicEngine.mesh.vao.AddVAO(name)
        self.model = ExtendedBaseModel(Eng.Engine.Instance.graphicEngine, name, text_id, pos, rot, scale)
        Eng.Engine.Instance.graphicEngine.scene.AddObject(self.model)
        
    # Utiliser cette fonction pour avoir les collision
    def Move(self, translation: tuple, timing: int = 0, camTranslation: tuple = glm.vec3([0, 0, 0])) -> None:
        """Fonction pour déplacer l'objet et permettre les collision\n
        translation: (x, y, z) déplacement de l'objet"""
        self.prev_position += translation
        self.velocity = translation
        self.camera_pos += camTranslation
    
    # Utiliser cette fonction pour avoir la rotation
    def Rotate(self, rotation: tuple, camRotation: tuple = (0, 0, 0)) -> None:
        """Fonction pour tourner l'objet\n
        rotation: (x, y, z) rotation de l'objet"""
        self.prev_rotation += rotation
        self.camera_yaw += camRotation[0]
        self.camera_pitch += camRotation[1]
        self.camera_roll += camRotation[2]
        
    # Utiliser cette fonction pour avoir les collision
    def SetPos(self, position: tuple, camPosition: tuple = glm.vec3([0, 0.2, 0.5])) -> None:
        """Fonction pour définir un position de l'objet\n
        translation: (x, y, z) position de l'objet"""
        self.prev_position = position
        self.camera_pos = camPosition
    
    # Utiliser cette fonction pour avoir la rotation
    def SetRot(self, orientation: tuple, camOrientation: tuple = (-90, -10, 0)) -> None:
        """Fonction pour définir une rotation de l'objet\n
        orientation: (x, y, z) orientation de l'objet"""
        self.prev_rotation = orientation
        self.camera_yaw = camOrientation[0]
        self.camera_pitch = camOrientation[1]
        self.camera_roll = camOrientation[2]
    
    def SyncPosCamera(self, position: tuple = glm.vec3([0, 0.2, 0.5])) -> None:
        self.camera_pos = glm.vec3(self.position) + position
    
    def SyncRotCamera(self, camOrientation: tuple = (-90, -10, 0)) -> None:
        self.camera_yaw = self.rotation[1]*10 + camOrientation[0]
        self.camera_pitch = self.rotation[0]*10 + camOrientation[1]
        self.camera_roll = self.rotation[2]*10 + camOrientation[2]
    
    def Update(self):
        if Eng.Engine.Instance.deltaTime > 0:
            self.move_position = self.position - self.prev_position
            if math.sqrt(self.move_position.x**2 + self.move_position.y**2 + self.move_position.z**2) <= 5:
                self.position = self.prev_position
            else:
                self.position -= self.move_position * 0.5
        self.model.pos = self.position

        if Eng.Engine.Instance.deltaTime > 0:
            self.move_rotation = self.rotation - self.prev_rotation
            if math.sqrt(self.move_rotation.x**2 + self.move_rotation.y**2 + self.move_rotation.z**2) <= 0.01:
                self.rotation = self.prev_rotation
            else:
                self.rotation -= self.move_rotation * 0.5
        self.model.rot = self.rotation
        

        self.model.m_model = self.model.get_model_matrix()