def exec_line(id, text):
	global id_current
	if id_current ==(id):
		exec(text)
		id_current+=1
def anim_next_day(id):
	global id_current
	if id_current==(id):
		ui_tv = psp2d.Image("game/scripts/images/ui_next_day.png")
		ui_num = psp2d.Image("game/scripts/images/ui_next_day_num.png")
		run = True
		temp_var = 0
		x_pos = 0
		x_pos_fin = -56
		play_anim=True
		while run:
			if play_anim==(True):
				if x_pos_fin>=(x_pos):
					play_anim=False
					run=False
				else:
					x_pos-=1
					sleep(0.035)
				screen.clear(psp2d.Color(0,0,0,255))
				screen.blit(ui_num, dx=x_pos, blend=True)
				screen.blit(ui_tv, blend=True)
				screen.swap()
		screen.clear(psp2d.Color(0,0,0,255))
		screen.blit(ui_num, dx=x_pos_fin, blend=True)
		screen.blit(ui_tv, blend=True)
		screen.swap()
		sleep(4)
		anim_fade()
		id_current+=1
def game_map(id, text1, id1, text2, id2, text3, id3):
	global id_current, lastPad
	if id_current==(id):
		run = True
		ui_map = psp2d.Image("game/scripts/images/map_bg.png")
		map_text = [text1, text2, text3]
		map_button = 0
		while run:
			if map_button==(-1):map_button = 0
			elif map_button==(3):map_button = 2
			screen.clear(psp2d.Color(0,0,0,255))
			screen.blit(ui_map)
			if map_button ==(0):
				font.drawText(screen, 22, 62, ">"+map_text[0])
				font.drawText(screen, 22, 82, ""+map_text[1])
				font.drawText(screen, 22, 102, ""+map_text[2])
			elif map_button ==(1):
				font.drawText(screen, 22, 62, ""+map_text[0])
				font.drawText(screen, 22, 82, ">"+map_text[1])
				font.drawText(screen, 22, 102, ""+map_text[2])
			elif map_button ==(2):
				font.drawText(screen, 22, 62, ""+map_text[0])
				font.drawText(screen, 22, 82, ""+map_text[1])
				font.drawText(screen, 22, 102, ">"+map_text[2])
			screen.swap()
			pad = psp2d.Controller()
			if pad.cross and (not lastPad or time() - lastPad >= 0.5):
				if map_button==(0):
					if id1==(0):pass
					else:
						run=False
						id_current=id1
				elif map_button==(1):
					if id2==(0):pass
					else:
						run=False
						id_current=id2
				elif map_button==(2):
					if id3==(0):pass
					else:
						run=False
						id_current=id3
				lastPad = time()
			elif pad.down and (not lastPad or time() - lastPad >= 0.5):map_button+=1;lastPad = time()
			elif pad.up and (not lastPad or time() - lastPad >= 0.5):map_button-=1;lastPad = time()
def loading_screen(id, tone, time):
	global id_current
	if id_current==(id):
		game_loading = psp2d.Image("game/scripts/images/loading.png")
		game_loading_happy = psp2d.Image("game/scripts/images/loading_a.png")
		game_loading_sad = psp2d.Image("game/scripts/images/loading_b.png")
		if tone==(0):
			screen.blit(game_loading)
		if tone==(1):
			screen.blit(game_loading_happy)
		if tone==(2):
			screen.blit(game_loading_sad)
		screen.swap()
		sleep(time)
		id_current+=1
