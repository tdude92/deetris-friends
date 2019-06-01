import pyglet

pyglet.resource.path = ["../resources"]
pyglet.resource.reindex()

window = pyglet.window.Window()

if __name__ == "__main__":
    pyglet.app.run()