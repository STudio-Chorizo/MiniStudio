from asyncio.windows_events import NULL
import dependencies.engine.engine as eng
import glm
import math

from dependencies.moderngl.model import ExtendedBaseModel


class GameObject(ExtendedBaseModel):
    def __init__(self, pos = (0, 0, 0), rot = (0, 0, 0), scale = (1, 1, 1)):
        self.position = glm.vec3(pos)
        self.rotation = glm.vec3(rot)
        self.scale = scale
        self.UID = "-1"

        self.forward = glm.vec3(0, 0, 1)
        self.right = glm.vec3(1, 0, 0)
        self.up = glm.vec3(0, 1, 0)

        self.isCollide = False
        self.collideBox = NULL
        self.velocity =  (0, 0, 0)

        self.model = NULL

    def SetModel(self, name):
        if(eng.Engine.Instance == NULL) : return
        
        text_id = eng.Engine.Instance.graphicEngine.mesh.texture.AddTexture(name)
        eng.Engine.Instance.graphicEngine.mesh.vao.vbo.AddVBO(name)
        eng.Engine.Instance.graphicEngine.mesh.vao.AddVAO(name)
        self.model = ExtendedBaseModel(eng.Engine.Instance.graphicEngine, name, text_id, self.position, self.rotation, self.scale)
        eng.Engine.Instance.graphicEngine.scene.AddObject(self.model)
        
    def SetCollider(self, size):
        self.isCollide = True
        self.collideBox = size

    def OnCollide(self, colider):
        pass


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
            self.model.rot = self.rotation
            self.model.m_model = self.model.get_model_matrix()
