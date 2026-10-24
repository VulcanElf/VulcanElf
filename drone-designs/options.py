"""The five hero/enemy drone design options."""
from sprites import *

def opt1_hero(g):   # Hugh: full drone kit, liberated -> blue lights
    bald_plate(g); eyepiece(g); neck_tube(g); drone_body(g); claw_arm(g)
def opt1_enemy(g):  # TNG classic drone
    bald_plate(g); eyepiece(g, beam=True); neck_tube(g); drone_body(g); claw_arm(g); drone_face(g)

def opt2_hero(g):   # Seven of Nine catsuit
    hair(g, "updo"); brow_implant(g); cheek_implant(g); hand_mesh(g)
def opt2_enemy(g):  # Voyager tactical drone
    bald_plate(g); eyepiece(g, beam=True); neck_tube(g); drone_body(g); armor_shoulder(g); drill_arm(g); drone_face(g)

def opt3_hero(g):   # Starfleet officer with leftover implants
    starfleet(g); eyepiece(g); claw_arm(g)
def opt3_enemy(g):  # First Contact drone
    bald_plate(g); eyepiece(g, beam=True); neck_tube(g); drone_body(g); drill_arm(g); drone_face(g)

def opt4_hero(g):   # Locutus, freed: half-assimilated captain
    bald_plate(g); eyepiece(g); neck_tube(g); drone_body(g); put(g, [(7, 14), (8, 14), (7, 15)], "B")
def opt4_enemy(g):
    bald_plate(g); eyepiece(g, beam=True); neck_tube(g); drone_body(g); claw_arm(g); drone_face(g)

def opt5_hero(g):   # Cube Green: gold ops officer, implant glows
    starfleet(g); bald_plate(g); eyepiece(g); hand_mesh(g)
def opt5_enemy(g):
    bald_plate(g); eyepiece(g, beam=True); neck_tube(g); drone_body(g); claw_arm(g); drone_face(g)

# Sprite palettes. Roles: K outline, S skin, W eye white, P pupil, A top, a lower,
# I implant light, i implant dark, T tube, L light, B badge, H hair
DRONE = dict(K="0F", P="0F", a="0F", A="0F", W="20", S="10", I="00", i="00", T="10", L="16")

OPTIONS = [
    dict(name="1. Hugh & the Collective", era="The Next Generation: 'Q Who', 'I, Borg' (1989-92)",
         hero_note="Freed drone in full Borg suit. Lights switched from red to blue.",
         enemy_note="Classic Next Generation drone: chalk skin, black ribbed suit, red eyepiece laser, claw arm.",
         hero=opt1_hero, enemy=opt1_enemy,
         hero_pal=dict(DRONE, L="21", S="36", I="10"),
         enemy_pal=dict(DRONE)),
    dict(name="2. Seven of Nine vs Tactical", era="Star Trek: Voyager (1997-2001)",
         hero_note="Human skin, silver catsuit, star implant over brow, cheek + hand mesh.",
         enemy_note="Voyager tactical drone: shoulder armor plate, drill arm, green glow.",
         hero=opt2_hero, enemy=opt2_enemy,
         hero_pal=dict(K="0F", S="36", W="20", P="11", A="10", a="00", I="00", i="0F", H="38", T="00", L="21", B="28"),
         enemy_pal=dict(DRONE, L="2A", T="00", I="10", S="3A")),
    dict(name="3. Starfleet vs First Contact", era="Next Generation crew + 'First Contact' film (1996)",
         hero_note="Next Generation uniform like your Mega Man crew sprites. Keeps an eyepiece and claw arm.",
         enemy_note="First Contact drone: gray skin, black armor, drill arm, red laser.",
         hero=opt3_hero, enemy=opt3_enemy,
         hero_pal=dict(K="0F", S="36", W="20", P="0F", A="16", a="0F", I="10", i="00", L="21", B="28", T="10"),
         enemy_pal=dict(DRONE, S="00", W="10", I="10", T="10")),
    dict(name="4. Locutus Unbound", era="The Next Generation: 'The Best of Both Worlds' (1990)",
         hero_note="Locutus look, freed: drone suit with a gold com-badge, eyepiece light dark.",
         enemy_note="Standard drones with the red laser beam on.",
         hero=opt4_hero, enemy=opt4_enemy,
         hero_pal=dict(DRONE, S="36", L="06", B="28", I="10"),
         enemy_pal=dict(DRONE)),
    dict(name="5. Cube Green", era="Borg cube interior lighting",
         hero_note="Gold ops uniform, bald with plate, eyepiece glows cyan. Hand mesh.",
         enemy_note="Drones lit only in cube greens. Strongest contrast vs the hero.",
         hero=opt5_hero, enemy=opt5_enemy,
         hero_pal=dict(K="0F", S="36", W="20", P="0F", A="28", a="0F", I="10", i="00", L="3C", B="38", T="10"),
         enemy_pal=dict(K="0F", P="0F", a="0F", A="0F", W="3A", S="2A", I="1A", i="0A", T="1A", L="3A")),
]
