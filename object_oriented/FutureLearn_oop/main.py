from room import Room

kitchen = Room('Kitchen')
kitchen.set_description('A lovely place to be')

dining_hall = Room('Dinning Hall')
dining_hall.set_description('A rom where whole family eats')

ballroom = Room('Ballroom')
ballroom.set_description('A vast room with wooden floor')

kitchen.link_room(dining_hall, 'south')
dining_hall.link_room(kitchen, 'north')
dining_hall.link_room(ballroom, 'west')
ballroom.link_room(dining_hall, 'east')

current_room = kitchen

while True:
    print('\n')
    current_room.get_details()
    command = input('>')
    current_room = current_room.move(command)


# print(kitchen)
