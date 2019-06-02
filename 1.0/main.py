import pyglet
from pyglet.window import key, mouse # Useless right now but we'll need it later.

# Change pyglet resource path.
pyglet.resource.path = ["../resources"]
pyglet.resource.reindex()

window = pyglet.window.Window()
sprite_sheet = pyglet.resource.image("deetriminos.png")

# Deetriminos:
"""
Each image of a deetrimino is stored in a list that 
contains all possible orientations of that deetrimino.
"""
deetrimino_I = [
    sprite_sheet.get_region(x = 0, y = 960, width = 128, height = 32),
    sprite_sheet.get_region(x = 0, y = 800, width = 32, height = 128)
]

deetrimino_J = [
    sprite_sheet.get_region(x = 160, y = 928, width = 96, height = 64),
    sprite_sheet.get_region(x = 160, y = 800, width = 64, height = 96),
    sprite_sheet.get_region(x = 160, y = 704, width = 96, height = 64),
    sprite_sheet.get_region(x = 160, y = 592, width = 64, height = 96)
]

deetrimino_L = [
    sprite_sheet.get_region(x = 288, y = 928, width = 96, height = 64),
    sprite_sheet.get_region(x = 288, y = 800, width = 64, height = 96),
    sprite_sheet.get_region(x = 288, y = 704, width = 96, height = 64),
    sprite_sheet.get_region(x = 288, y = 592, width = 64, height = 96)
]

deetrimino_O = [
    sprite_sheet.get_region(x = 0, y = 496, width = 64, height = 64)
]

deetrimino_S = [
    sprite_sheet.get_region(x = 96, y = 496, width = 96, height = 64),
    sprite_sheet.get_region(x = 96, y = 368, width = 64, height = 96),
]

deetrimino_Z = [
    sprite_sheet.get_region(x = 224, y = 496, width = 96, height = 64),
    sprite_sheet.get_region(x = 224, y = 368, width = 64, height = 96),
]

deetrimino_T = [
    sprite_sheet.get_region(x = 0, y = 272, width = 96, height = 64),
    sprite_sheet.get_region(x = 0, y = 144, width = 64, height = 96),
    sprite_sheet.get_region(x = 128, y = 272, width = 96, height = 64),
    sprite_sheet.get_region(x = 128, y = 144, width = 64, height = 96)
]


@window.event
def on_draw():
    window.clear()

window.push_handlers(pyglet.window.event.WindowEventLogger()) # This prints every event onto the console.
pyglet.app.run()
