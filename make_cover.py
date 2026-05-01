#!/usr/bin/env python3
"""Vault Pro cover image — 1280x720"""
from PIL import Image, ImageDraw, ImageFont
import glob

W, H = 1280, 720
BG = (12, 18, 28)
TXT = (255, 255, 255)
ACCENT = (147, 197, 253)  # sky blue
GOLD = (250, 204, 21)
MUTED = (100, 116, 139)

def find_font(paths, size):
    for p in paths:
        for path in glob.glob(p):
            try: return ImageFont.truetype(path, size)
            except: pass
    return ImageFont.load_default()

bold = ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]
reg = ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]
mono = ["/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"]

f_huge = find_font(bold, 72)
f_med = find_font(reg, 44)
f_small = find_font(bold, 22)
f_money = find_font(mono, 64)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# Subtle cross-grid texture
for x in range(0, W, 32):
    for y in range(0, H, 32):
        d.point((x, y), fill=(36, 48, 64))

# Top tag
d.text((48, 48), "VAULT PRO", font=f_small, fill=GOLD)

# Main lockup — split across two lines
title_l1 = "Claude · Hermes · Obsidian"
title_l2 = "as one OS"

bb1 = d.textbbox((0,0), title_l1, font=f_huge)
bb2 = d.textbbox((0,0), title_l2, font=f_huge)
tw1 = bb1[2]-bb1[0]
tw2 = bb2[2]-bb2[0]

# Line 1 stacked
d.text(((W-tw1)/2, 240), title_l1, font=f_huge, fill=TXT)
# Line 2 with accent
d.text(((W-tw2)/2, 360), title_l2, font=f_huge, fill=ACCENT)

# Subtitle
sub = "The operating system for AI-first solo founders"
bbs = d.textbbox((0,0), sub, font=f_med)
tws = bbs[2]-bbs[0]
d.text(((W-tws)/2, 490), sub, font=f_med, fill=MUTED)

# Price badge
badge = "$49"
bb = d.textbbox((0,0), badge, font=f_money)
bw = bb[2]-bb[0]; bh = bb[3]-bb[1]
pad = 18
bx = W - bw - 80; by = H - bh - 80
d.rectangle([bx-pad, by-pad, bx+bw+pad, by+bh+pad+12], outline=GOLD, width=3)
d.text((bx, by), badge, font=f_money, fill=GOLD)

# Bottom-left
d.text((48, H-50), "github.com/bshelby88/claude-obsidian-vault-pro", font=f_small, fill=MUTED)

img.save("/home/sprit/vault-pro-landing/og.png", "PNG", optimize=True)
print("saved og.png")
