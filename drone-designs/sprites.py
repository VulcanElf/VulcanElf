"""Mega Man style 24x24 NES sprites for the hero drone and enemy drones."""
from PIL import Image

BASE = """\
........KKKKKKK.........
......KKSSSSSSSKK.......
.....KSSSSSSSSSSSK......
....KSSSSSSSSSSSSSK.....
....KSSSSSSSSSSSSSK.....
...KSSSWWPSSSWWPSSSK....
...KSSSWWPSSSWWPSSSK....
...KSSSWWPSSSWWPSSSK....
...KSSSSSSSSSSSSSSSK....
....KSSSSSKKKSSSSSK.....
.....KSSSSSSSSSSSK......
......KKSSSSSSSKK.......
....KKAAAKKKKKAAAKK.....
..KKAAAAAAAAAAAAAAAKK...
.KSKAAAAAAAAAAAAAAAKSK..
.KSSKAAAAAAAAAAAAAKSSK..
.KSSKAAAAAAAAAAAAAKSSK..
..KKKaaaaaaaaaaaaaKKK...
....KaaaaaaKaaaaaaK.....
...KaaaaaaK.KaaaaaaK....
..KaaaaaaK...KaaaaaaK...
.KaaaaaaaK...KaaaaaaaK..
.KKKKKKKKK...KKKKKKKKK..
........................"""

# NES 2C02 colors (FCEUX palette), keyed by hex index
NES = {
    "0F": (0, 0, 0), "00": (124, 124, 124), "10": (188, 188, 188), "20": (248, 248, 248),
    "06": (168, 16, 0), "16": (248, 56, 0), "26": (248, 120, 88), "36": (240, 208, 176),
    "27": (252, 160, 68), "17": (228, 92, 16), "07": (136, 20, 0),
    "28": (248, 184, 0), "38": (248, 216, 120), "18": (172, 124, 0),
    "11": (0, 120, 248), "21": (60, 188, 252), "31": (164, 228, 252), "01": (0, 0, 252),
    "1A": (0, 168, 0), "2A": (88, 216, 84), "3A": (184, 248, 184), "0A": (0, 104, 0),
    "2C": (0, 232, 216), "1C": (0, 136, 136), "3C": (0, 252, 252),
    "15": (228, 0, 88), "05": (168, 0, 32),
}


def grid():
    return [list(r) for r in BASE.split("\n")]


def put(g, pts, role):
    for x, y in pts:
        if 0 <= y < len(g) and 0 <= x < len(g[0]):
            g[y][x] = role


def bald_plate(g):
    """Cranial implant plate on the viewer-left of the skull."""
    put(g, [(8, 1), (9, 1), (10, 1)], "i")
    put(g, [(6, 2), (7, 2), (8, 2), (9, 2), (10, 2)], "I")
    put(g, [(5, 3), (6, 3), (7, 3), (8, 3), (9, 3)], "I")
    put(g, [(5, 4), (6, 4)], "I")
    put(g, [(7, 3)], "i")  # bolt
    put(g, [(11, 1), (11, 2), (10, 3)], "K")  # plate edge seam


def eyepiece(g, light="L", beam=False):
    """Ocular implant over the viewer-left eye."""
    put(g, [(x, 4) for x in range(7, 10)], "K")
    put(g, [(x, 8) for x in range(7, 10)], "K")
    for y in (5, 6, 7):
        put(g, [(6, y), (10, y)], "K")
        put(g, [(7, y), (8, y), (9, y)], "I")
    put(g, [(8, 6)], light)
    if beam:
        put(g, [(3, 6), (2, 6), (1, 6), (0, 6)], light)


def brow_implant(g):
    """Seven-of-Nine style star implant above the viewer-right eye."""
    put(g, [(15, 3), (14, 4), (16, 4), (15, 4)], "I")
    put(g, [(17, 4)], "i")


def cheek_implant(g):
    put(g, [(4, 7), (4, 8), (5, 8)], "I")


def neck_tube(g):
    put(g, [(16, 8), (16, 9), (15, 10), (15, 11)], "T")
    put(g, [(14, 12)], "T")


def drone_body(g):
    """Black ribbed bodysuit with gray tubing."""
    for y in (14, 16):
        for x in range(5, 18):
            if g[y][x] == "A":
                g[y][x] = "i"
    put(g, [(8, y) for y in range(13, 18)], "T")
    put(g, [(14, y) for y in range(13, 18)], "T")
    put(g, [(11, 15), (12, 15), (11, 14), (12, 14)], "L")  # chest node light


def claw_arm(g):
    """Viewer-right hand replaced with an assimilation claw."""
    for x, y in [(20, 14), (20, 15), (20, 16), (21, 15), (21, 16)]:
        g[y][x] = "I"
    put(g, [(22, 13), (22, 14), (23, 13)], "i")
    put(g, [(22, 16), (22, 17), (23, 17)], "i")
    put(g, [(21, 13), (21, 14), (21, 17), (19, 17)], "K")
    put(g, [(22, 15)], "K")


def drill_arm(g):
    for x, y in [(20, 14), (20, 15), (20, 16), (21, 15), (21, 16)]:
        g[y][x] = "I"
    put(g, [(22, 15), (22, 16), (23, 15)], "i")
    put(g, [(21, 14), (21, 17)], "K")


def hand_mesh(g):
    put(g, [(2, 15), (3, 16)], "I")


def armor_shoulder(g):
    """Heavy tactical shoulder plate (Voyager era)."""
    put(g, [(2, 12), (3, 12), (4, 12), (5, 12)], "K")
    put(g, [(1, 13), (2, 13), (3, 13), (4, 13), (5, 13), (6, 13)], "I")
    put(g, [(1, 14), (3, 14), (5, 14)], "i")
    put(g, [(0, 13), (0, 14), (1, 12)], "K")


def starfleet(g, badge=True):
    """TNG uniform: colored body, black shoulders/collar, gold com-badge."""
    put(g, [(x, 12) for x in range(4, 19)], "K")
    for x in range(4, 19):
        if g[13][x] == "A":
            g[13][x] = "a"
    if badge:
        put(g, [(7, 14), (8, 14), (7, 15)], "B")


def hair(g, style):
    if style == "updo":  # Seven's swept-up blonde hair
        put(g, [(x, 0) for x in range(8, 15)], "H")
        put(g, [(x, 1) for x in range(7, 17)], "H")
        put(g, [(x, 2) for x in range(6, 17)], "H")
        put(g, [(5, 3), (6, 3), (17, 3), (17, 4), (5, 4)], "H")
        put(g, [(x, 0) for x in (6, 7, 15, 16)], "K")
    if style == "fringe":  # Hugh's short regrowth
        put(g, [(x, 1) for x in range(11, 16)], "H")
        put(g, [(x, 2) for x in range(11, 17)], "H")


def drone_face(g):
    """Gaunt drone face: flat mouth line, sunken eyes."""
    put(g, [(13, 9), (14, 9)], "K")


def render(g, pal, scale=8, bg=None):
    h, w = len(g), len(g[0])
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    for y in range(h):
        for x in range(w):
            c = g[y][x]
            if c == ".":
                continue
            im.putpixel((x, y), NES[pal[c]] + (255,))
    im = im.resize((w * scale, h * scale), Image.NEAREST)
    return im


def used_colors(g, pal):
    return sorted({pal[c] for row in g for c in row if c != "."})
