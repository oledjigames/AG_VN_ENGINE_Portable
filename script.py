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
font_extra = psp2d.Font("engine/fonts/ex_font.png")
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

debug=False

main_plot = 'game/plot/plot.py'
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
ui_loading = psp2d.Image("engine/ui/ui_loading.png")

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
def debug_show():
	global debug, id_current, main_plot
	if debug==(True):
		font_out.drawText(screen, 5, 5, "id_current = "+str(id_current))
		font_out.drawText(screen, 5, 15, "main_plot = "+str(main_plot))
execfile('engine/scripts/animation.py')
execfile('engine/scripts/save_sys.py')
execfile('engine/scripts/vn_func.py')
execfile('engine/scripts/audio.py')
execfile('engine/scripts/menu.py')
execfile('engine/scripts/ui.py')
execfile('game/scripts/init_scripts.py')
def game_render():
	global main_plot
	execfile(main_plot)
intro("LOADING COMPLETE", 0.3)
game_op_run = True
def game_op():
	global game_op_run
	game_op_run = True
	while game_op_run:
		global id_current, lastPad, Do_once, Do_once_sound,ui_loading
		pad = psp2d.Controller()
		if pad.cross and (not lastPad or time() - lastPad >= 0.45):
			id_current+=1
			Do_once = True
			Do_once_sound = True
			lastPad = time()
			game_op_run=False
		elif pad.triangle:
			pass
		elif pad.start:
			if id_current >=(1):
				pause_ui()
				game_op_run=False
				screen.blit(ui_loading)
				screen.swap()
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
	elif pad.triangle:
		pass
	elif pad.start:
		if id_current >=(1):
			pause_ui()
pspogg.end()