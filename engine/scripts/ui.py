def pause_ui():
	global ui_pause, lastPad, id_current
	x_pos =-168
	x_fin = 0
	x_now = -168
	animation = True
	work = True
	pause_text = ["Continue","Quick Save","Quick Load","Menu"]
	pause_button = 0 #0 cont 1qs 2ql 3m
	while work:
		if animation==(False):
			if pause_button==(-1):pause_button = 3
			elif pause_button==(4):pause_button = 0
			screen.blit(ui_pause, blend=True)
			if pause_button ==(0):
				font.drawText(screen, 7, 115, ">"+pause_text[0])
				font.drawText(screen, 7, 128, ""+pause_text[1])
				font.drawText(screen, 7, 140, ""+pause_text[2])
				font.drawText(screen, 7, 152, ""+pause_text[3])
			elif pause_button ==(1):
				font.drawText(screen, 7, 115, ""+pause_text[0])
				font.drawText(screen, 7, 128, ">"+pause_text[1])
				font.drawText(screen, 7, 140, ""+pause_text[2])
				font.drawText(screen, 7, 152, ""+pause_text[3])
			elif pause_button ==(2):
				font.drawText(screen, 7, 115, ""+pause_text[0])
				font.drawText(screen, 7, 128, ""+pause_text[1])
				font.drawText(screen, 7, 140, ">"+pause_text[2])
				font.drawText(screen, 7, 152, ""+pause_text[3])
			elif pause_button ==(3):
				font.drawText(screen, 7, 115, ""+pause_text[0])
				font.drawText(screen, 7, 128, ""+pause_text[1])
				font.drawText(screen, 7, 140, ""+pause_text[2])
				font.drawText(screen, 7, 152, ">"+pause_text[3])
			pad = psp2d.Controller()
			if pad.cross and (not lastPad or time() - lastPad >= 0.5):
				if pause_button==(0):work = False
				elif pause_button==(1):quick_save()
				elif pause_button==(2):quick_load()
				elif pause_button==(3):id_current=0;work = False
				lastPad = time()
			elif pad.down and (not lastPad or time() - lastPad >= 0.5):pause_button+=1;lastPad = time()
			elif pad.up and (not lastPad or time() - lastPad >= 0.5):pause_button-=1;lastPad = time()
			screen.swap()
		else:
			screen.blit(ui_pause, dx=x_now, blend=True)
			x_now+=3
			psp2d.Timer(0.2)
			if x_now >=(x_fin):
				x_now = x_fin
				animation = False
			screen.swap()