import pyglet

class KOS():
    def __init__(self,window) -> None:
        self.window = window
        self.completeBatch = pyglet.graphics.Batch()

        self.axisColor = (211,211,211)

        self.checkWindowLength()


    def checkWindowLength(self):
        self.width = self.window.width
        self.height = self.window.height
    def checkFor00(self):
        self.checkWindowLength()
        self.xo = self.width / 2
        self.y0 = self.height / 2
    
    def drawAxis(self):
        self.plusyAxis = pyglet.shapes.Line(self.x0, self.y0 , self.x0, 0, width=1,color=self.axisColor, batch=self.completeBatch)