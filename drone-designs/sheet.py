from PIL import Image, ImageDraw, ImageFont
import portrait as P
from options import OPTIONS, grid, render, used_colors

PALE = dict(S=(205, 205, 200), s=(150, 152, 150), m=(110, 100, 100), v=(120, 125, 125), W=(230, 230, 230),
            P=(20, 20, 20), I=(150, 155, 160), i=(70, 72, 78), L=(255, 40, 30), T=(150, 155, 162),
            t=(105, 110, 118), A=(38, 40, 44), a=(18, 18, 22), r=(170, 20, 20), B=(230, 180, 40),
            C=(200, 160, 40), H=(230, 200, 120), h=(180, 140, 70), R=(60, 120, 200))
HUMAN = dict(PALE, S=(236, 196, 160), s=(196, 146, 112), m=(170, 90, 80), W=(245, 245, 245), P=(60, 90, 140))
GREEN = dict(PALE, S=(150, 220, 150), s=(70, 150, 80), m=(30, 90, 40), v=(60, 130, 70), W=(200, 255, 200),
             P=(10, 40, 10), I=(60, 170, 70), i=(20, 80, 30), L=(200, 255, 120), T=(70, 170, 80), t=(40, 120, 50),
             A=(10, 40, 16), a=(4, 20, 8))


def drone(c, beam=True, vein=True, suit=True):
    P.base(c)
    if suit:
        P.drone_suit(c)
    P.cranial_plate(c); P.eyepiece(c, beam=beam); P.head_tubes(c)
    if vein:
        P.veins(c)


def p1h(c): drone(c, beam=False, vein=False)
def p1e(c): drone(c, vein=False)
def p2h(c): P.base(c, hair="updo"); P.catsuit(c); P.brow_star(c); P.ear_implant(c)
def p2e(c):
    drone(c)
    c.poly([(0, 52), (6, 46), (18, 46), (22, 52), (10, 58), (0, 58)], "I")   # tactical shoulder armor
    c.line([(2, 52), (18, 50)], "i")
def p3h(c): P.base(c); P.starfleet(c); P.eyepiece(c); c.line([(44, 30), (46, 40)], "T", 2)
def p3e(c): drone(c)
def p4h(c): P.base(c); P.drone_suit(c); P.locutus_collar(c); P.cranial_plate(c); P.eyepiece(c); P.head_tubes(c)
def p4e(c): drone(c, vein=False)
def p5h(c): P.base(c); P.starfleet(c); P.cranial_plate(c); P.eyepiece(c)
def p5e(c): drone(c)

PORTRAITS = [
    (p1h, dict(HUMAN, S=(214, 196, 180), s=(170, 150, 138), L=(60, 180, 255)), p1e, PALE),
    (p2h, dict(HUMAN, A=(170, 175, 190), a=(110, 115, 130), I=(190, 195, 205), i=(90, 95, 105)),
     p2e, dict(PALE, L=(80, 255, 90), S=(185, 205, 190), s=(130, 150, 135))),
    (p3h, dict(HUMAN, A=(190, 30, 30), a=(20, 20, 24), L=(60, 180, 255)),
     p3e, dict(PALE, S=(150, 155, 150), s=(100, 105, 100), v=(70, 75, 80), A=(14, 14, 16), a=(4, 4, 6))),
    (p4h, dict(HUMAN, L=(110, 20, 20)), p4e, PALE),
    (p5h, dict(HUMAN, A=(220, 170, 30), a=(20, 20, 24), L=(60, 240, 240), B=(250, 220, 120)), p5e, GREEN),
]

F = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
title_f, head_f, body_f, small_f = (ImageFont.truetype(FB, 30), ImageFont.truetype(FB, 24),
                                   ImageFont.truetype(F, 17), ImageFont.truetype(F, 15))
GOLD, BG, CARD = (240, 192, 32), (10, 10, 16), (24, 24, 32)

ROW_H, W = 330, 1500


def frame(img, color=GOLD, t=4):
    out = Image.new("RGB", (img.width + 2 * t, img.height + 2 * t), color)
    out.paste(img, (t, t))
    return out


def wrap(d, text, font, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=font) > width:
            lines.append(cur); cur = w
        else:
            cur = trial
    lines.append(cur)
    return lines


sheet = Image.new("RGB", (W, 90 + ROW_H * len(OPTIONS)), BG)
d = ImageDraw.Draw(sheet)
d.text((24, 24), "Borg drone appearance: 5 options (hero + enemy)", font=title_f, fill=GOLD)
singles = []
for i, (o, (ph, hp, pe, ep)) in enumerate(zip(OPTIONS, PORTRAITS)):
    y0 = 90 + i * ROW_H
    d.rectangle((16, y0, W - 16, y0 + ROW_H - 14), fill=CARD)
    imgs = []
    for fn, pal in ((ph, hp), (pe, ep)):
        c = P.Canvas(); fn(c); imgs.append(frame(P.finish(c, pal)))
    sprites = []
    counts = []
    for k in ("hero", "enemy"):
        g = grid(); o[k](g)
        sp = render(g, o[k + "_pal"], 8)
        bgsp = Image.new("RGBA", sp.size, (64, 64, 64, 255)); bgsp.alpha_composite(sp)
        sprites.append(frame(bgsp.convert("RGB"), (90, 90, 100), 3))
        counts.append(len(used_colors(g, o[k + "_pal"])))
    x = 30
    for img in imgs:
        sheet.paste(img, (x, y0 + 14)); x += img.width + 14
    for sp in sprites:
        sheet.paste(sp, (x, y0 + 14 + 30)); x += sp.width + 14
    d.text((30 + 4, y0 + ROW_H - 42), "hero", font=small_f, fill=(200, 200, 210))
    d.text((30 + 278, y0 + ROW_H - 42), "enemy", font=small_f, fill=(200, 200, 210))
    sx = 30 + 2 * 278
    d.text((sx, y0 + 18), "Game sprites (24x24 pixels, shown 8x)", font=small_f, fill=(200, 200, 210))
    d.text((sx, y0 + 250), f"hero: {counts[0]} colors   enemy: {counts[1]} colors", font=small_f, fill=(170, 170, 180))
    d.text((sx, y0 + 270), "Nintendo limit: 3 colors + see-through per layer", font=small_f, fill=(130, 130, 140))
    tx = x + 10
    d.text((tx, y0 + 18), o["name"], font=head_f, fill=GOLD)
    d.text((tx, y0 + 52), o["era"], font=small_f, fill=(140, 170, 230))
    ty = y0 + 86
    for label, note in (("Hero", o["hero_note"]), ("Enemy", o["enemy_note"])):
        d.text((tx, ty), label, font=ImageFont.truetype(FB, 17), fill=(230, 230, 235)); ty += 24
        for line in wrap(d, note, body_f, W - tx - 40):
            d.text((tx, ty), line, font=body_f, fill=(215, 215, 220)); ty += 22
        ty += 10
    card = sheet.crop((16, y0, W - 16, y0 + ROW_H - 14))
    card.save(f"option{i + 1}.png")
sheet.save("drone_options.png")
print(sheet.size)
