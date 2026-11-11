"""Generate an original animated pixel-art banner (SVG) for the FaryBot GitHub profile.

Scene: purple night sky, twinkling stars, pixel moon, city skyline,
and a pixel panda coding on a laptop. Everything is drawn from squares,
so it stays crisp ("pixelated") at any size.
"""
import random

U = 8                    # size of one "pixel" in SVG units
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("--width", type=int, default=1200)
ap.add_argument("--height", type=int, default=320)
ap.add_argument("--text-x", type=float, default=6)      # grid column where the text starts
ap.add_argument("--panda-x", type=int, default=118)     # grid column of the panda
ap.add_argument("--title", default="HI! I'M FARYAL")
ap.add_argument("--subtitle", default="software engineering · art · pandas")
ap.add_argument("--contact", default="faryalsadiqihi5@gmail.com  ·  github.com/FaryBot")
args = ap.parse_args()
W, H = args.width, args.height
TX, PXO = args.text_x, args.panda_x
random.seed(7)           # same stars every time

out = []
add = out.append

# ---------- colours (pastel purple palette) ----------
SKY_TOP, SKY_MID, SKY_LOW = "#241640", "#4b2f7a", "#9b74cf"
BUILD_1, BUILD_2 = "#33224f", "#2a1b42"
WIN_ON, WIN_OFF = "#ffd6f5", "#3f2b60"
MOON, MOON_SHADE = "#fbe8ff", "#e6c8f5"
OUTLINE, PATCH = "#2b1a3d", "#2b1a3d"
FUR, CHEEK = "#fdfbff", "#f7a8c8"
DESK, DESK_EDGE = "#7a56b3", "#5d3f91"
LID, LID_EDGE = "#d9c2f2", "#b392e0"
TEXT, TEXT_SHADOW, SUB = "#fbe8ff", "#2b1a3d", "#f3e6ff"


def px(x, y, color, w=1, h=1, extra=""):
    """One block of w*h pixels at grid position (x, y)."""
    add(f'<rect x="{x*U}" y="{y*U}" width="{w*U}" height="{h*U}" fill="{color}"{extra}/>')


add(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
    f'shape-rendering="crispEdges" role="img" aria-label="Pixel panda coding at night - Faryal Sadiqi, software engineering, art, pandas">')
add("""<style>
.tw{animation:tw 3s steps(2) infinite}
.d1{animation-delay:.4s}.d2{animation-delay:1.1s}.d3{animation-delay:1.9s}.d4{animation-delay:2.5s}
@keyframes tw{0%,100%{opacity:1}50%{opacity:.25}}
.blink{animation:blink 4s steps(1) infinite}
@keyframes blink{0%,92%{opacity:1}93%,97%{opacity:0}98%,100%{opacity:1}}
.glow{animation:glow 2.4s ease-in-out infinite alternate}
@keyframes glow{from{opacity:.55}to{opacity:.95}}
.cursor{animation:cur 1s steps(1) infinite}
@keyframes cur{0%,49%{opacity:1}50%,100%{opacity:0}}
.bob{animation:bob 2s steps(2) infinite}
@keyframes bob{0%,100%{transform:translateY(0)}50%{transform:translateY(-4px)}}
</style>""")

# ---------- sky (stepped bands = pixel gradient) ----------
bands = [SKY_TOP, "#2c1b4e", "#34205c", "#3d256a", SKY_MID, "#5a3a8c", "#6c489f",
         "#7f58b3", "#8f66c2", SKY_LOW]
band_h = H // len(bands)
for i, c in enumerate(bands):
    add(f'<rect x="0" y="{i*band_h}" width="{W}" height="{band_h + 1}" fill="{c}"/>')

mx, my, r = int(TX) + 94, 7, 5
# ---------- stars ----------
cls = ["", " d1", " d2", " d3", " d4"]
for _ in range(46):
    x = random.randrange(0, W // U)
    y = random.randrange(0, 18)
    if mx - 8 < x < mx + 8 and y < 14:     # keep the moon area clear
        continue
    if TX - 3 < x < TX + 90 and 5 < y < 26:    # keep the text area clear
        continue
    big = random.random() < 0.25
    color = random.choice(["#ffffff", "#ffe3fa", "#e9d8ff"])
    k = random.choice(cls)
    if big:   # little plus-shaped star
        add(f'<g class="tw{k}" fill="{color}">'
            f'<rect x="{x*U}" y="{(y-1)*U}" width="{U}" height="{3*U}"/>'
            f'<rect x="{(x-1)*U}" y="{y*U}" width="{3*U}" height="{U}"/></g>')
    else:
        add(f'<rect class="tw{k}" x="{x*U}" y="{y*U}" width="{U}" height="{U}" fill="{color}"/>')

# ---------- moon (pixel circle) ----------
mx, my, r = int(TX) + 94, 7, 5
for gy in range(my - r, my + r + 1):
    for gx in range(mx - r, mx + r + 1):
        d = (gx - mx) ** 2 + (gy - my) ** 2
        if d <= r * r:
            shade = MOON_SHADE if (gx - mx) + (gy - my) > 3 else MOON
            px(gx, gy, shade)
for (cx, cy) in [(mx - 2, my - 2), (mx + 2, my + 2), (mx - 1, my + 2)]:     # craters
    px(cx, cy, MOON_SHADE)

# ---------- skyline ----------
gy_base = H // U   # 40 rows
x = 0
heights = [14, 19, 11, 22, 16, 25, 13, 18, 21, 12, 17, 24, 15, 20, 11, 18, 23, 14, 19, 16]
i = 0
while x < W // U:
    bw = [6, 8, 5, 9, 7][i % 5]
    bh = heights[i % len(heights)]
    if TX - 2 < x < TX + 92:
        bh = min(bh, 12)
    color = BUILD_1 if i % 2 else BUILD_2
    px(x, gy_base - bh, color, bw, bh)
    for wy in range(gy_base - bh + 2, gy_base - 2, 3):
        for wx in range(x + 1, x + bw - 1, 2):
            on = random.random() < 0.35
            px(wx, wy, WIN_ON if on else WIN_OFF)
    x += bw
    i += 1

# ---------- desk ----------
px(0, H // U - 3, DESK_EDGE, W // U, 1)
px(0, H // U - 2, DESK, W // U, 2)

# ---------- panda (each letter = one pixel) ----------
# O outline, K dark patch, W fur, E eye shine (blinks), P cheek, N nose
panda = [
    "..KKK..........KKK..",
    ".KKKKK........KKKKK.",
    ".KKKKOOOOOOOOOOKKKK.",
    "..KKOWWWWWWWWWWOKK..",
    "...OWWWWWWWWWWWWO...",
    "..OWWKKKWWWWKKKWWO..",
    "..OWKKEKWWWWKEKKWO..",
    "..OWKKKKWWWWKKKKWO..",
    "..OWPPWWWNNWWWPPWO..",
    "..OWWWWWWWWWWWWWWO..",
    "...OWWWWWWWWWWWWO...",
    "....OOOOOOOOOOOO....",
    "...KKKWWWWWWWWKKK...",
    "..KKKKWWWWWWWWKKKK..",
    ".KKKKKWWWWWWWWKKKKK.",
]
assert len({len(r) for r in panda}) == 1, "panda rows must be equal length"
colors = {"O": OUTLINE, "K": PATCH, "W": FUR, "P": CHEEK, "N": OUTLINE, "E": FUR}
PX, PY = PXO, (H // U) - 22          # where the panda sits (grid)
add('<g class="bob">')
# light rim around the panda so it stands out against dark buildings
for ry, row in enumerate(panda):
    for rx, ch in enumerate(row):
        if ch == ".":
            continue
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = rx + dx, ry + dy
            if ny < 0 or ny >= len(panda) or nx < 0 or nx >= len(row) or panda[ny][nx] == ".":
                px(PX + nx, PY + ny, "#e9d8ff")
eyes = []
for ry, row in enumerate(panda):
    for rx, ch in enumerate(row):
        if ch == ".":
            continue
        if ch == "E":
            eyes.append((PX + rx, PY + ry))
            continue
        px(PX + rx, PY + ry, colors[ch])
# eye shine blinks: underneath it the patch colour shows
for (ex, ey) in eyes:
    px(ex, ey, PATCH)
add('<g class="blink">')
for (ex, ey) in eyes:
    px(ex, ey, FUR)
add('</g></g>')

# ---------- laptop (we see the back of the lid) ----------
LX, LY = PXO - 2, (H // U) - 10
px(LX, LY, LID_EDGE, 24, 1)
px(LX, LY + 1, LID, 24, 6)
px(LX, LY + 7, LID_EDGE, 24, 1)
heart = [".PP.PP.", "PPPPPPP", ".PPPPP.", "..PPP..", "...P..."]
for hy, row in enumerate(heart):
    for hx, ch in enumerate(row):
        if ch == "P":
            px(LX + 9 + hx, LY + 2 + hy, CHEEK)
# screen glow on the panda's face
add(f'<rect class="glow" x="{(PX+3)*U}" y="{(PY+3)*U}" width="{14*U}" height="{9*U}" '
    f'fill="#bfa3ff" opacity=".6" style="mix-blend-mode:soft-light"/>')

# ---------- mug + plant (little props) ----------
MUGX, BASE = PXO - 10, (H // U) - 7
px(MUGX, BASE, "#f7a8c8", 3, 4); px(MUGX + 3, BASE + 1, "#f7a8c8", 1, 2)       # mug
add('<g class="tw d2" fill="#ffffff" opacity=".7">')
px(MUGX + 1, BASE - 2, "#ffffff"); px(MUGX + 2, BASE - 3, "#ffffff")                   # steam
add('</g>')
px(PXO + 24, BASE, "#8a5a44", 3, 4)                                     # pot
for (dx, dy) in [(0, -2), (2, -2), (1, -3), (-1, -3), (3, -3), (1, -1)]:
    px(PXO + 24 + dx, BASE + dy, "#9fe0b0")

# ---------- bitmap title text ----------
FONT = {
    "H": ["10001", "10001", "10001", "11111", "10001", "10001", "10001"],
    "I": ["11111", "00100", "00100", "00100", "00100", "00100", "11111"],
    "M": ["10001", "11011", "10101", "10101", "10001", "10001", "10001"],
    "F": ["11111", "10000", "10000", "11110", "10000", "10000", "10000"],
    "A": ["01110", "10001", "10001", "11111", "10001", "10001", "10001"],
    "R": ["11110", "10001", "10001", "11110", "10100", "10010", "10001"],
    "Y": ["10001", "10001", "01010", "00100", "00100", "00100", "00100"],
    "L": ["10000", "10000", "10000", "10000", "10000", "10000", "11111"],
    ",": ["00000", "00000", "00000", "00000", "00110", "00100", "01000"],
    "'": ["00100", "00100", "01000", "00000", "00000", "00000", "00000"],
    "!": ["00100", "00100", "00100", "00100", "00100", "00000", "00100"],
    " ": ["000", "000", "000", "000", "000", "000", "000"],
}


def bitmap_text(text, gx, gy, color, scale=1):
    """Draw text with the tiny 5x7 pixel font; returns the grid x where it ends."""
    cx = gx
    for ch in text:
        glyph = FONT[ch]
        for ry, row in enumerate(glyph):
            for rx, bit in enumerate(row):
                if bit == "1":
                    add(f'<rect x="{(cx*U + rx*U*scale/1)}" y="{gy*U + ry*U*scale}" '
                        f'width="{U*scale}" height="{U*scale}" fill="{color}"/>')
        cx += (len(glyph[0]) + 1) * scale
    return cx


title = args.title
bitmap_text(title, TX + 1, 9, TEXT_SHADOW)       # shadow, one pixel down-right
end = bitmap_text(title, TX, 8, TEXT)
add(f'<rect class="cursor" x="{(end+1)*U}" y="{8*U}" width="{3*U}" height="{7*U}" fill="#f7a8c8"/>')

# subtitle + blinking cursor
FONTFAM = "'Courier New', Courier, monospace"
add(f'<text x="{TX*U}" y="{19.5*U}" font-family="{FONTFAM}" font-size="26" font-weight="700" '
    f'letter-spacing="1" fill="{SUB}">{args.subtitle}</text>')
add(f'<text x="{TX*U}" y="{23.5*U}" font-family="{FONTFAM}" font-size="17" font-weight="700" '
    f'fill="#e3cff7">{args.contact}</text>')

add("</svg>")
print("\n".join(out))
