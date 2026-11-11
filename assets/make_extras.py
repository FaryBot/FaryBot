"""Generate two README pictures for the FaryBot profile (original pixel art):

1. terminal.svg  - a terminal window that types out a game-style "character sheet"
2. panda-grid.svg - a contribution-graph-style grid with a pixel panda in it

Usage: python3 make_extras.py <output folder>
"""
import random
import sys
from pathlib import Path

out_dir = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
out_dir.mkdir(parents=True, exist_ok=True)

PANDA = [
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


def esc(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ---------------------------------------------------------------- terminal
def terminal():
    W, H = 900, 400
    o = []
    a = o.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
      f'role="img" aria-label="Terminal showing Faryal\'s character sheet">')
    a("""<style>
.l{opacity:0;animation:show .01s forwards}
@keyframes show{to{opacity:1}}
.bar{transform-origin:0 0;transform:scaleX(0);animation:fill 1.6s steps(12) forwards}
@keyframes fill{to{transform:scaleX(1)}}
.cur{animation:cur 1s steps(1) infinite}
@keyframes cur{0%,49%{opacity:1}50%,100%{opacity:0}}
.blink{animation:blink 4s steps(1) infinite}
@keyframes blink{0%,92%{opacity:1}93%,97%{opacity:0}98%,100%{opacity:1}}
text{font-family:'Courier New',Courier,monospace;font-size:17px;font-weight:700}
</style>""")
    # window
    a(f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="#1e1530" stroke="#c9a7e8" stroke-width="2"/>')
    a(f'<path d="M1 15 a14 14 0 0 1 14 -14 H{W-15} a14 14 0 0 1 14 14 V40 H1 Z" fill="#2d2147"/>')
    for i, c in enumerate(["#f7a8c8", "#ffe08a", "#9fe0b0"]):
        a(f'<circle cx="{26 + i*22}" cy="21" r="7" fill="{c}"/>')
    a('<text x="450" y="26" text-anchor="middle" fill="#bfa6dd" style="font-size:14px">faryal@panda-den: ~</text>')

    # pixel panda (left)
    u, ox, oy = 9, 34, 112
    colors = {"O": "#2b1a3d", "K": "#2b1a3d", "W": "#fdfbff", "P": "#f7a8c8", "N": "#2b1a3d"}
    a('<g class="l" style="animation-delay:.6s">')
    for ry, row in enumerate(PANDA):          # light rim so the panda stands out
        for rx, ch in enumerate(row):
            if ch == ".":
                continue
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = rx + dx, ry + dy
                if ny < 0 or ny >= len(PANDA) or nx < 0 or nx >= len(row) or PANDA[ny][nx] == ".":
                    a(f'<rect x="{ox+nx*u}" y="{oy+ny*u}" width="{u}" height="{u}" fill="#c9a7e8"/>')
    for ry, row in enumerate(PANDA):
        for rx, ch in enumerate(row):
            if ch == ".":
                continue
            fill = "#2b1a3d" if ch == "E" else colors[ch]
            a(f'<rect x="{ox+rx*u}" y="{oy+ry*u}" width="{u}" height="{u}" fill="{fill}"/>')
    for ry, row in enumerate(PANDA):
        for rx, ch in enumerate(row):
            if ch == "E":
                a(f'<rect class="blink" x="{ox+rx*u}" y="{oy+ry*u}" width="{u}" height="{u}" fill="#fdfbff"/>')
    a('</g>')

    lines = [
        (0.0, 72, '<tspan fill="#9fe0b0">faryal@panda-den</tspan><tspan fill="#e9d8ff">:~$ </tspan>'
                  '<tspan fill="#fbe8ff">./whoami --stats</tspan>'),
        (0.8, 118, '<tspan fill="#c9a7e8">NAME   </tspan><tspan fill="#fbe8ff">Faryal Sadiqi</tspan>'),
        (1.1, 146, '<tspan fill="#c9a7e8">CLASS  </tspan><tspan fill="#fbe8ff">Software Engineer · frontend → full-stack</tspan>'),
        (1.4, 174, '<tspan fill="#c9a7e8">LEVEL  </tspan><tspan fill="#fbe8ff">4 · HBO-ICT @ Hanze, Groningen</tspan>'),
        (1.7, 202, '<tspan fill="#c9a7e8">EXP    </tspan>'),
        (2.0, 230, '<tspan fill="#c9a7e8">QUEST  </tspan><tspan fill="#fbe8ff">graduation internship · Feb 2027</tspan>'),
        (2.3, 258, '<tspan fill="#c9a7e8">BUFFS  </tspan><tspan fill="#fbe8ff">planning · structure · pixel art · curiosity</tspan>'),
        (2.6, 286, '<tspan fill="#c9a7e8">DEBUFF </tspan><tspan fill="#fbe8ff">little bit of a perfectionist</tspan>'),
        (3.4, 334, '<tspan fill="#9fe0b0">faryal@panda-den</tspan><tspan fill="#e9d8ff">:~$ </tspan>'
                   '<tspan fill="#fbe8ff">' + esc("while (!(success = tryAgain())) { exp++; }") + '</tspan>'),
        (4.2, 364, '<tspan fill="#f7a8c8">' + esc("> there's always a restart button ✿") + '</tspan>'),
    ]
    for delay, y, content in lines:
        x = 24 if y in (72, 334, 364) else 250
        a(f'<text class="l" x="{x}" y="{y}" style="animation-delay:{delay}s" xml:space="preserve">{content}</text>')

    # EXP bar (pixel blocks), fills up
    bx, by = 250 + 7 * 10.3, 188
    a(f'<g class="l" style="animation-delay:1.7s">')
    a(f'<rect x="{bx}" y="{by}" width="300" height="18" fill="#2d2147" stroke="#c9a7e8" stroke-width="2"/>')
    a(f'<g class="bar" style="animation-delay:1.8s;transform-box:fill-box">')
    for i in range(12):
        a(f'<rect x="{bx + 4 + i*20}" y="{by + 4}" width="16" height="10" fill="#c9a7e8"/>')
    a('</g>')
    a(f'<text x="{bx + 312}" y="{by + 15}" fill="#bfa6dd" style="font-size:14px">80% · keep going</text>')
    a('</g>')
    a(f'<rect class="cur" x="24" y="374" width="11" height="4" fill="#fbe8ff"/>')
    a("</svg>")
    return "\n".join(o)


# ---------------------------------------------------------------- panda grid
def panda_grid():
    random.seed(3)
    cols, rows = 40, 19
    cell, gap = 14, 4
    pad_x, pad_top = 24, 56
    W = pad_x * 2 + cols * (cell + gap) - gap
    H = pad_top + rows * (cell + gap) - gap + 60
    levels = ["#2a2140", "#4a3570", "#7454a8", "#a988d8", "#efe4ff"]
    o = []
    a = o.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
      f'role="img" aria-label="A pixel panda drawn in a contribution-graph style grid">')
    a("""<style>
.c{opacity:0;animation:pop .35s steps(2) forwards}
@keyframes pop{to{opacity:1}}
text{font-family:'Courier New',Courier,monospace;font-weight:700}
</style>""")
    a(f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="#171124" stroke="#4a3570" stroke-width="2"/>')
    a(f'<text x="{pad_x}" y="34" fill="#e9d8ff" style="font-size:17px">'
      f'my contribution graph is still growing, so here\'s a panda for now ✿</text>')

    # where the panda goes in the grid
    pr, pc = 2, (cols - len(PANDA[0])) // 2
    m = {"O": 3, "K": 1, "W": 4, "E": 4, "N": 1}
    for r in range(rows):
        for c in range(cols):
            lvl = 0
            fill = None
            pr_i, pc_i = r - pr, c - pc
            if 0 <= pr_i < len(PANDA) and 0 <= pc_i < len(PANDA[0]) and PANDA[pr_i][pc_i] != ".":
                ch = PANDA[pr_i][pc_i]
                if ch == "P":
                    fill = "#f7a8c8"
                else:
                    lvl = m[ch]
            elif r == rows - 1 or (r >= rows - 2 and random.random() < 0.5):
                lvl = random.choice([1, 2, 3])          # little "grass" row
            elif random.random() < 0.07:
                lvl = 1
            fill = fill or levels[lvl]
            x = pad_x + c * (cell + gap)
            y = pad_top + r * (cell + gap)
            delay = (c + r) * 0.035
            a(f'<rect class="c" style="animation-delay:{delay:.2f}s" x="{x}" y="{y}" '
              f'width="{cell}" height="{cell}" rx="3" fill="{fill}"/>')

    # legend
    ly = H - 26
    a(f'<text x="{W - pad_x - 190}" y="{ly + 12}" fill="#bfa6dd" style="font-size:14px">Less</text>')
    for i, lv in enumerate(levels):
        a(f'<rect x="{W - pad_x - 145 + i*20}" y="{ly}" width="14" height="14" rx="3" fill="{lv}"/>')
    a(f'<text x="{W - pad_x - 40}" y="{ly + 12}" fill="#bfa6dd" style="font-size:14px">More</text>')
    a(f'<text x="{pad_x}" y="{ly + 12}" fill="#8f7ab0" style="font-size:13px">real squares coming soon, one commit at a time</text>')
    a("</svg>")
    return "\n".join(o)


(out_dir / "terminal.svg").write_text(terminal(), encoding="utf-8")
(out_dir / "panda-grid.svg").write_text(panda_grid(), encoding="utf-8")
print("written to", out_dir)
