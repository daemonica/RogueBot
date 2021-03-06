import random
import rooms.roomloader as roomloader

name = 'Распутье'

room_type = 'other'

def get_actions(user):
	all_visited_rooms = user.get_perma_variable('visited_rooms', [ ])
	rooms = user.get_room_temp('rooms')

	actions = [ ]

	for room_type, room_name in rooms:
		if room_name in all_visited_rooms or not room_type.startswith('monster'):
			loaded_room = roomloader.load_room(room_name, room_type)
			actions.append([loaded_room.name])
		else:
			actions.append(['?????'])

	return actions

def enter(user, reply):
	rooms = [  ]

	while len(rooms) < 4:
		rm = roomloader.get_next_room(user)
		loaded_room = roomloader.load_room(rm[1], rm[0])

		if random.random() < 0.05:
			rm = ('special', 'rick_astley')

		if not loaded_room.not_for_sign:
			rooms.append(rm)


	user.set_room_temp('rooms', list(set(rooms)))

def action(user, reply, text):
	rooms = user.get_room_temp('rooms')
	for room_type, room_name in rooms:
		loaded_room = roomloader.load_room(room_name, room_type)
		if loaded_room.name == text:
			if random.random() < 0.1:
				reply('Что-то пошло не так, ты увидел фезку пролетающую у тебя над головой. Ощущения будто был нарушен межпространственный континуум.')
				user.open_room(reply)
			else:
				user.open_room(reply, room_type, room_name)
			return

	reply('Такого выбора тебе не давали.')

