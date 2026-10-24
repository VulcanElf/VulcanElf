"""Export the chosen pair: Hugh hero (option 1) + Cube Green enemy (option 5)."""
from PIL import Image
import portrait as P
from options import OPTIONS, grid, render
from sheet import PORTRAITS

for name, opt, which, pidx in (("hero_hugh", 0, "hero", 0), ("enemy_cube_green", 4, "enemy", 4)):
    o = OPTIONS[opt]
    g = grid(); o[which](g)
    render(g, o[which + "_pal"], 1).save(f"{name}_sprite_1x.png")
    render(g, o[which + "_pal"], 8).save(f"{name}_sprite_8x.png")
    fn, pal = PORTRAITS[pidx][0:2] if which == "hero" else PORTRAITS[pidx][2:4]
    c = P.Canvas(); fn(c)
    P.finish(c, pal, scale=1).save(f"{name}_portrait_1x.png")
    P.finish(c, pal, scale=4).save(f"{name}_portrait_4x.png")

imgs = [Image.open(f) for f in ("hero_hugh_portrait_4x.png", "enemy_cube_green_portrait_4x.png")]
sp = [Image.open(f) for f in ("hero_hugh_sprite_8x.png", "enemy_cube_green_sprite_8x.png")]
out = Image.new("RGB", (256 * 2 + 192 * 2 + 60, 276), (24, 24, 32))
x = 10
for im in imgs:
    out.paste(im, (x, 10)); x += 266
for im in sp:
    bg = Image.new("RGBA", im.size, (64, 64, 64, 255)); bg.alpha_composite(im)
    out.paste(bg.convert("RGB"), (x, 42)); x += 202
out.save("chosen_pair.png")
