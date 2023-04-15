from asyncio.windows_events import NULL
import dependencies.engine.engine as Eng
import glm
import math

from dependencies.moderngl.model import ExtendedBaseModel


class GameObject(ExtendedBaseModel):
    def __init__(self, pos = (0, 0, 0), rot = (0, 0, 0), scale = (1, 1, 1)):
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
        self.velocity =  (0, 0, 0)

        self.model = NULL

    def SetModel(self, name):
        if(Eng.Engine.Instance == NULL) : return
        
        text_id = Eng.Engine.Instance.graphicEngine.mesh.texture.AddTexture(name)
        Eng.Engine.Instance.graphicEngine.mesh.vao.vbo.AddVBO(name)
        Eng.Engine.Instance.graphicEngine.mesh.vao.AddVAO(name)
        self.model = ExtendedBaseModel(Eng.Engine.Instance.graphicEngine, name, text_id, self.position, self.rotation, self.scale)
        Eng.Engine.Instance.graphicEngine.scene.AddObject(self.model)
        
    def SetCollider(self, size):
        self.isCollide = True
        self.collideBox = size

    def OnCollide(self, colider):
        pass


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
    def SetPos(self, position: tuple, camPosition: tuple = glm.vec3([0, 0.15, 0.2])) -> None:
        """Fonction pour définir un position de l'objet\n
        translation: (x, y, z) position de l'objet"""
        self.prev_position = position
        self.camera_pos = camPosition
    
    # Utiliser cette fonction pour avoir la rotation
    def SetRot(self, orientation: tuple, camOrientation: tuple = (-10, 90, 0)) -> None:
        """Fonction pour définir une rotation de l'objet\n
        orientation: (x, y, z) orientation de l'objet"""
        self.rotation = orientation
        self.camera_pitch = camOrientation[0]
        self.camera_yaw = camOrientation[1]
        self.camera_roll = camOrientation[2]
    
    def SyncPosCamera(self, position: tuple = glm.vec3([0, 0.2, -0.5])) -> None:
        self.camera_pos = glm.vec3(self.position) + position
    
    def SyncRotCamera(self, camOrientation: tuple = (-10, 90, 0)) -> None:
        self.camera_pitch = self.rotation[1]*10 + camOrientation[0]
        self.camera_yaw = self.rotation[0]*10 + camOrientation[1]
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
        
        if(self.model != NULL) : self.model.m_model = self.model.get_model_matrix()
