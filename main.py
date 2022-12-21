import pyglet

from classes import KOS

HEIGHT = 600
WIDTH = 800

window = pyglet.window.Window(WIDTH,HEIGHT,resizable=True)
koordinatenSystem = KOS(window)


@window.event
def on_draw():
    window.clear()
    koordinatenSystem.completeBatch.draw()


pyglet.app.run()
