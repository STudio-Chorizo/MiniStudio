import dependencies.engine.engine as eng
class EndLvl():
    def __init__(self):
        self.AS = 0

    def NewLvl(self, AS):
        #AS c'est la séssion actuel !
        self.AS = AS
        print("grosse merde")
        u = dict(eng.Engine.Instance.gameObjects)
        for n in u:
            eng.Engine.Instance.Destroy(n)

        eng.Engine.Instance.LoadScene(self.AS +1)