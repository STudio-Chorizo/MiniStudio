from asyncio.windows_events import NULL
from dependencies.engine.Untils.vector import Magnitude
import dependencies.engine.engine as eng
import glm
import math

from dependencies.moderngl.model import ExtendedBaseModel


class GameObject:
    def __init__(self, pos = (0, 0, 0), rot = (0, 0, 0), scale = (1, 1, 1)):
        self.position = glm.vec3(pos)
        self.rotation = glm.vec3(rot)
        self.scale = scale
        self.UID = "-1"
        self.isActive = True

        self.forward = glm.vec3(0, 0, 1)
        self.right = glm.vec3(1, 0, 0)
        self.up = glm.vec3(0, 1, 0)

        self.isCollide = False
        self.collideBox = NULL
        self.velocity =  (0, 0, 0)

        self.forward = glm.vec3(0, 0, 1)
        self.right = glm.vec3(1, 0, 0)
        self.up = glm.vec3(0, 1, 0)
        self.UpdateLocalAxis()
        self.model = NULL

    def SetModel(self, name):
        if(eng.Engine.Instance == NULL) : return
        
        text_id = eng.Engine.Instance.graphicEngine.mesh.texture.AddTexture(name)
        eng.Engine.Instance.graphicEngine.mesh.vao.vbo.AddVBO(name)
        eng.Engine.Instance.graphicEngine.mesh.vao.AddVAO(name)
        self.model = ExtendedBaseModel(eng.Engine.Instance.graphicEngine, name, text_id, self.position, glm.radians(self.rotation), self.scale)
        eng.Engine.Instance.graphicEngine.scene.AddObject(self.model)
        
    def SetCollider(self, size):
        self.isCollide = True
        self.collideBox = size

    def OnCollide(self, colider):
        pass

    def Raycast(self, dir, max = 150):
        """Envoie un rayon depuis l'objet.
        return (hitObj, hitPoint) || False"""
        col = dict(eng.Engine.Instance.gameObjects)
        point = (self.position[0], self.position[1], self.position[2])
        ray = dir * 0.1
        collider = dict(col)
        for obj in collider:
            o = eng.Engine.Instance.gameObjects[obj]
            if(Magnitude(self.position - o.position) > max or o.UID == self.UID) : 
                col.pop(obj)

        collider = dict(col)
        for i in range(0, max * 10, 1):
            point += ray
            for obj in collider:
                o = eng.Engine.Instance.gameObjects[obj]
                if(Magnitude(self.position - o.position) < i * 0.1) : 
                    #col.pop(obj)
                    continue

                axisIn = 0
                for k in range(3):
                    pos2 = o.position[k] + o.collideBox[k]
                    posn2 = o.position[k] - o.collideBox[k]
                    #if(point[i] > posn2 and point[i] < pos2 or point[i] > posn2 and point[i] < pos2 or
                    #pos2 > point[i] and pos2 < point[i] or posn2 > point[i] and posn2 < point[i] ) : axisIn += 1
                    if(point[k] > posn2 and point[k] < pos2) : axisIn += 1
                if(axisIn >= 3) : return (o, point)
                
            collider = dict(col)
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
    
    def Update(self):
        
        if(self.model != NULL) : 
            self.model.pos = self.position
            self.model.rot = self.rotation / 180 * math.pi
            self.model.m_model = self.model.get_model_matrix()
