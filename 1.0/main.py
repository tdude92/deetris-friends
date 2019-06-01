import pyglet
from pyglet.window import key, mouse # Useless right now but we'll need it later.

# Change pyglet resource path.
pyglet.resource.path = ["../resources"]
pyglet.resource.reindex()

window = pyglet.window.Window()
sprite_sheet = pyglet.resource.image("deetriminos.png")

# Deetriminos:
"""
Each image of a deetrimino is stored in a tuple that 
contains all possible orientations of that deetrimino.
"""
LIGHT_BLUE = (
    sprite_sheet.get_region(x = 0, y = 960, width = 128, height = 32),
    sprite_sheet.get_region(x = 0, y = 800, width = 32, height = 128)
)


@window.event
def on_draw():
    window.clear()
    LIGHT_BLUE[0].blit(0, 0)
    LIGHT_BLUE[1].blit(160, 0)

window.push_handlers(pyglet.window.event.WindowEventLogger()) # This prints every event onto the console.
pyglet.app.run()
