# -*- coding: utf-8 -*-
import psp2d
import pspmp3
import pspogg
from time import time, localtime, sleep
import os
screen = psp2d.Screen()
font = psp2d.Font("engine/fonts/font.png")
font_out = psp2d.Font("engine/fonts/font_big.png")
font_black = psp2d.Font("engine/fonts/font_black.png")
CLEAR_COLOR = psp2d.Color(0,0,0)
screen.clear(psp2d.Color(0,0,0,255))
#intro blyat
id_current = 0
logo_engine = psp2d.Image("engine/ui/logo.png")
def intro(text, time):
	global logo_engine
	screen.blit(logo_engine)
	font_black.drawText(screen, 4, 252, str(text))
	screen.swap()
	psp2d.Timer(time)
intro("initialization", 0.2)

#main_plot = str(open('game/plot/plot.py', 'r').read())
lastPad = time()
Game_running = True
Do_once = True
Do_once_sound = True
pspmp3.init(1)
choice_var =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
intro("LOADING: UI IMAGES", 0.1)
#load
ui_text_bord = psp2d.Image("engine/ui/window.png")
ui_menu = psp2d.Image("engine/ui/ui_menu.png")
ui_choice = psp2d.Image("engine/ui/choice.png")
ui_pause = psp2d.Image("engine/ui/ui_pause.png")
ui_cross = psp2d.Image("engine/ui/ui_cross.png")

execfile('engine/scripts/images.py')

#variables
background_id = 0
background_screen = psp2d.Image(480, 272)
background_screen = psp2d.Image("game/image/background/background0.png")
character = []
character.append((character_files[0], 0))

intro("LOADING: ENGINE LOGIC", 0.1)
def render_multi_line(text, x, y, fsize):
        lines = text.splitlines()
        for i, l in enumerate(lines):
            #screen.blit(sys_font.render(l, 0, hecolor), (x, y + fsize*i))
			font_out.drawText(screen, x, y+fsize*i, l)

execfile('engine/scripts/animation.py')
execfile('engine/scripts/save_sys.py')
execfile('engine/scripts/vn_func.py')
execfile('engine/scripts/audio.py')
execfile('engine/scripts/menu.py')
execfile('engine/scripts/ui.py')
def game_render():
	global main_plot
	execfile('game/plot/plot.py')

intro("LOADING COMPLETE", 0.3)
while Game_running:
	if id_current ==(0):menu_render()
	game_render()
	Do_once_sound =False
	pad = psp2d.Controller()
	if pad.cross and (not lastPad or time() - lastPad >= 0.45):
		id_current+=1
		Do_once = True
		Do_once_sound = True
		lastPad = time()
	elif pad.start:
		if id_current >=(1):
			pause_ui()
pspogg.end()