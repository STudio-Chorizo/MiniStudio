from asyncio.windows_events import NULL
import dependencies.engine.gameobject as go
import dependencies.engine.engine as eng
class Booster(go.GameObject):
	def __init__(self, pos=..., rot=..., scale=...):
		super().__init__(pos, rot, scale)
		self.boost = 0
		self.Begin = -1
		self.obj = None

	def OnCollide(self, colider):
		if colider.UID != "0":
			return
		self.Begin = eng.Engine.Instance.time
		self.obj = colider
		self.boost = 1
		self.model = NULL
		self.isCollide = False
		self.StartBooster()

	def StartBooster(self):
		self.obj.boost = 3

	def Update(self):
		if (self.Begin != -1 and self.Begin + 5000 < eng.Engine.Instance.time):
			self.obj.boost = 1