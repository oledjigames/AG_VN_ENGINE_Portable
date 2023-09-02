def anim_fade():
	anim_fade_img = psp2d.Image("engine/anim_img/anim_fade.png")
	active = True
	opacity = 0
	while active:
		if opacity==(100):
			active = False
		else:
			opacity+=1
			screen.blit(anim_fade_img, blend=True)
			psp2d.Timer(0.5)
			screen.swap()
def anim_char(id, characterid, text, x_pos):
	global id_current, background_screen, character, character_files
	if id_current==(id):
		play_anim = True
		speed_anim = 3
		if text==("from_left"):
			start_pos = -110
			while play_anim:
				start_pos+=speed_anim
				if start_pos>=(x_pos):
					play_anim=False
				screen.blit(background_screen)
				for a, b in character:
					screen.blit(a, dx=b, blend=True)
				screen.blit(character_files[characterid], dx=start_pos, blend=True)
				psp2d.Timer(0.2)
				screen.swap()
		if text==("left_to"):
			start_pos = x_pos
			while play_anim:
				start_pos+=speed_anim
				if start_pos>=(480):
					play_anim=False
				screen.blit(background_screen)
				for a, b in character:
					screen.blit(a, dx=b, blend=True)
				screen.blit(character_files[characterid], dx=start_pos, blend=True)
				psp2d.Timer(0.2)
				screen.swap()
		id_current+=1
def anim_eye(id, text):
	global id_current, background_screen, character
	play_anim=True
	speed_anim = 3
	anim_eye_u = psp2d.Image("engine/anim_img/eye_u.png")
	anim_eye_d = psp2d.Image("engine/anim_img/eye_d.png")
	if id_current ==(id):
		if text ==("open"):
			temp_y_u = 0
			temp_y_d = 0
			while play_anim:
				temp_y_u -= speed_anim
				temp_y_d += speed_anim
				screen.blit(background_screen)
				for a, b in character:
					screen.blit(a, dx=b, blend=True)
				screen.blit(anim_eye_u, dy=temp_y_u, blend=True)
				screen.blit(anim_eye_d, dy=temp_y_d, blend=True)
				if temp_y_d>=(270):
					play_anim=False
				psp2d.Timer(0.2)
				screen.swap()
		if text ==("close"):
			temp_y_u = -272
			temp_y_d = 272
			while play_anim:
				temp_y_u += speed_anim
				temp_y_d -= speed_anim
				screen.blit(background_screen)
				for a, b in character:
					screen.blit(a, dx=b, blend=True)
				screen.blit(anim_eye_u, dy=temp_y_u, blend=True)
				screen.blit(anim_eye_d, dy=temp_y_d, blend=True)
				if temp_y_d<=(0):
					play_anim=False
				psp2d.Timer(0.2)
				screen.swap()
		id_current+=1