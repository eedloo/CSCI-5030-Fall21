def check(command):
	while True:
		received = input()
		if received == 'succeeded ' + command:
			return True
		elif received.startswich('failed ' + command):
			return False
		def action(command):
			print('start ' + command)
			return check_for_success(command)
		action('ShowMenu()')
		action('HideMenu()')
action ('CreateCharacter(Tom, D)')
action ('SetExpression(Tom, Happy)')
action ('SetClothing(Tom, Merchant)')
action ('SetHairStyle(Tom, mage_beard)')
action ('ShowMenu()')
action ('HideMenu()')
action ('CreatePlace(CastleBedroom,CastleBedroom )')
action ('SetPosition(Tom, CastleBedroom)')
action ('SetCameraFocus(Tom)')
action ('Wait(2)')
action ('Sleep(Tom, CastleBedroom.Bed)')
action ('Wait(2)')
action ('Sit(Tom, CastleBedroom.Bed)')
'''action ('Wait(2)')
action ('Exit(Tom, CastleBedroom.Door )')
action ('FadeOut()')
action ('CreatePlace(Hallway,Hallway )')
action ('SetPosition(Tom, Hallway.BackDoor)')
action ('FadeIn()')'''
action("CreateItem(Sword, Sword)")
action ('SetPosition(Sword, Tom)')
action('EnableIcon("SwordAttack",Sword, Tom)')
#action ('EnableIcon(\'open\', Hand, Hallway.Door,\'Go to the CastleBedroom,\',true)')
action ('WalkTo(Tom, Hallway.Door)')
while (True):
			input()

