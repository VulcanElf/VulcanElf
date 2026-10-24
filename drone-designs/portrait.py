"""64x64 head-and-shoulders portraits in the style of the TNG/DS9 pixel grids."""
from PIL import Image, ImageDraw

N = 64
# role -> group, used for the interior edge pass
GROUP = dict(S="skin", s="skin", m="skin", v="skin", W="eye", P="eye", R="eye",
             I="metal", i="metal", L="light", T="tube", t="tube",
             A="suit", a="suit", r="suit", B="badge", H="hair", h="hair", C="suit")


class Canvas:
    def __init__(self):
        self.im = Image.new("P", (N, N), 0)
        self.roles = ["."]
        self.d = ImageDraw.Draw(self.im)

    def idx(self, role):
        if role not in self.roles:
            self.roles.append(role)
        return self.roles.index(role)

    def ellipse(self, box, role):
        self.d.ellipse(box, fill=self.idx(role))

    def poly(self, pts, role):
        self.d.polygon(pts, fill=self.idx(role))

    def rect(self, box, role):
        self.d.rectangle(box, fill=self.idx(role))

    def line(self, pts, role, w=1):
        self.d.line(pts, fill=self.idx(role), width=w)

    def px(self, pts, role):
        for p in pts:
            self.im.putpixel(p, self.idx(role))

    def get(self, x, y):
        return self.roles[self.im.getpixel((x, y))]


def base(c, hair=None, skin_shade=True):
    # shoulders / body
    c.poly([(0, 63), (2, 54), (10, 49), (22, 46), (42, 46), (54, 49), (62, 54), (63, 63)], "A")
    c.rect((25, 38, 39, 50), "s")  # neck
    c.poly([(25, 46), (32, 52), (39, 46), (39, 50), (25, 50)], "s")
    # ears
    c.ellipse((16, 26, 21, 36), "S")
    c.ellipse((43, 26, 48, 36), "s")
    # head
    c.ellipse((18, 9, 46, 45), "S")
    if skin_shade:
        head = Image.new("1", (N, N), 0)
        ImageDraw.Draw(head).ellipse((18, 9, 46, 45), fill=1)
        lit = Image.new("1", (N, N), 0)
        ImageDraw.Draw(lit).ellipse((15, 7, 43, 45), fill=1)
        for y in range(N):
            for x in range(N):
                if head.getpixel((x, y)) and not lit.getpixel((x, y)):
                    c.px([(x, y)], "s")
    # brows
    c.line([(22, 24), (28, 23)], "s", 1)
    c.line([(36, 23), (42, 24)], "s", 1)
    # eyes
    for ex in (23, 36):
        c.rect((ex, 27, ex + 5, 28), "W")
        c.rect((ex + 2, 27, ex + 3, 28), "P")
        c.line([(ex, 26), (ex + 5, 26)], "s")
    # nose
    c.line([(33, 29), (34, 35)], "s")
    c.line([(30, 36), (34, 36)], "s")
    # mouth
    c.line([(28, 40), (36, 40)], "m")
    c.line([(29, 41), (35, 41)], "S")
    if hair == "updo":
        c.ellipse((18, 5, 46, 21), "H")
        c.ellipse((24, 1, 42, 12), "H")
        c.poly([(18, 24), (18, 14), (24, 12), (22, 22)], "H")
        c.poly([(46, 24), (46, 14), (40, 12), (42, 22)], "H")
        c.line([(24, 7), (30, 17)], "h")
        c.line([(34, 5), (39, 15)], "h")
        c.line([(19, 20), (23, 12)], "h")


def drone_suit(c, ribs=True):
    """Black Borg exoskeleton: ribbed body, chest plate, shoulder tubes."""
    c.poly([(0, 63), (2, 54), (10, 49), (22, 46), (42, 46), (54, 49), (62, 54), (63, 63)], "A")
    c.poly([(22, 46), (42, 46), (40, 52), (24, 52)], "a")  # high collar
    if ribs:
        for y in range(53, 64, 3):
            c.line([(4, y), (60, y)], "a")
    c.poly([(26, 54), (38, 54), (40, 63), (24, 63)], "I")  # chest plate
    c.rect((29, 57, 35, 60), "i")
    c.px([(31, 58), (32, 58), (33, 58)], "L")
    # shoulder tubes
    c.line([(6, 63), (8, 54), (16, 49)], "T", 2)
    c.line([(58, 63), (56, 54), (48, 49)], "T", 2)


def cranial_plate(c):
    c.poly([(18, 25), (18, 16), (23, 10), (30, 8), (34, 9), (33, 14), (28, 18), (24, 22), (22, 26)], "I")
    c.line([(18, 25), (18, 16), (23, 10), (30, 8), (34, 9)], "i")
    c.line([(33, 14), (28, 18), (24, 22), (22, 26)], "i")
    c.px([(22, 15), (27, 12), (21, 20)], "i")  # bolts
    c.px([(23, 15), (28, 12), (22, 20)], "L")


def eyepiece(c, beam=False):
    c.ellipse((20, 22, 31, 33), "i")
    c.ellipse((22, 24, 29, 31), "I")
    c.rect((24, 26, 27, 29), "i")
    c.rect((25, 27, 26, 28), "L")
    c.line([(20, 27), (14, 26)], "i", 2)  # mount to the plate
    if beam:
        c.line([(25, 27), (0, 18)], "L")


def head_tubes(c):
    c.line([(44, 30), (46, 38), (44, 46), (46, 52)], "T", 2)
    c.line([(20, 34), (18, 42), (20, 48)], "t", 2)


def veins(c):
    c.line([(38, 20), (40, 24), (39, 30)], "v")
    c.line([(40, 24), (43, 26)], "v")
    c.line([(30, 34), (28, 38)], "v")
    c.line([(36, 13), (38, 18), (38, 20)], "v")


def brow_star(c):
    """Seven's ocular implant above her left (viewer-right) eye."""
    c.px([(41, 21), (42, 21), (43, 20), (44, 19), (42, 22), (43, 23), (41, 20), (40, 19)], "I")
    c.px([(42, 20), (43, 21)], "i")


def ear_implant(c):
    c.ellipse((14, 28, 20, 34), "I")
    c.ellipse((16, 30, 18, 32), "i")
    c.line([(17, 34), (20, 40)], "i")


def catsuit(c):
    c.poly([(0, 63), (2, 54), (10, 49), (22, 46), (42, 46), (54, 49), (62, 54), (63, 63)], "A")
    c.poly([(23, 42), (41, 42), (40, 50), (24, 50)], "A")  # high collar
    c.line([(24, 50), (32, 63)], "a")
    c.line([(40, 50), (32, 63)], "a")
    c.line([(8, 52), (20, 63)], "a")
    c.line([(56, 52), (44, 63)], "a")


def starfleet(c):
    """TNG season 3+ uniform: black shoulders/collar over a colored body."""
    c.poly([(0, 63), (2, 54), (10, 49), (22, 46), (42, 46), (54, 49), (62, 54), (63, 63)], "A")
    c.poly([(0, 60), (2, 54), (10, 49), (22, 46), (42, 46), (54, 49), (62, 54), (63, 60), (40, 55), (24, 55)], "a")
    c.poly([(23, 44), (41, 44), (40, 50), (24, 50)], "a")
    c.line([(24, 49), (40, 49)], "C")  # collar piping
    c.poly([(12, 57), (16, 55), (18, 59), (14, 61)], "B")  # com-badge


def locutus_collar(c):
    c.poly([(23, 44), (41, 44), (40, 49), (24, 49)], "r")


def finish(c, pal, outline=(12, 12, 20), halo=(40, 96, 220), bg=(0, 0, 0), scale=4):
    """Color the role map, darken region edges, add the dark outline and blue halo."""
    out = Image.new("RGB", (N, N), bg)
    role = [[c.get(x, y) for x in range(N)] for y in range(N)]
    for y in range(N):
        for x in range(N):
            r = role[y][x]
            if r == ".":
                continue
            col = pal[r]
            # interior edges: darken a pixel whose lower/right neighbour belongs to another group
            for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    n = role[ny][nx]
                    if n != "." and GROUP.get(n) != GROUP.get(r) and GROUP.get(r) not in ("eye", "light") \
                            and GROUP.get(n) not in ("eye",) and (dx, dy) in ((1, 0), (0, 1)):
                        col = tuple(int(v * 0.55) for v in col)
                        break
            out.putpixel((x, y), col)
    # silhouette outline + halo
    def filled(x, y):
        return 0 <= x < N and 0 <= y < N and role[y][x] != "."
    final = out.copy()
    for y in range(N):
        for x in range(N):
            if role[y][x] != "." and pal[role[y][x]] is not None:
                if any(not filled(x + dx, y + dy) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))) and y < N - 1:
                    final.putpixel((x, y), outline)
    for y in range(N):
        for x in range(N):
            if role[y][x] == "." and any(filled(x + dx, y + dy) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
                final.putpixel((x, y), halo)
    # keep the laser beam bright over the halo/background
    for y in range(N):
        for x in range(N):
            if role[y][x] == "L":
                final.putpixel((x, y), pal["L"])
    return final.resize((N * scale, N * scale), Image.NEAREST)
